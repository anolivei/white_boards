/* 
Exercício de SQL no Hackerrank
*/
SELECT dist.id, nomes.nome, SUM(dist.distancia)
AS total
FROM dist
INNER JOIN nomes
ON dist.id=nomes.id
GROUP BY nomes.id, nomes.nome
LIMIT 100
