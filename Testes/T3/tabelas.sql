-- Criar tabela para Demonstrações Contábeis
CREATE TABLE demonstracoes_contabeis (
    id SERIAL PRIMARY KEY,
    data DATE NOT NULL,
    reg_ans VARCHAR(20) NOT NULL,
    cd_conta_contabil VARCHAR(50) NOT NULL,
    descricao TEXT NOT NULL,
    vl_saldo_inicial NUMERIC(18,2) NOT NULL,
    vl_saldo_final NUMERIC(18,2) NOT NULL,
    ano INT,
    trimestre VARCHAR(5)
);

-- Criar tabela para Operadoras Ativas
CREATE TABLE operadoras_ativas (
    id SERIAL PRIMARY KEY,
    registro_ans VARCHAR(20) NOT NULL,
    cnpj VARCHAR(20) NOT NULL,
    razao_social TEXT NOT NULL,
    nome_fantasia TEXT,
    modalidade TEXT NOT NULL,
    logradouro TEXT,
    numero VARCHAR(15),
    complemento TEXT,
    bairro TEXT,
    cidade TEXT,
    uf VARCHAR(2),
    cep VARCHAR(15),
    ddd VARCHAR(5),
    telefone VARCHAR(20),
    fax VARCHAR(20),
    endereco_eletronico TEXT,
    representante TEXT,
    cargo_representante TEXT,
    regiao_de_comercializacao TEXT,
    data_registro_ans DATE
);
