#!/usr/bin/env python3

from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import sys

spark = SparkSession.builder.appName("Task1").getOrCreate()

input_data = sys.argv[1]
output_dir = sys.argv[2]

df = spark.read.csv(input_data, header=True, inferSchema=True)

filtered_df = df.filter(df["trip_distance"] > 2)

result = (filtered_df.groupBy("PULocationID")
          .sum("trip_distance")
          .withColumnRenamed("sum(trip_distance)", "total_distance"))

result = result.withColumn("total_distance", col("total_distance").cast("decimal(10, 2)"))

sorted_result = result.orderBy("PULocationID")

sorted_result.write.csv(output_dir, mode="overwrite", header=False)
spark.stop()
