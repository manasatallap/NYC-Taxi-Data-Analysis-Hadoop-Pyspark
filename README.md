# NYC Taxi Data Analysis with Hadoop & Pyspark

## Overview
This project analyzes NYC Yellow Taxi data using **Hadoop MapReduce** and **PySpark**, demonstrating scalable data proceessing techniques. The project implements data analysis tasks, including trip distance aggregation, indentifying actie locations, and computing trends over time

## Technologies Used
- **Data Processing and Handling:** Hadoop, PySpark (DataFrame API)
- **Programming:** Python

## Implemented Tasks

### Hadoop MapReduce
1. Total Trip Distance by Pickup Location
2. Total Trip Distance by Pickup Hour
3. Distinct Drop-off Locations
4. Top 10 Longest Rides by Distance

### PySpark (DataFrame API)
Trips under 2 miles were excluded to focus on significant travel distances and reduce noice from short, frequent rides that may not offer meaningful insights 

1. Total Trip Distance by Pickup Location
2. Top 10 Most Active Locations (based on pickup/drop-off counts)
3. Top 3 Days with Highest Average Pickups
4. Most Active Brooklyn Zone Per Hour

## How to Run
git clone https://github.com/manasatallap/NYC-Taxi-Data-Analysis-Hadoop-Pyspark.git

### Hadoop
Needs to be run on Linux, WSL, or Mac. Java and ssh much be installed.
More detailed instructions: 
https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/SingleCluster.html

Run:
/usr/local/hadoop/bin/hadoop jar \
/usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming*.jar \
-reducer ./reducer1.py -mapper ./mapper1.py -input data.csv -output output

Change name of reducer and mapper files from 1-4 depending on task

### PySpark
Needs Java 8, 11, or 17 with JAVA_HOME properly set. Also needs Python 3.8 or above. 
Can be easily installed with pip install pyspark
More detailed instructions: https://spark.apache.org/docs/latest/api/python/getting_started/install.html#:~:text=Python%203.8%20and%20above.

Run:
./main1.py data.csv {output_directory}

Change name of main files from 1-3 depending on task

For Task 4:
./main4.py data.ccv map.csv output4




