from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    request=p.request.new_context()

    response=request.get("https://jsonplaceholder.typicode.com/posts/1")
    print("Status",response.status)
    print("Response JSON:", response.json())