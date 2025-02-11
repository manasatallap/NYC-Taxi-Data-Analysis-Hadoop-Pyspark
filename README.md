# NYC Taxi Data Analusis with Hadoop & Pyspark

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
git clone


