show tables;
select * from scorers;
describe scorers;
select * from results;
describe results;
select * from shootout;
describe shootout;



select * from Vista_1;
-- consultas --


-- Mejores 15 goleadores hasta la ultima actualización
#create view Vista_1 AS 
#SELECT scorervista_1vista_1, COUNT(*) AS cantidad_de_goles
#FROM scorers
#GROUP BY scorer
#ORDER BY cantidad_de_goles DESC
#vista_1limit 15;

-- 2 equipo que ha sido ganador más veces en casa
SELECT home_team, COUNT(*) AS GEC
FROM results
GROUP BY home_team
order by GEC DESC;


-- 3 equipo que ha sido ganador más veces como visitante

SELECT away_team, COUNT(*) AS GEC
FROM results
GROUP BY away_team
ORDER BY GEC DESC;

-- Equipos con la mayor cantidad de victorias en shootouts
SELECT
    home_team AS equipo,
    COUNT(*) AS victorias_en_shootout
FROM
    shootout
WHERE
    winner = home_team
GROUP BY
    home_team
ORDER BY
    victorias_en_shootout DESC;

-- Goleadores más exitosos en partidos recientes
SELECT r.dates, s.scorer,
    COUNT(*) AS goles FROM results r JOIN scorers s ON r.id_scorers = s.id_scorers
WHERE
    r.dates >= DATE_SUB(CURDATE(), INTERVAL 1 MONTH)
GROUP BY
    r.dates, s.scorer
ORDER BY
    goles DESC;


