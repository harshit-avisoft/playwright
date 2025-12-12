from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    request = p.request.new_context()

    response = request.delete(
        "https://jsonplaceholder.typicode.com/posts/1"
    )

    print("Status:", response.status)
