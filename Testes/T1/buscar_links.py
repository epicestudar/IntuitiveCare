import requests
import json
import os
from bs4 import BeautifulSoup

# Diretório base do projeto
base_dir = r'C:\Vinicius-DEV\IntuitiveCare\Testes\T1'

# Diretório para armazenar o JSON
dados_dir = os.path.join(base_dir, 'links')
os.makedirs(dados_dir, exist_ok=True)

# Caminho do arquivo JSON
json_file = os.path.join(dados_dir, 'pdf_links.json')

# Verifica se o arquivo já existe
if os.path.exists(json_file):
    resposta = input(f'O arquivo {json_file} já existe. Deseja sobrescrevê-lo? (s/n): ').strip().lower()
    if resposta != 's':
        print('Operação cancelada.')
        exit()

# URL da página principal
url = 'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos'

# Fazer a requisição GET
response = requests.get(url)
response.raise_for_status()

# Analisar o HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Encontrar todos os links na página
links = soup.find_all('a', href=True)

# Filtrar apenas os links que levam a PDFs
pdf_links = [link['href'] for link in links if ('Anexo_I' in link['href'] or 'Anexo_II' in link['href']) and link['href'].endswith('.pdf')]

# Salvar os links em um arquivo JSON
with open(json_file, 'w') as f:
    json.dump(pdf_links, f, indent=4)

print(f'Links dos PDFs salvos em {json_file}')
