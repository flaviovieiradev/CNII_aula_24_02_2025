from azure.storage.blob import BlobServiceClient

def upload_file_to_azure(container_name, local_file_path, blob_name):
    # Configurar a conexão com o Azure
    connect_str = "Coloque aqui a sua connection string"
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    
    # Obter o cliente do container
    container_client = blob_service_client.get_container_client(container_name)
    
    # Fazer upload do arquivo
    with open(local_file_path, "rb") as data:
        container_client.upload_blob(name=blob_name, data=data)
    
    print(f'Arquivo {local_file_path} enviado para o container {container_name} como {blob_name}.')

def download_file_from_azure(container_name, blob_name, local_file_path):
    # Configurar a conexão com o Azure
    connect_str = "Coloque aqui a sua connection string"
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    
    # Obter o cliente do container
    container_client = blob_service_client.get_container_client(container_name)
    
    # Fazer download do arquivo
    with open(local_file_path, "wb") as download_file:
        blob_client = container_client.get_blob_client(blob_name)
        download_file.write(blob_client.download_blob().readall())
    
    print(f'Arquivo {blob_name} baixado do container {container_name} para {local_file_path}.')

if __name__ == "__main__":
    container_name = "imagem"
    
    # Exemplo de upload de arquivo
    local_file_to_upload = "Coloque aqui o caminho e o nome do arquivo a ser feito o upload"
    blob_name = "Coloque aqui o nome do arquivo que você quer fazer o upload"
    upload_file_to_azure(container_name, local_file_to_upload, blob_name)
    
    # Exemplo de download de arquivo
    blob_name_to_download = "Coloque aqui o nome do arquivo que você quer fazer o download."
    local_file_to_download = "Coloque aqui o caminho e o nome do arquivo, o destino onde você quer salvar o arquivo"
    download_file_from_azure(container_name, blob_name_to_download, local_file_to_download)