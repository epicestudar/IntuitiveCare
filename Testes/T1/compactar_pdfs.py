import os
import zipfile

# Diretório base do projeto
base_dir = r'C:\Vinicius-DEV\IntuitiveCare\Testes\T1'

# Diretório onde os PDFs foram salvos
output_dir = os.path.join(base_dir, 'anexos')

# Diretório onde o ZIP será salvo
zip_dir = os.path.join(base_dir, 'zip')
os.makedirs(zip_dir, exist_ok=True)

# Nome do arquivo ZIP de saída
zip_filename = os.path.join(zip_dir, 'anexos.zip')

# Verifica se o ZIP já existe
if os.path.exists(zip_filename):
    resposta = input(f'O arquivo {zip_filename} já existe. Deseja sobrescrevê-lo? (s/n): ').strip().lower()
    if resposta != 's':
        print('Operação cancelada.')
        exit()

# Criar o arquivo ZIP contendo apenas arquivos PDF
with zipfile.ZipFile(zip_filename, 'w') as zipf:
    for root, _, files in os.walk(output_dir):
        for file in files:
            if file.endswith('.pdf'):
                zipf.write(os.path.join(root, file), arcname=file)

print(f'Arquivo ZIP criado com sucesso: {zip_filename}')
