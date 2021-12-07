-- CrimeAnal.csv 파일에에에서 범죄 발생장소별 빈도수 내림차순으로 뽑아내기 HiveQL 이용 

CREATE TABLE `crimeplaceanal`(
`index` int,
`crime_cnt` int,
`crime_type` string,
`crime_place` string)
ROW FORMAT SERDE
'org.apache.hadoop.hive.ql.io.orc.OrcSerde'
STORED AS INPUTFORMAT
'org.apache.hadoop.hive.ql.io.orc.OrcInputFormat'
OUTPUTFORMAT
'org.apache.hadoop.hive.ql.io.orc.OrcOutputFormat'
LOCATION
'hdfs://sandbox-hdp.hortonworks.com:8020/apps/hive/warehouse/crimeplaceanal'
TBLPROPERTIES (
'COLUMN_STATS_ACCURATE'='{\"BASIC_STATS\":\"true\"}',
'numFiles'='1',
'numRows'='661',
'rawDataSize'='128226',
'totalSize'='2052',
'transient_lastDdlTime'='1638806908')

-- 범죄 발생장소별 빈도수 내림차순

SELECT crimeplaceanal.crime_place as place, sum(crimeplaceanal.crime_cnt) as sum 
FROM crimeplaceanal
GROUP BY crimeplaceanal.crime_place
ORDER BY sum DESC