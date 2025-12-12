from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    request=p.request.new_context(
        base_url="https://jsonplaceholder.typicode.com"
    )
    response=request.get("/users/1")
    print(response.json())
    # print(response.text())