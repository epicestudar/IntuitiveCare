# Importação das bibliotecas necessárias
import requests
import json
import os
import logging
from bs4 import BeautifulSoup

# Diretórios do projeto de teste 1
base_dir = r'C:\Vinicius-DEV\IntuitiveCare\Testes\T1'
log_dir = os.path.join(base_dir, 'log')
os.makedirs(log_dir, exist_ok=True)  # Garante que a pasta de logs existe

# Configuração do logging
log_file = os.path.join(log_dir, 'logs.txt')
logging.basicConfig(filename=log_file, level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Diretório para armazenar o JSON que terá os links dos PDF's
dados_dir = os.path.join(base_dir, 'links')
os.makedirs(dados_dir, exist_ok=True)

# Caminho do arquivo JSON
json_file = os.path.join(dados_dir, 'pdf_links.json')

# Verifica se o arquivo já existe
if os.path.exists(json_file):
    resposta = input(f'O arquivo {json_file} já existe. Deseja sobrescrevê-lo? (s/n): ').strip().lower()
    # Se o usuário digitar algo diferente de 's' a operação será cancelada
    if resposta != 's':
        print('Operação cancelada.')
        exit()

# URL da página principal
url = 'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos'

# Fazer a requisição GET e verificar se houve algum erro durante a requisição
try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    logging.info("Página acessada com sucesso.")
except requests.exceptions.RequestException as e:
    logging.error(f"Erro ao acessar a URL {url}: {e}")
    print(f"Erro ao acessar a URL: {e}")
    exit()

# Analisa o HTML da página
soup = BeautifulSoup(response.text, 'html.parser')

# Encontra todos os links na página
links = soup.find_all('a', href=True)

# Filtra apenas os links que levam à PDF's que contenham 'Anexo_1' ou 'Anexo_2' e que terminem com '.pdf'
pdf_links = [link['href'] for link in links if ('Anexo_I' in link['href'] or 'Anexo_II' in link['href']) and link['href'].endswith('.pdf')]

# Salva os links em um arquivo JSON
with open(json_file, 'w') as f:
    json.dump(pdf_links, f, indent=4)

# Imprime uma mensagem de sucesso com o nome do arquivo JSON que foi criado
logging.info(f"Links dos PDFs salvos em {json_file}")
print(f'Links dos PDFs salvos em {json_file}')
