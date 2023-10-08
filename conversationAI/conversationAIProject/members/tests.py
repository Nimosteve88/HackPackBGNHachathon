import requests

# Replace 'YOUR_API_KEY' with your actual News API key
api_key = 'b2c8adec9244439385335aee2daf292e'

# Define the API endpoint for Nigeria news
url = f'https://newsapi.org/v2/top-headlines?country=ng&apiKey={api_key}'

# Send a GET request to the API
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Check if the 'articles' key exists in the response
    if 'articles' in data:
        # Iterate through the list of articles and print the titles
        for article in data['articles']:
            title = article.get('title')
            if title:
                print(title)
    else:
        print("No articles found in the response.")
else:
    print(f"Failed to fetch news. Status code: {response.status_code}")
