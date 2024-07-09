-- CTE (Common Table Expression) para preparar dados de interações.
WITH Interactions AS (
  -- Primeira parte da CTE: Seleciona interações listando PERSONAGEM A como "character" e PERSONAGEM B como "friend".
  -- Isso garante que cada relação entre personagens seja vista a partir da perspectiva de PERSONAGEM A.
  SELECT `PERSONAGEM A` AS character, `PERSONAGEM B` AS friend
  FROM `dataset.dataset1`
  
  UNION ALL  -- Usa UNION ALL para combinar os resultados do primeiro SELECT com o segundo SELECT.
  
  -- Segunda parte da CTE: Inverte os papéis de PERSONAGEM A e PERSONAGEM B.
  -- Isso garante que as interações sejam simétricas, considerando PERSONAGEM B agora como "character" e PERSONAGEM A como "friend".
  SELECT `PERSONAGEM B` AS character, `PERSONAGEM A` AS friend
  FROM `dataset.dataset1`
),
-- Segunda CTE para identificar amigos em comum entre os pares de personagens.
CommonFriends AS (
  -- Realiza um JOIN entre duas instâncias da CTE "Interactions".
  -- "a" e "b" são aliases para duas instâncias separadas de "Interactions".
  SELECT a.character AS personagem1, b.character AS personagem2, a.friend AS common_friend
  FROM Interactions a
  JOIN Interactions b 
  ON a.friend = b.friend  -- Condição de JOIN que vincula amigos comuns entre dois personagens.
  AND a.character < b.character  -- Evita duplicatas, garantindo que cada par seja único e não repetido.
)
-- Consulta final que utiliza a CTE "CommonFriends" para produzir o resultado final.
SELECT 
  personagem1,  -- Primeiro personagem do par
  personagem2,  -- Segundo personagem do par
  COUNT(common_friend) AS total_amigos_em_comum,  -- Conta quantos amigos em comum cada par de personagens tem.
  STRING_AGG(common_friend, ',') AS lista_amigos_em_comum  -- Agrega todos os amigos em comum em uma única string, separados por vírgula.
FROM CommonFriends
-- Agrupa os resultados por personagem1 e personagem2 para aplicar as funções de agregação.
GROUP BY personagem1, personagem2
-- Filtra para incluir apenas os pares que têm um ou mais amigos em comum.
HAVING total_amigos_em_comum > 0;
