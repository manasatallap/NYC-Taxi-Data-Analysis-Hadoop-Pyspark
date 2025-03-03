#!/usr/bin/env python3

from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import sys

# Initialize Spark session
spark = SparkSession.builder.appName("Task1").getOrCreate()

# Get input and output paths from command line arguments
input_data = sys.argv[1]
output_dir = sys.argv[2]

# Read input data
df = spark.read.csv(input_data, header=True, inferSchema=True)

# Filter trips with distance greater than 2
filtered_df = df.filter(df["trip_distance"] > 2)

# Group by pick-up location and sum trip distances
result = (filtered_df.groupBy("PULocationID")
          .sum("trip_distance")
          .withColumnRenamed("sum(trip_distance)", "total_distance"))

# Cast total distance to decimal
result = result.withColumn("total_distance", col("total_distance").cast("decimal(10, 2)"))

# Sort results by pick-up location ID
sorted_result = result.orderBy("PULocationID")

# Write results to output directory
sorted_result.write.csv(output_dir, mode="overwrite", header=False)

# Stop Spark session
spark.stop()
