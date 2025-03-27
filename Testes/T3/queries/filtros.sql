-- Quais as 10 operadoras com maiores despesas em "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR" no último trimestre?
SELECT 
    dc.reg_ans, 
    oa.razao_social, 
    SUM(dc.vl_saldo_final) AS total_despesas
FROM demonstracoes_contabeis dc
JOIN operadoras_ativas oa ON dc.reg_ans = oa.registro_ans
WHERE dc.descricao = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTENCIA A SAUDE MEDICO HOSPITALAR'
  AND dc.data >= (SELECT MAX(data) FROM demonstracoes_contabeis) - INTERVAL '3 months'
GROUP BY dc.reg_ans, oa.razao_social
ORDER BY total_despesas DESC
LIMIT 10;


-- Quais as 10 operadoras com maiores despesas nessa categoria no último ano?
SELECT 
    dc.reg_ans, 
    oa.razao_social, 
    SUM(dc.vl_saldo_final) AS total_despesas
FROM demonstracoes_contabeis dc
JOIN operadoras_ativas oa ON dc.reg_ans = oa.registro_ans
WHERE dc.descricao = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTENCIA A SAUDE MEDICO HOSPITALAR'
  AND dc.data >= (SELECT MAX(data) FROM demonstracoes_contabeis) - INTERVAL '1 year'
GROUP BY dc.reg_ans, oa.razao_social
ORDER BY total_despesas DESC
LIMIT 10;
