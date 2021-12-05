# -*- coding: utf-8 -*-

from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark = SparkSession.builder.appName("CrimeAnal").getOrCreate()

    df1 = spark.read.load("hdfs:///user/maria_dev/CrimePlaceCnt2.csv",
    format="csv",sep=",",inferSchema="true",header="true")  

    df1.create("CrimeMax")  

    result= spark.sql("""
    SELECT city_name,city_cnt
    FROM CrimeMax 
    """)

    for row in result.collect():
        print(row.city_name,row.city_cnt)  