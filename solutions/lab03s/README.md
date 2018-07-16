# Суперачивка №3

### Используте url2domain.py для отфильтровки данных, затем загрузите в таблицу, как в Лабораторной работе №3. Можно пропустить этот шаг, и использовать данные из ранее созданной таблицы

### Получаем число всех доменов
```
select count(*) from visits;
```
должны получить 6571038

###  Пoлучаем число автоюзеров

```
SELECT count(*)
FROM visits t1
INNER JOIN
(
  SELECT uid
    FROM visits
    GROUP BY uid
    HAVING SUM(CASE WHEN url_string='cars.ru'        THEN 1 ELSE 0 END)>9 OR 
           SUM(CASE WHEN url_string='avto-russia.ru' THEN 1 ELSE 0 END)>9 OR
           SUM(CASE WHEN url_string='bmwclub.ru'     THEN 1 ELSE 0 END)>9
) t2
ON t1.uid = t2.uid
```

должны получить 313527


### Мегазапрос с выгрузкой итогового файла в Хадуп

Назначаем переменным ранее полученные результаты - для простоты.

```
SET v1 = 313527;

SET v2 = 6571038;

SET va = ${hiveconf:v1} / ${hiveconf:v2};

WITH c1 AS (
    SELECT
        uid,
        url_string,
        COUNT(1) AS cnt,
        ROW_NUMBER() OVER(PARTITION BY uid ORDER BY COUNT(1) DESC) AS N
    FROM visits
    WHERE TRIM(url_string) in ('cars.ru', 'avto-russia.ru', 'bmwclub.ru')  
    GROUP BY uid, url_string 
    HAVING COUNT(1) > 9
), c2 AS (
    SELECT v.uid, v.url_string,
        CASE WHEN c1.uid IS NULL THEN 0 ELSE 1 END AS auto_user
    FROM visits v
    LEFT JOIN (SELECT uid FROM c1 WHERE N = 1) c1 ON c1.uid = v.uid
)
INSERT OVERWRITE DIRECTORY '/user/name.surname/lab03result_s'
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t'
STORED AS TEXTFILE
SELECT 
    url_string,
    CAST(
        POWER(SUM(auto_user) / ${hiveconf:v2}, 2) / ((COUNT(1) / ${hiveconf:v2}) * ${hiveconf:va})
        AS DECIMAL(21,20)
    ) AS cnt
FROM c2
GROUP BY url_string
SORT BY cnt DESC, url_string
LIMIT 200;
```


