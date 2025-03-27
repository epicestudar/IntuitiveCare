import pandas as pd
from pathlib import Path

# Caminho base das demonstrações contábeis
base_path = Path(r"C:\Vinicius-DEV\IntuitiveCare\Testes\T3\demonstracoes_contabeis")

# Anos e trimestres a serem processados
anos = ["2023", "2024"]
trimestres = ["1T", "2T", "3T", "4T"]

# Percorrer cada ano e trimestre
for ano in anos:
    for trimestre in trimestres:
        csv_path = base_path / ano / f"{trimestre}{ano}.csv"

        # Verifica se o arquivo existe antes de processar
        if csv_path.exists():
            print(f"Processando: {csv_path}")

            # Carrega o CSV como string para evitar problemas de conversão automática
            df = pd.read_csv(csv_path, delimiter=";", dtype=str)

            # Substituir vírgulas por pontos nas colunas numéricas
            df["VL_SALDO_INICIAL"] = df["VL_SALDO_INICIAL"].str.replace(",", ".")
            df["VL_SALDO_FINAL"] = df["VL_SALDO_FINAL"].str.replace(",", ".")

            # Salvar de volta no formato correto
            df.to_csv(csv_path, sep=";", index=False)
            print(f"✔ Arquivo atualizado: {csv_path}")
        else:
            print(f"⚠ Arquivo não encontrado: {csv_path}")
