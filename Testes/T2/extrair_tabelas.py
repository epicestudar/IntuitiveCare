import camelot
import pandas as pd
import zipfile
import os

# Caminho do arquivo PDF
pdf_file = r'C:\Vinicius-DEV\IntuitiveCare\Testes\T1\anexos\Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf'

# Tentar extrair as tabelas usando o flavor 'lattice' (para tabelas com bordas visíveis)
tables_lattice = camelot.read_pdf(pdf_file, pages='all', flavor='lattice')
if tables_lattice:
    print("Tabelas extraídas com 'lattice'.")
    tables = tables_lattice
else:
    print("Nenhuma tabela encontrada com 'lattice'. Tentando 'stream'.")
    # Se o lattice não encontrar, tenta com 'stream' (para tabelas baseadas em texto)
    tables_stream = camelot.read_pdf(pdf_file, pages='all', flavor='stream')
    if tables_stream:
        print("Tabelas extraídas com 'stream'.")
        tables = tables_stream
    else:
        print("Nenhuma tabela encontrada.")
        exit()

# Concatenar todas as tabelas extraídas (se houver mais de uma)
df_list = [table.df for table in tables]
df = pd.concat(df_list, ignore_index=True)

# Definir um dicionário de substituições
abreviacoes = {
    'OD': 'Seg. Odontológica',
    'AMB': 'Seg. Ambulatorial'
}

# Substituir as abreviações nas colunas do DataFrame
df.replace(abreviacoes, inplace=True)

# Caminho para salvar o arquivo CSV
csv_file = r'C:\Vinicius-DEV\IntuitiveCare\Testes\T2\dados\rol_procedimentos.csv'

# Garantir que o diretório de destino exista
os.makedirs(os.path.dirname(csv_file), exist_ok=True)

# Salvar os dados extraídos e modificados em um arquivo CSV
df.to_csv(csv_file, index=False)
print(f'Dados salvos com sucesso em {csv_file}')

# Caminho para o arquivo ZIP de saída
zip_filename = r'C:\Vinicius-DEV\IntuitiveCare\Testes\T2\zip\Teste_Vinicius.zip'

# Garantir que o diretório do ZIP exista
os.makedirs(os.path.dirname(zip_filename), exist_ok=True)

# Compactar o CSV em um arquivo ZIP
with zipfile.ZipFile(zip_filename, 'w') as zipf:
    zipf.write(csv_file, os.path.basename(csv_file))

print(f'Arquivo ZIP com as substituições criado com sucesso: {zip_filename}')
