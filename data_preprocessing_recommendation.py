
import pandas as pd
from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder.master("local").appName("RetailRecommender").getOrCreate()

# Sample transaction data
data = {
    "user_id": [1, 2, 3, 4, 5, 6],
    "product_id": [101, 102, 103, 101, 104, 102],
    "rating": [5, 3, 4, 5, 2, 4],
}

# Create DataFrame
df = pd.DataFrame(data)
spark_df = spark.createDataFrame(df)

# Show the DataFrame
spark_df.show()
