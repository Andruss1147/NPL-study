# Лабораторная работа №3

### Используйте приложенный url2domains.py чтобы отфильтровать данные. (не забудьте сделать его исполняемым chmod +x url2domains.py)

`hadoop fs -cat /labs/lab03data/* | ./url2domains.py > filtered`

### Загружаем его в HDFS

`hadoop fs -put filtered /user/${USER}/`

### Создаем таблицу в Hive (здесь и далее используем Амбари)

```
DROP TABLE visits;

CREATE EXTERNAL TABLE visits(
    uid BIGINT, ts FLOAT, url_string STRING)
ROW FORMAT DELIMITED 
FIELDS TERMINATED BY ',';
```

### Загружаем данные в таблицу (внимание! При повторной загрузке надо сначала снова залить файл на HDSF (шаг 2)

`LOAD DATA INPATH '/user/name.surname/filtered' OVERWRITE INTO TABLE visits;`

### Мега запрос с выгрузкой итогового фала на Хадуп

```
WITH agg AS (
    SELECT uid, trim(url_string) as url_string, count(url_string) AS cnt
    FROM visits
    GROUP BY uid, url_string
    HAVING cnt > 9
), ungrouped AS (
    SELECT agg.uid,
        CASE WHEN agg.url_string IN ('cars.ru', 'avto-russia.ru', 'bmwclub.ru') THEN 1 ELSE 0 END AS auto_user,
        CASE WHEN agg.url_string IN ('zakon.kz', 'egov.kz', 'makler.md') THEN 1 ELSE 0 END AS business_user,
        CASE WHEN agg.url_string IN ('russianfood.com', 'psychologies.ru', 'gotovim.ru') THEN 1 ELSE 0 END AS home_user,
        CASE WHEN agg.url_string IN ('books.imhonet.ru', 'zhurnaly.biz', 'zvukobook.ru') THEN 1 ELSE 0 END AS book_user
    FROM agg
)
INSERT OVERWRITE DIRECTORY '/data/home/name.surname/lab03result'
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t'
STORED AS TEXTFILE
SELECT uid, MAX(auto_user) AS auto_user, MAX(business_user) AS business_user,
            MAX(home_user) AS home_user, MAX(book_user) AS book_user
FROM ungrouped
GROUP BY uid;
``` 

### Доп. Кирилл упомянул способ фильтровать данные при загрузке. Проверьте сами, работает ли, и как.

```
ADD FILE /data/home/kilrill.danilyuk/lab03/url2domain.py;
SELECT TRANSFORM(uid, ts, url_string)
    USING 'url2domain.py'
    AS uid, ts, url_string
FROM visits;
```

