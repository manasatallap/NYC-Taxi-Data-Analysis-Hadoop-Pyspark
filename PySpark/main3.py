#!/usr/bin/env python3

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, dayofweek, date_format, count
import sys

# Initialize Spark session
spark = SparkSession.builder.appName("Task3").getOrCreate()

# Get input and output paths from command line arguments
input_data = sys.argv[1]
output_dir = sys.argv[2]

# Read input data
df = spark.read.csv(input_data, header=True, inferSchema=True)

# Extract day of the week from pickup datetime
df = df.withColumn("day_of_week", dayofweek("tpep_pickup_datetime"))

# Get day name from pickup datetime
df = df.withColumn("day_name", date_format("tpep_pickup_datetime", "EEEE"))

# Calculate average pickups by day of the week
avg_pickups = (df.groupBy("day_name", "day_of_week")
               .agg(count("*").alias("total_pickups"))
               .groupBy("day_name", "day_of_week")
               .avg("total_pickups")
               .withColumnRenamed("avg(total_pickups)", "average_pickups"))

# Get top 3 days by average pickups
top3_days = (avg_pickups.orderBy(col("average_pickups").desc(), col("day_of_week").asc())
             .select("day_name")
             .limit(3))

# Write results to output directory
top3_days.write.csv(output_dir, mode="overwrite", header=False)

# Stop Spark session
spark.stop()
