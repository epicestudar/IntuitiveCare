-- Importar os arquivos de Demonstrações Contábeis para o PostgreSQL
COPY demonstracoes_contabeis (data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
FROM 'C:/Vinicius-DEV/IntuitiveCare/Testes/T3/demonstracoes_contabeis/2023/1T2023.csv'
DELIMITER ';' CSV HEADER;

-- Atualizar os dados carregados com o ano e o trimestre corretos
UPDATE demonstracoes_contabeis
SET ano = 2023, trimestre = '1T'
WHERE ano IS NULL AND trimestre IS NULL;

-- Importar os arquivos de Demonstrações Contábeis para o PostgreSQL
COPY demonstracoes_contabeis (data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
FROM 'C:/Vinicius-DEV/IntuitiveCare/Testes/T3/demonstracoes_contabeis/2023/2T2023.csv'
DELIMITER ';' CSV HEADER;

-- Atualizar os dados carregados com o ano e o trimestre corretos
UPDATE demonstracoes_contabeis
SET ano = 2023, trimestre = '2T'
WHERE ano IS NULL AND trimestre IS NULL;

-- Importar os arquivos de Demonstrações Contábeis para o PostgreSQL
COPY demonstracoes_contabeis (data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
FROM 'C:/Vinicius-DEV/IntuitiveCare/Testes/T3/demonstracoes_contabeis/2023/3T2023.csv'
DELIMITER ';' CSV HEADER;

-- Atualizar os dados carregados com o ano e o trimestre corretos
UPDATE demonstracoes_contabeis
SET ano = 2023, trimestre = '3T'
WHERE ano IS NULL AND trimestre IS NULL;

-- Importar os arquivos de Demonstrações Contábeis para o PostgreSQL
COPY demonstracoes_contabeis (data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
FROM 'C:/Vinicius-DEV/IntuitiveCare/Testes/T3/demonstracoes_contabeis/2023/4T2023.csv'
DELIMITER ';' CSV HEADER;

-- Atualizar os dados carregados com o ano e o trimestre corretos
UPDATE demonstracoes_contabeis
SET ano = 2023, trimestre = '4T'
WHERE ano IS NULL AND trimestre IS NULL;

-- Importar os arquivos de Demonstrações Contábeis para o PostgreSQL
COPY demonstracoes_contabeis (data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
FROM 'C:/Vinicius-DEV/IntuitiveCare/Testes/T3/demonstracoes_contabeis/2024/1T2024.csv'
DELIMITER ';' CSV HEADER;

-- Atualizar os dados carregados com o ano e o trimestre corretos
UPDATE demonstracoes_contabeis
SET ano = 2024, trimestre = '1T'
WHERE ano IS NULL AND trimestre IS NULL;

-- Importar os arquivos de Demonstrações Contábeis para o PostgreSQL
COPY demonstracoes_contabeis (data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
FROM 'C:/Vinicius-DEV/IntuitiveCare/Testes/T3/demonstracoes_contabeis/2024/2T2024.csv'
DELIMITER ';' CSV HEADER;

-- Atualizar os dados carregados com o ano e o trimestre corretos
UPDATE demonstracoes_contabeis
SET ano = 2024, trimestre = '2T'
WHERE ano IS NULL AND trimestre IS NULL;

-- Importar os arquivos de Demonstrações Contábeis para o PostgreSQL
COPY demonstracoes_contabeis (data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
FROM 'C:/Vinicius-DEV/IntuitiveCare/Testes/T3/demonstracoes_contabeis/2024/3T2024.csv'
DELIMITER ';' CSV HEADER;

-- Atualizar os dados carregados com o ano e o trimestre corretos
UPDATE demonstracoes_contabeis
SET ano = 2024, trimestre = '3T'
WHERE ano IS NULL AND trimestre IS NULL;

-- Importar os arquivos de Demonstrações Contábeis para o PostgreSQL
COPY demonstracoes_contabeis (data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
FROM 'C:/Vinicius-DEV/IntuitiveCare/Testes/T3/demonstracoes_contabeis/2024/4T2024.csv'
DELIMITER ';' CSV HEADER;

-- Atualizar os dados carregados com o ano e o trimestre corretos
UPDATE demonstracoes_contabeis
SET ano = 2024, trimestre = '4T'
WHERE ano IS NULL AND trimestre IS NULL;

-- Importar o arquivo de Operadoras Ativas para o PostgreSQL
COPY operadoras_ativas (registro_ans, cnpj, razao_social, nome_fantasia, modalidade, logradouro, numero, complemento, bairro, cidade, uf, cep, ddd, telefone, fax, endereco_eletronico, representante, cargo_representante, regiao_de_comercializacao, data_registro_ans)
FROM 'C:/Vinicius-DEV/IntuitiveCare/Testes/T3/operadoras_ativas/Relatorio_cadop.csv'
DELIMITER ';' CSV HEADER;

-- Atualizar o nome fantasia das operadoras para 'Não informado' caso este seja nulo
UPDATE operadoras_ativas 
SET nome_fantasia = 'Não informado' 
WHERE nome_fantasia IS NULL;