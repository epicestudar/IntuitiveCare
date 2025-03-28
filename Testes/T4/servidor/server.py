from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from fastapi.responses import JSONResponse

# Caminho do CSV
CSV_PATH = "C:/Vinicius-DEV/IntuitiveCare/Testes/T3/operadoras_ativas/Relatorio_cadop.csv"

# Carregar os dados no início
df = pd.read_csv(CSV_PATH, delimiter=";", dtype=str)

# Normalizar os nomes das colunas para evitar problemas
df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

app = FastAPI()

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Pode ser alterado para o domínio específico (ex: ['http://localhost:8080'])
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos os métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permitir todos os cabeçalhos
)

@app.get("/search")
def search_operadoras(query: str = Query(..., min_length=2)):
    """
    Busca operadoras pelo nome fantasia, razão social ou CNPJ.
    """
    query = query.lower()

    # Filtrar os dados com base no nome, razão social ou CNPJ
    results = df[  # Buscando o valor
        df["nome_fantasia"].str.lower().str.contains(query, na=False) |
        df["razao_social"].str.lower().str.contains(query, na=False) |
        df["cnpj"].str.contains(query, na=False)
    ].fillna("").to_dict(orient="records")  # Preenchendo NaN antes da conversão para lista

    return JSONResponse(content=results)
