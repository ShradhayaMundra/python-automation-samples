import requests

def fetch_api_data():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        for item in data[:5]:
            print(item["title"])

if __name__ == "__main__":
    fetch_api_data()
