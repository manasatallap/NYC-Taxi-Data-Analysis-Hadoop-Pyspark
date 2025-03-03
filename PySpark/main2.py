#!/usr/bin/env python3

from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import sys

# Initialize Spark session
spark = SparkSession.builder.appName("Task2").getOrCreate()

# Get input and output paths from command line arguments
input_data = sys.argv[1]
output_dir = sys.argv[2]

# Read input data
df = spark.read.csv(input_data, header=True, inferSchema=True)

# Count pickups by location
pickup_counts = df.groupBy("PULocationID").count().withColumnRenamed("count", "pickup_count")

# Count drop-offs by location
dropoff_counts = df.groupBy("DOLocationID").count().withColumnRenamed("count", "dropoff_count")

# Rename columns for joining
pickup_counts = pickup_counts.withColumnRenamed("PULocationID", "LocationID")
dropoff_counts = dropoff_counts.withColumnRenamed("DOLocationID", "LocationID")

# Join pickup and drop-off counts
activity = pickup_counts.join(dropoff_counts, "LocationID", "outer").fillna(0)

# Calculate total activity
activity = activity.withColumn("total_activity", col("pickup_count") + col("dropoff_count"))

# Get top 10 locations by total activity
top10 = (activity.select("LocationID")
         .orderBy(col("total_activity").desc(), col("LocationID").asc())
         .limit(10))

# Write results to output directory
top10.write.csv(output_dir, mode="overwrite", header=False)

# Stop Spark session
spark.stop()
