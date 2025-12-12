from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    request = p.request.new_context()

    payload = {"title": "Hello", "body": "World", "userId": 1}

    response = request.post(
        "https://jsonplaceholder.typicode.com/posts",
        data=payload
    )

    print("Status:", response.status)
    print("Created:", response.json())
