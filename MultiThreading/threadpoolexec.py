import concurrent.futures
import requests

websites =[
    "https://www.example.com",
    "https://www.python.org",
    "https://www.github.com",
    "https://www.stackoverflow.com",
    "https://www.reddit.com"
]

def check_website(url):
    try:
        response =requests.get(url, timeout=3)
        if response.status_code == 200:
            print(f"{url} is alive")
        else:
            print(f"{url} returned status (response.status_code)")
    except requests.RequestException:
        print(f"{url} is down..")

with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    executor.map(check_website, websites)