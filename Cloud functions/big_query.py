import pandas as pd
import pyarrow
from google.cloud import bigquery
from google.cloud import storage
import warnings
warnings.filterwarnings("ignore")


def pasar_a_bigquery(event, context):
    bucket = event['bucket']
    archivo = event['name']

    id_proyecto = 'silicon-carver-416314'  
    id_dataset = 'proyecto_final'      
    id_tabla = 'Recorridos de taxis'          

    referencia_tabla = bigquery.Client(project=id_proyecto).dataset(id_dataset).table(id_tabla)

    configuracion_carga = bigquery.LoadJobConfig(write_disposition=bigquery.WriteDisposition.WRITE_APPEND, source_format=bigquery.SourceFormat.PARQUET)

    ruta = f'gs://{bucket}/{archivo}'
    

    df = pd.read_parquet(ruta, engine='pyarrow')
    

    cargar_bigquery = bigquery.Client(project=id_proyecto).load_table_from_dataframe(df, referencia_tabla, job_config=configuracion_carga)

    cargar_bigquery.result()

    print(f'\n\nDatos cargados en BigQuery desde {archivo}.\n\n')