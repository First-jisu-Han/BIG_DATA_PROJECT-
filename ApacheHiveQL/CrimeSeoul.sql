-- CrimeRegions.csv 에서 서울의 전체 범죄 빈도수와 서울의 구단위 마다 범죄 빈도수를 내림차순으로 뽑아내기 HIVEQL 이용 

CREATE TABLE `crimeregions`(
`crime_place` string,
`crime_cnt` int)
ROW FORMAT SERDE
'org.apache.hadoop.hive.ql.io.orc.OrcSerde'
STORED AS INPUTFORMAT
'org.apache.hadoop.hive.ql.io.orc.OrcInputFormat'
OUTPUTFORMAT
'org.apache.hadoop.hive.ql.io.orc.OrcOutputFormat'
LOCATION
'hdfs://sandbox-hdp.hortonworks.com:8020/apps/hive/warehouse/crimeregions'
TBLPROPERTIES (
'COLUMN_STATS_ACCURATE'='{\"BASIC_STATS\":\"true\"}',
'numFiles'='1',
'numRows'='39529',
'rawDataSize'='3872542',
'totalSize'='33218',
'transient_lastDdlTime'='1638760863')

-- 서울의 전체 범죄 빈도수

SELECT sum(crimeregions.crime_cnt)
FROM crimeregions
WHERE crimeregions.crime_place LIKE '서울%'

-- 서울의 구단위 마다 범죄 빈도수를 내림차순

SELECT crimeregions.crime_place as place ,sum(crimeregions.crime_cnt) as sum
FROM crimeregions
WHERE crimeregions.crime_place LIKE '서울%'
GROUP BY crimeregions.crime_place
ORDER BY sum DESC

