from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from fastapi.responses import JSONResponse
import logging

# Caminho do meu arquivo CSV
CSV_PATH = "C:/Vinicius-DEV/IntuitiveCare/Testes/T3/operadoras_ativas/Relatorio_cadop.csv"

# Carregamento dos dados uma vez na inicialização do servidor
df = None

app = FastAPI()

# Configuração do CORS (em produção, restrinja origens para maior segurança)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, substitua "*" por origens específicas
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Carregar os dados quando o servidor for iniciado
@app.on_event("startup")
async def load_data():
    global df
    try:
        df = pd.read_csv(CSV_PATH, delimiter=";", dtype=str)
        df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
        logging.info("Arquivo CSV carregado com sucesso.")
    except Exception as e:
        logging.error(f"Erro ao carregar o arquivo CSV: {e}")

# Endpoint para buscar operadoras pelo nome fantasia, razão social ou CNPJ. Retorna resultados em JSON.
@app.get("/search")
def search_operadoras(
    query: str = Query(..., min_length=2),
    page: int = Query(1, ge=1),  # Página inicial
    page_size: int = Query(10, le=100),  # Número de resultados por página
):
    """
    Busca operadoras pelo nome fantasia, razão social ou CNPJ com paginação.
    """
    # Validando se o 'query' é alfanumérico
    if not query.isalnum():
        return JSONResponse(status_code=400, content={"message": "A consulta deve conter apenas caracteres alfanuméricos."})

    query = query.lower()

    # Filtro dos dados com base no nome, razão social ou CNPJ
    filtered_data = df[
        df["nome_fantasia"].str.lower().fillna("").str.contains(query) |
        df["razao_social"].str.lower().fillna("").str.contains(query) |
        df["cnpj"].str.contains(query, na=False)
    ].fillna("")

    # Paginação dos resultados
    start = (page - 1) * page_size
    end = start + page_size
    results = filtered_data.iloc[start:end].to_dict(orient="records")

    return JSONResponse(content=results)

