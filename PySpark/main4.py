#!/usr/bin/env python3

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, hour, count
from pyspark.sql.window import Window
from pyspark.sql.functions import row_number
import sys

spark = SparkSession.builder.appName("Task4").getOrCreate()

input_data = sys.argv[1]
map_data = sys.argv[2]
output_dir = sys.argv[3]

df = spark.read.csv(input_data, header=True, inferSchema=True)
map_df = spark.read.csv(map_data, header=True, inferSchema=True)

brooklyn_zones = map_df.filter(map_df["borough"] == "Brooklyn")

df = df.withColumn("hour", hour("tpep_pickup_datetime"))

brooklyn_pickups = df.join(brooklyn_zones, df["PULocationID"] == map_df["LocationID"])

hourly_pickups = brooklyn_pickups.groupBy("hour", "zone").agg(count("*").alias("pickup_count"))

window_spec = Window.partitionBy("hour").orderBy(col("pickup_count").desc(), col("zone").asc())
ranked_pickups = hourly_pickups.withColumn("rank", row_number().over(window_spec))

top_zones_per_hour = ranked_pickups.filter(col("rank") == 1).select("hour", "zone")

top_zones_per_hour.orderBy("hour").write.csv(output_dir, mode="overwrite", header=False)

spark.stop()
