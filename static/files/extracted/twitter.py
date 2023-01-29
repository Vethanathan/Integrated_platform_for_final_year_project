import requests
import json

bearer_token = "AAAAAAAAAAAAAAAAAAAAAMq%2BlQEAAAAAE14vVOXX16%2BPUZYwxE5e5QYXR44%3DiJYypPiwdwpESHcAMfEtPSz70XqjQYTNFZAuYhmpuEB4Ea3YXe"
# Set up your Twitter API credentials
api_key = "5CqARkK98cBXCtpKLw3m5ov0p"
api_secret_key = "X2rz7OCv0aBbtLqQkvxIovTxlk5JZsCYc13goa4nV9xDFs2zLl"
access_token = "1406258634946793474-GLfAIfIZSBPQ3GpkHjT3YxeLQIgS3Z"
access_token_secret = "BL79OQCM5yg88wxKyv581gEMbq2uWt9vsuwmxJHiANzV5"

headers = {
    "Authorization": f"Bearer {api_key} {api_secret_key} {access_token} {access_token_secret}"
}

# Set up the request body
data = {
    "status": "Hello, world! This is a tweet from my Twitter bot."
}

# Send a POST request to the /tweets endpoint
response = requests.post("https://api.twitter.com/2/tweets", headers=headers, json=data)

# Print the response from the API
print(response.json())
