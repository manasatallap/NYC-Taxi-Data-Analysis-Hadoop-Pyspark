# NYC Taxi Data Analysis with Hadoop & PySpark
## Overview
This project demonstrates large-scale data processing capabilities by analyzing NYC Yellow Taxi trip data using both **Hadoop MapReduce** and **PySpark**. The analysis includes computing trip distances, identifying high-traffic locations, and analyzing temporal patterns in taxi services.

## Getting Started

### Prerequisites
- **Hadoop Setup:**
  - Supported platforms: Linux, WSL, or macOS
  - Java Runtime Environment
  - SSH server
  - Hadoop installation ([Official Setup Guide](https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/SingleCluster.html))

- **PySpark Setup:**
  - Python 3.8+
  - Java 8/11/17 with JAVA_HOME configured
  - PySpark (`pip install pyspark`)

### Installation
```bash
git clone https://github.com/manasatallap/NYC-Taxi-Data-Analysis-Hadoop-Pyspark.git
cd NYC-Taxi-Data-Analysis-Hadoop-Pyspark
```

### Running the Analysis

#### Hadoop MapReduce Tasks
```bash
/usr/local/hadoop/bin/hadoop jar \
/usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming*.jar \
-reducer ./reducer{N}.py -mapper ./mapper{N}.py \
-input ../data.csv -output output
```
Replace `{N}` with task number (1-4)

#### PySpark Tasks
```bash
# Tasks 1-3
./main{N}.py ../data.csv output_directory

# Task 4 (Brooklyn Zone Analysis)
./main4.py ../data.csv map.csv output4
```
Replace `{N}` with task number (1-3)

## Analysis Tasks

### Hadoop MapReduce Implementation
1. **Pickup Location Distance Analysis**: Aggregates total trip distances by pickup location
2. **Hourly Distance Patterns**: Analyzes trip distances grouped by pickup hour
3. **Drop-off Location Distribution**: Identifies unique drop-off locations
4. **Distance-Based Trip Analysis**: Determines the top 10 longest trips

### PySpark Implementation
*Note: All analyses exclude trips under 2 miles to focus on significant travel patterns*

1. **Location-Based Distance Analysis**: Calculates total trip distances per pickup location
2. **Activity Hotspots**: Identifies top 10 locations based on combined pickup/drop-off frequency
3. **Weekly Peak Analysis**: Determines the three busiest days based on average pickup counts
4. **Brooklyn Hourly Patterns**: Analyzes the most active zones in Brooklyn for each hour

## Data Sources
- **Trip Data**: NYC Taxi & Limousine Commission's [Trip Record Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)
- **Data Dictionary**: Available [here](https://www.nyc.gov/assets/tlc/downloads/pdf/data_dictionary_trip_records_yellow.pdf)
- **Zone Mapping**: TLC Taxi Zone Lookup Table from [NYC Open Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)

## Technologies Used
- Data Processing and Handling: Hadoop, PySpark (DataFrame API)
- Programming: Python
