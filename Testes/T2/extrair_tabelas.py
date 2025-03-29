import camelot
import pandas as pd
import zipfile
import os
import shutil
import logging

# Diretórios do projeto
base_dir = r'C:\Vinicius-DEV\IntuitiveCare\Testes\T2'
log_dir = os.path.join(base_dir, 'log')
dados_dir = os.path.join(base_dir, 'dados')
zip_dir = os.path.join(base_dir, 'zip')
pdf_dir_t1 = r'C:\Vinicius-DEV\IntuitiveCare\Testes\T1\anexos'  # Diretório do PDF na pasta T1
pdf_dir_t2 = os.path.join(base_dir, 'anexos')  # Diretório de destino na pasta T2

# Criar diretórios se não existirem
os.makedirs(log_dir, exist_ok=True)
os.makedirs(dados_dir, exist_ok=True)
os.makedirs(zip_dir, exist_ok=True)
os.makedirs(pdf_dir_t2, exist_ok=True)

# Configuração do logging
log_file = os.path.join(log_dir, 'logs.txt')
logging.basicConfig(filename=log_file, level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Caminho do arquivo PDF na pasta T1 e T2
pdf_file_t1 = os.path.join(pdf_dir_t1, 'Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf')
pdf_file_t2 = os.path.join(pdf_dir_t2, 'Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf')

# Caminho do arquivo CSV de saída
csv_file = os.path.join(dados_dir, 'rol_procedimentos.csv')

# Caminho para o arquivo ZIP de saída
zip_filename = os.path.join(zip_dir, 'Teste_Vinicius.zip')

try:
    # Verificar se o PDF existe em T2, se não, copiar de T1
    if not os.path.exists(pdf_file_t2):
        shutil.copy(pdf_file_t1, pdf_file_t2)
        logging.info(f"Arquivo PDF copiado para {pdf_file_t2}")
        print(f"Arquivo PDF copiado para {pdf_file_t2}")
    else:
        logging.info(f"O arquivo PDF já existe em {pdf_file_t2}")
        print(f"O arquivo PDF já existe em {pdf_file_t2}")

    # Tentar extrair tabelas com 'stream' (baseado em texto)
    tables = camelot.read_pdf(pdf_file_t2, pages='all', flavor='stream')

    # Se 'stream' não encontrar tabelas, tentar com 'lattice' (baseado em linhas)
    if not tables.n:
        logging.warning("Nenhuma tabela encontrada com 'stream'. Tentando com 'lattice'.")
        tables = camelot.read_pdf(pdf_file_t2, pages='all', flavor='lattice')

    # Se ainda assim não encontrar tabelas, encerrar o script
    if not tables.n:
        logging.error("Nenhuma tabela foi encontrada no PDF.")
        print("Nenhuma tabela foi encontrada no PDF.")
        exit()
    
    logging.info(f"{tables.n} tabelas extraídas do PDF.")

    # Concatenar todas as tabelas extraídas
    df_list = [table.df for table in tables]
    df = pd.concat(df_list, ignore_index=True)

    # Dicionário de substituições para abreviações
    abreviacoes = {
        'OD': 'Seg. Odontológica',
        'AMB': 'Seg. Ambulatorial'
    }

    # Aplicar substituições no DataFrame
    df.replace(abreviacoes, inplace=True)

    # Verificar se o CSV já existe
    if os.path.exists(csv_file):
        resposta = input(f"O arquivo '{csv_file}' já existe. Deseja sobrescrevê-lo? (s/n): ").strip().lower()
        if resposta != 's':
            logging.info("Operação cancelada pelo usuário. CSV não sobrescrito.")
            print("Operação cancelada. O arquivo não será sobrescrito.")
            exit()

    # Salvar o CSV
    df.to_csv(csv_file, index=False)
    logging.info(f'Dados salvos com sucesso em {csv_file}')
    print(f'Dados salvos com sucesso em {csv_file}')

    # Verificar se o ZIP já existe
    if os.path.exists(zip_filename):
        resposta = input(f"O arquivo ZIP '{zip_filename}' já existe. Deseja sobrescrevê-lo? (s/n): ").strip().lower()
        if resposta != 's':
            logging.info("Operação cancelada pelo usuário. ZIP não sobrescrito.")
            print("Operação cancelada. O arquivo ZIP não será sobrescrito.")
            exit()

    # Compactar o CSV em um arquivo ZIP
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(csv_file, os.path.basename(csv_file))

    logging.info(f'Arquivo ZIP criado com sucesso: {zip_filename}')
    print(f'Arquivo ZIP criado com sucesso: {zip_filename}')

except Exception as e:
    logging.error(f"Erro inesperado: {e}")
    print(f"Ocorreu um erro inesperado: {e}")
