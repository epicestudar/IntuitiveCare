# Importação das bibliotecas necessárias para construção do servidor que será integrado com a interface
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from fastapi.responses import JSONResponse

# Caminho do meu arquivo CSV
CSV_PATH = "C:/Vinicius-DEV/IntuitiveCare/Testes/T3/operadoras_ativas/Relatorio_cadop.csv"

# Carregamento dos dados
df = pd.read_csv(CSV_PATH, delimiter=";", dtype=str)

# Normalização dos nomes das colunas para evitar problemas de caracteres
df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

app = FastAPI()

# Configuração do CORS para evitar problemas na interface
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos os cabeçalhos
)

# Endpoint para buscar operadoras pelo nome fantasia, razão social ou CNPJ. Retorna resultados em JSON.
@app.get("/search")
def search_operadoras(query: str = Query(..., min_length=2)):
    """
    Busca operadoras pelo nome fantasia, razão social ou CNPJ.
    """
    query = query.lower()

    # Filtro dos dados com base no nome, razão social ou CNPJ
    results = df[  # Buscando o valor
        df["nome_fantasia"].str.lower().str.contains(query, na=False) |
        df["razao_social"].str.lower().str.contains(query, na=False) |
        df["cnpj"].str.contains(query, na=False)
    ].fillna("").to_dict(orient="records")  # Preenchendo NaN antes da conversão para lista

    # Retorno com a busca
    return JSONResponse(content=results)
