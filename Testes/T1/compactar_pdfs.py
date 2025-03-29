# Importação das bibliotecas necessárias
import os
import zipfile
import logging

# Diretórios do projeto de teste 1
base_dir = r'C:\Vinicius-DEV\IntuitiveCare\Testes\T1'
log_dir = os.path.join(base_dir, 'log')
os.makedirs(log_dir, exist_ok=True)

# Configuração do logging
log_file = os.path.join(log_dir, 'logs.txt')
logging.basicConfig(filename=log_file, level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Diretório onde os PDFs foram salvos
output_dir = os.path.join(base_dir, 'anexos')

# Diretório onde o ZIP será salvo
zip_dir = os.path.join(base_dir, 'zip')
os.makedirs(zip_dir, exist_ok=True)

# Nome do arquivo ZIP de saída
zip_filename = os.path.join(zip_dir, 'anexos.zip')

# Verifica se o ZIP já existe, caso já exista uma mensagem aparecerá e perguntará se o usuário deseja sobreescrever o arquivo e o usuário terá que responder com 's' ou 'n'
if os.path.exists(zip_filename):
    resposta = input(f'O arquivo {zip_filename} já existe. Deseja sobrescrevê-lo? (s/n): ').strip().lower()
    # Se o usuário digitar algo diferente de 's' a operação será cancelada
    if resposta != 's':
        print('Operação cancelada.')
        exit()

# Criação do arquivo ZIP contendo apenas arquivos PDF
try:
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(output_dir):
            for file in files:
                if file.endswith('.pdf'):
                    zipf.write(os.path.join(root, file), arcname=file)
    logging.info(f"Arquivo ZIP criado com sucesso: {zip_filename}")
    print(f'Arquivo ZIP criado com sucesso: {zip_filename}')
except Exception as e:
    logging.error(f"Erro ao criar o arquivo ZIP: {e}")
    print(f"Erro ao criar o arquivo ZIP: {e}")
