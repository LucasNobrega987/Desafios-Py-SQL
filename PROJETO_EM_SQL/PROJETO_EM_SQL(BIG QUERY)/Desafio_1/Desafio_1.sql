-- Criar uma tabela para armazenar os resultados das interações
CREATE OR REPLACE TABLE dataset.interacoes_resultados AS
SELECT 
    personagem,
    SUM(IF(livro = 1, peso, 0)) AS interacoes_livro1,
    SUM(IF(livro = 2, peso, 0)) AS interacoes_livro2,
    SUM(IF(livro = 3, peso, 0)) AS interacoes_livro3,
    SUM(peso) AS total_interacoes
FROM (
    SELECT `PERSONAGEM A` AS personagem, PESO, LIVRO FROM `dataset.dataset1`
    UNION ALL
    SELECT `PERSONAGEM B` AS personagem, PESO, LIVRO FROM `dataset.dataset1`
)
GROUP BY personagem
ORDER BY total_interacoes DESC;
