from google.cloud import storage
import pandas as pd
import pyarrow
import warnings
warnings.filterwarnings("ignore")


def verificar_archivo_existente_2(bucket_name, file_name):
    client = storage.Client()
    bucket = client.get_bucket(bucket_name)
    for blob in bucket.list_blobs():
        if blob.name.endswith(file_name):
            return True
    return False


def positivos(valor:float|int) -> float|int:
    try:
        if type(valor) == float:
            return float(abs(valor))
        else:
            return int(abs(valor))
    except:
        return -1
    
        
def revision_nulos(data:pd.DataFrame) -> dict:
    print()
    print()
    print('Nulos')
    print()
    print()
    porcentaje_nulos_dict = {}
    for columna in data.columns:
        nulos = data[columna].isnull().sum()
        total = len(data[columna])
        porcentaje = round(nulos/total*100,2)
        porcentaje_nulos_dict[columna] = porcentaje
        print()
        print(f'Columna: {columna:<20}      Cantidad de nulos: {nulos:<7}      Porcentaje de nulos: {str(porcentaje) + " %":<8}')
        print()
    return porcentaje_nulos_dict


def reemplazar_nan_float(valor:float) -> float:
    if pd.isnull(valor):
        return float(-1)
    else:
        return float(valor)
        

def reemplazar_nan_int(valor:float) -> int:
    if pd.isnull(valor):
        return int(-1)
    else:
        return int(valor)
    

def mediana_columna_float(data:pd.Series) -> float:
    return float(round(data.median(), 2))


def mediana_columna_int(data:pd.Series) -> int:
    return int(data.median())


def reemplazar_nan_mediana_int(columna:str, data:pd.DataFrame) -> None:
    mediana = mediana_columna_int(data[columna][~data[columna].isnull()])
    def mediana_f_i(valor:float) -> int:
        if pd.isnull(valor):
            return int(mediana)
        else:
            return int(valor)
    data[columna] = data[columna].apply(mediana_f_i)
        

def reemplazar_nan_mediana_float(columna:str, data:pd.DataFrame) -> None:
    mediana = mediana_columna_float(data[columna][~data[columna].isnull()])
    def mediana_f_f(valor:float) -> float:
        if pd.isnull(valor):
            return float(mediana)
        else:
            return float(valor)
    data[columna] = data[columna].apply(mediana_f_f)



def revision_duplicados(data:pd.DataFrame) -> None:
    print()
    print('Duplicados')
    print()
    duplicados = data.duplicated().sum()
    total = len(data)
    porcentaje = round(duplicados/total*100,2)
    print()
    print(f'Cantidad de duplicados: {duplicados:<7}      Porcentaje de duplicados: {str(porcentaje) + " %":<8}')
    print()
    if duplicados > 0:
        data = data.drop_duplicates()
        print()
        print()
        print(f'Se eliminaron {duplicados} registros duplicados.')
        print()
        print()


    
def limite_pasajeros(cantidad:int) -> int:
    if cantidad > 4:
        return int(-1)
    else:
        return int(cantidad)
    
def borrar_registros(data:pd.DataFrame) -> None:
    antes = data.shape[0]
    data = data.drop(data[(data['passenger_count'] == 0) | (data['trip_distance'] == 0) | (data['fare_amount'] == 0)].index)
    despues = data.shape[0]
    print()
    print()
    print(f'Se borraron {antes-despues} registros.')
    print()
    print()

def etl_taxis(event, context):
    # Crea una instancia del cliente de Cloud Storage
    client = storage.Client()
    bucket = event['bucket']
    archivo = event['name']
    nombre_nuevo = f'{archivo[:-8]}_limpio.parquet'
    print()
    print()
    print(f'Archivo: {archivo}')

    if verificar_archivo_existente_2('datasets_limpios_taxis', nombre_nuevo):
        print()
        print()
        print(f'El archivo {nombre_nuevo} ya existe en el bucket "datasets_limpios_taxis". No se realizará el procesamiento.')
        print()
        print()
        return


    df = pd.read_parquet(f'gs://{bucket}/{archivo}', engine='pyarrow')
    
    shape_inicio = df.shape

       
    nuevos_nombres = {'tpep_pickup_datetime': 'start_trip', 'tpep_dropoff_datetime': 'end_trip', 'passenger_count': 'passenger_count',
                  'trip_distance': 'trip_distance', 'PULocationID': 'pu_location_id', 'DOLocationID': 'do_location_id', 'fare_amount': 'fare_amount',
                  'total_amount': 'total_amount', 'congestion_surcharge': 'congestion_surcharge', 'payment_type': 'payment_type',
                  'tip_amount': 'tip_amount', 'lpep_pickup_datetime': 'start_trip', 'lpep_dropoff_datetime': 'end_trip'}

    df.rename(columns=nuevos_nombres, inplace=True)

    columnas_a_borrar = []
    for columna in df.columns:
        if columna not in nuevos_nombres.values():
            columnas_a_borrar.append(columna)
    
    df = df.drop(columnas_a_borrar, axis=1)

    if 'yellow' in archivo:
        df['type_of_taxi'] = 0
    else:
        df['type_of_taxi'] = 1

    borrar_registros(df)
    

    for columna in df.columns[2:-1]:
        df[columna] = df[columna].apply(positivos)
      
    nulos_dict = revision_nulos(df)

    for columna in df.columns[2:-1]:
        if df[columna].isnull().sum() == 0:
            continue
        else:
            if columna == 'pu_location_id' or columna == 'do_location_id' or columna == 'payment_type' or columna == 'congestion_surcharge':
                df[columna] = df[columna].apply(reemplazar_nan_int)
            elif columna == 'passenger_count':
                if nulos_dict[columna] >= 10:
                    df[columna] = df[columna].apply(reemplazar_nan_int)
                else:
                    reemplazar_nan_mediana_int(columna, df)
            else:
                if nulos_dict[columna] >= 10:
                    df[columna] = df[columna].apply(reemplazar_nan_float)
                else:
                    reemplazar_nan_mediana_float(columna, df)
    
    revision_duplicados(df)

    df['passenger_count'] = df['passenger_count'].apply(limite_pasajeros)

    df = df.drop(df['trip_distance'][df['trip_distance'] > 20].index)
    df = df.drop(df[(df['fare_amount']>0) & (df['trip_distance']==0)].index)
    df = df.drop(df[(df['fare_amount']>300) & (df['trip_distance']<20)].index)
    df = df.drop(df[(df['fare_amount']>100) & (df['trip_distance']<5)].index)
    df['payment_type'][df['payment_type'] == 2] = -1

    shape_final = df.shape
    print()
    print()
    print('Shape:')
    print()
    print()
    print(f'Inicio: {shape_inicio}   Final: {shape_final}')
    print()
    print()

    ruta = 'gs://datasets_limpios_taxis/'
    df.to_parquet(f'{ruta}{archivo[:-8]}_limpio.parquet')

     
