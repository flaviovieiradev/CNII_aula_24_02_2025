from azure.data.tables import TableServiceClient, UpdateMode
from azure.core.exceptions import ResourceExistsError

# Configurações iniciais
connection_string = "Insira a sua connection string"
table_name = "Nome da tabela"

# Conectando ao serviço de Tabelas
table_service_client = TableServiceClient.from_connection_string(conn_str=connection_string)

# Criando uma tabela
try:
    table_client = table_service_client.create_table_if_not_exists(table_name)
    print(f"Tabela '{table_name}' criada com sucesso!")
except ResourceExistsError:
    table_client = table_service_client.get_table_client(table_name)
    print(f"Tabela '{table_name}' já existe.")

# Função para inserir um novo registro (Create)
def insert_entity(entity: dict):
    table_client.create_entity(entity)
    print(f"Entidade inserida: {entity}")

# Função para ler um registro (Read)
def read_entity(partition_key, row_key):
    entity = table_client.get_entity(partition_key=partition_key, row_key=row_key)
    print(f"Entidade lida: {entity}")
    return entity

# Função para atualizar um registro (Update)
def update_entity(entity: dict):
    table_client.update_entity(entity, mode=UpdateMode.MERGE)
    print(f"Entidade atualizada: {entity}")

# Função para deletar um registro (Delete)
def delete_entity(partition_key, row_key):
    table_client.delete_entity(partition_key=partition_key, row_key=row_key)
    print(f"Entidade com PartitionKey='{partition_key}' e RowKey='{row_key}' deletada.")

# Entidade exemplo
entity = {
    'PartitionKey': 'clientes',
    'RowKey': '001',
    'Nome': 'Insira um nome',
    'Email': 'Insira um e-mail',
    'Idade': 00
}

# Criar entidade
insert_entity(entity)

# Ler entidade
read_entity('clientes', '001')

# Atualizar entidade
#entity['Idade'] = 22
#update_entity(entity)

# Deletar entidade
#delete_entity('clientes', '001')
