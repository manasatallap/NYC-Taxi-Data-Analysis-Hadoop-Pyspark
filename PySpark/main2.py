#!/usr/bin/env python3

from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import sys
spark = SparkSession.builder.appName("Task2").getOrCreate()
input_data = sys.argv[1]
output_dir = sys.argv[2]

df = spark.read.csv(input_data, header=True, inferSchema=True)

pickup_counts = df.groupBy("PULocationID").count().withColumnRenamed("count", "pickup_count")
dropoff_counts = df.groupBy("DOLocationID").count().withColumnRenamed("count", "dropoff_count")

pickup_counts = pickup_counts.withColumnRenamed("PULocationID", "LocationID")
dropoff_counts = dropoff_counts.withColumnRenamed("DOLocationID", "LocationID")

activity = pickup_counts.join(dropoff_counts, "LocationID", "outer").fillna(0)

activity = activity.withColumn("total_activity", col("pickup_count") + col("dropoff_count"))

top10 = (activity.select("LocationID")
         .orderBy(col("total_activity").desc(), col("LocationID").asc())
         .limit(10))

top10.write.csv(output_dir, mode="overwrite", header=False)

spark.stop()

