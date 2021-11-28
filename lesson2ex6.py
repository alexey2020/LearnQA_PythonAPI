import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)

print(f"Количество редиректов равно: {len(response.history)}")
print(f"Конечный URL: {response.url}")
