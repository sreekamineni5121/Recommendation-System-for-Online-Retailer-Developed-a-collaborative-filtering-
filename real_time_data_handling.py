
# Function to simulate real-time transaction processing
def process_real_time_data(new_data):
    new_df = pd.DataFrame(new_data)
    new_spark_df = spark.createDataFrame(new_df)
    return new_spark_df

# Simulate incoming transactions
new_transactions = {
    "user_id": [1, 2],
    "product_id": [105, 106],
    "rating": [4, 5],
}
real_time_df = process_real_time_data(new_transactions)

# Show the incoming data
real_time_df.show()

# Optionally, you can append this data to your existing dataset for further training
