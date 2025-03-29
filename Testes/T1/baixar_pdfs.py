# Importação das bibliotecas necessárias
import os
import json
import requests
import time
import logging

# Diretórios do projeto de teste 1
base_dir = r'C:\Vinicius-DEV\IntuitiveCare\Testes\T1'
log_dir = os.path.join(base_dir, 'log')
os.makedirs(log_dir, exist_ok=True)

# Configuração do logging
log_file = os.path.join(log_dir, 'logs.txt')
logging.basicConfig(filename=log_file, level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Diretório onde os PDFs serão salvos
output_dir = os.path.join(base_dir, 'anexos')
os.makedirs(output_dir, exist_ok=True)

# Caminho do arquivo JSON
json_file = os.path.join(base_dir, 'links', 'pdf_links.json')

# Verifica se o arquivo JSON existe, caso não exista uma mensagem será exibida
if not os.path.exists(json_file):
    logging.error(f'Erro: O arquivo {json_file} não foi encontrado.')
    print(f'Erro: O arquivo {json_file} não foi encontrado. Execute buscar_links.py primeiro.')
    exit()

# Carrega os links do arquivo JSON
with open(json_file, 'r') as f:
    pdf_links = json.load(f)

# Função para baixar um PDF
def download_pdf(url, output_dir, max_retries=3):
    filename = os.path.join(output_dir, url.split('/')[-1])

    # Verifica se o arquivo já existe, caso já exista o download será pulado
    if os.path.exists(filename):
        logging.info(f'O arquivo {filename} já existe. Pulando download.')
        print(f'O arquivo {filename} já existe. Pulando download...')
        return
    
    # Tentativa de download com timeout de 10 segundos e até 3 tentativas
    retries = 0
    while retries < max_retries:
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            with open(filename, 'wb') as f:
                f.write(response.content)
            logging.info(f'Download concluído: {filename}')
            print(f'Download concluído: {filename}')
            return
        except requests.exceptions.RequestException as e:
            retries += 1
            logging.warning(f"Tentativa {retries} falhou para {url}: {e}")
            print(f"Erro ao baixar {url}, tentativa {retries}/{max_retries}: {e}")
            time.sleep(2)
    logging.error(f"Falha ao baixar {url} após {max_retries} tentativas.")
    print(f"Falha ao baixar {url} após {max_retries} tentativas.")

# Baixa cada PDF
for pdf_link in pdf_links:
    if not pdf_link.startswith('http'):
        pdf_link = 'https://www.gov.br' + pdf_link
    download_pdf(pdf_link, output_dir)

# Imprime uma mensagem de sucesso
logging.info("Todos os PDFs foram processados com sucesso!")
print("Todos os PDFs foram processados com sucesso!")
