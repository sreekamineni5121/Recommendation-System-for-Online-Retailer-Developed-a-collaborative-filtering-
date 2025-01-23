
from pyspark.sql import functions as F

# Example API function to fetch top 5 recommendations for a user
def get_recommendations(user_id):
    user_recommendations = recommendations.filter(recommendations.user_id == user_id).collect()
    return user_recommendations[0]["recommendations"]

# Example of usage: fetch recommendations for user 1
user_recommendations = get_recommendations(1)
print(user_recommendations)
