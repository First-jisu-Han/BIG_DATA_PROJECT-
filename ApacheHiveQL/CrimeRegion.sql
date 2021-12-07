-- CrimeRegion.csv 파일에서 지역별 범죄 빈도수 내림차순 뽑아내기 HiveQL 이용 

CREATE TABLE `crimeregion`(
`city_name` string,
`city_cnt` int)
ROW FORMAT SERDE
'org.apache.hadoop.hive.ql.io.orc.OrcSerde'
STORED AS INPUTFORMAT
'org.apache.hadoop.hive.ql.io.orc.OrcInputFormat'
OUTPUTFORMAT
'org.apache.hadoop.hive.ql.io.orc.OrcOutputFormat'
LOCATION
'hdfs://sandbox-hdp.hortonworks.com:8020/apps/hive/warehouse/crimeregion'
TBLPROPERTIES (
'COLUMN_STATS_ACCURATE'='{\"BASIC_STATS\":\"true\"}',
'numFiles'='1',
'numRows'='561',
'rawDataSize'='52650',
'totalSize'='1475',
'transient_lastDdlTime'='1638726202')

-- 지역별 범죄 빈도수 내림차순

SELECT crimeregion.city_name, sum(crimeregion.city_cnt) as sum
FROM crimeregion
GROUP BY crimeregion.city_name
ORDER BY sum DESC