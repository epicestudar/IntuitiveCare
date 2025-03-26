import os
import json
import requests

# Diretório base do projeto
base_dir = r'C:\Vinicius-DEV\IntuitiveCare\Testes\T1'

# Diretório onde os PDFs serão salvos
output_dir = os.path.join(base_dir, 'anexos')
os.makedirs(output_dir, exist_ok=True)

# Caminho do arquivo JSON
json_file = os.path.join(base_dir, 'links', 'pdf_links.json')

# Verifica se o arquivo JSON existe
if not os.path.exists(json_file):
    print(f'Erro: O arquivo {json_file} não foi encontrado. Execute buscar_links.py primeiro.')
    exit()

# Carregar os links do arquivo JSON
with open(json_file, 'r') as f:
    pdf_links = json.load(f)

# Função para baixar e salvar um PDF
def download_pdf(url, output_dir):
    filename = os.path.join(output_dir, url.split('/')[-1])
    
    # Verifica se o arquivo já existe
    if os.path.exists(filename):
        print(f'O arquivo {filename} já existe. Pulando download...')
        return

    response = requests.get(url)
    response.raise_for_status()
    with open(filename, 'wb') as f:
        f.write(response.content)
    print(f'Download concluído: {filename}')

# Baixar cada PDF
for pdf_link in pdf_links:
    if not pdf_link.startswith('http'):
        pdf_link = 'https://www.gov.br' + pdf_link
    download_pdf(pdf_link, output_dir)

print("Todos os PDFs foram processados com sucesso!")
