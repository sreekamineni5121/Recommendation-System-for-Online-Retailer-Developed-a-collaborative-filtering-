
from pyspark.ml.recommendation import ALS
from pyspark.sql.functions import col

# Convert to Spark DataFrame for ALS
als_data = spark_df.select(col("user_id"), col("product_id"), col("rating"))

# Build the ALS model
als = ALS(max_iter=10, reg_param=0.1, userCol="user_id", itemCol="product_id", ratingCol="rating", nonnegative=True, coldStartStrategy="drop")
model = als.fit(als_data)

# Generate product recommendations for all users
recommendations = model.recommendForAllUsers(5)

# Show the recommendations
recommendations.show()
