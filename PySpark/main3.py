#!/usr/bin/env python3

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, dayofweek, date_format, count
import sys

spark = SparkSession.builder.appName("Task3").getOrCreate()

input_data = sys.argv[1]
output_dir = sys.argv[2]

df = spark.read.csv(input_data, header=True, inferSchema=True)

df = df.withColumn("day_of_week", dayofweek("tpep_pickup_datetime"))

df = df.withColumn("day_name", date_format("tpep_pickup_datetime", "EEEE"))

avg_pickups = (df.groupBy("day_name", "day_of_week")
               .agg(count("*").alias("total_pickups"))
               .groupBy("day_name", "day_of_week")
               .avg("total_pickups")
               .withColumnRenamed("avg(total_pickups)", "average_pickups"))

top3_days = (avg_pickups.orderBy(col("average_pickups").desc(), col("day_of_week").asc())
             .select("day_name")
             .limit(3))

top3_days.write.csv(output_dir, mode="overwrite", header=False)

spark.stop()
