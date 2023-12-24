from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder.appName("DataTransformation").getOrCreate()

# Load the CSV data
df = spark.read.csv("input_data.csv", header=True, inferSchema=True)

# Perform data transformation (filter and aggregate)
filtered_df = df.filter(df["Age"] >= 30)
aggregated_df = filtered_df.groupBy("Name").agg({"Salary": "avg"})

# Print the results
aggregated_df.show()

# Save the results to a new CSV file
aggregated_df.write.csv("output_data.csv", header=True)

# Stop the Spark session
spark.stop()
