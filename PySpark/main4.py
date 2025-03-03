#!/usr/bin/env python3

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, hour, count
from pyspark.sql.window import Window
from pyspark.sql.functions import row_number
import sys

# Initialize Spark session
spark = SparkSession.builder.appName("Task4").getOrCreate()

# Get input and output paths from command line arguments
input_data = sys.argv[1]
map_data = sys.argv[2]
output_dir = sys.argv[3]

# Read input data and borough map data
df = spark.read.csv(input_data, header=True, inferSchema=True)
map_df = spark.read.csv(map_data, header=True, inferSchema=True)

# Filter for Brooklyn zones
brooklyn_zones = map_df.filter(map_df["borough"] == "Brooklyn")

# Extract hour from pickup datetime
df = df.withColumn("hour", hour("tpep_pickup_datetime"))

# Join taxi data with Brooklyn zones
brooklyn_pickups = df.join(brooklyn_zones, df["PULocationID"] == map_df["LocationID"])

# Aggregate pickups by hour and zone
hourly_pickups = brooklyn_pickups.groupBy("hour", "zone").agg(count("*").alias("pickup_count"))

# Define window specification for ranking
window_spec = Window.partitionBy("hour").orderBy(col("pickup_count").desc(), col("zone").asc())

# Rank pickups within each hour
ranked_pickups = hourly_pickups.withColumn("rank", row_number().over(window_spec))

# Filter for top zones per hour
top_zones_per_hour = ranked_pickups.filter(col("rank") == 1).select("hour", "zone")

# Write results to output directory
top_zones_per_hour.orderBy("hour").write.csv(output_dir, mode="overwrite", header=False)

# Stop Spark session
spark.stop()
