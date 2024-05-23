import requests
from bs4 import BeautifulSoup
from google.cloud import storage

def download_and_upload_parquet_files(request):
    # URL del sitio web a realizar el web scraping
    website = "https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page"
    response = requests.get(website)
    soup = BeautifulSoup(response.text, "html.parser")

    # Encontrar enlaces que apunten a archivos .parquet
    links = soup.find_all("a", href=lambda href: href and ("yellow_tripdata_2024" or "green_tripdata_2024") in href and ".parquet")

    # Inicializar el cliente de Google Cloud Storage
    storage_client = storage.Client()
    bucket = storage_client.bucket('datasets_taxis_nyc')  # Reemplaza 'tu_bucket' con el nombre de tu bucket

    for link in links:
        # Descargar el archivo .parquet
        file_url = link["href"]
        file_name = file_url.split("/")[-1]  # Obtener el nombre del archivo de la URL
        response = requests.get(file_url)
        if response.status_code == 200:
            # Subir el archivo .parquet a Google Cloud Storage
            blob = bucket.blob(file_name)
            blob.upload_from_string(response.content)
            print(f"Archivo {file_name} subido a Google Cloud Storage.")
        else:
            print(f"No se pudo descargar el archivo {file_url}.")

    return "Proceso completado."
