from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    request=p.request.new_context()

    data={
        "title":"My Post",
        "body":"Hello World",
        "userId":1
    }
    response=request.post(
        "https://jsonplaceholder.typicode.com/posts",
        data=data
    )

    print("Status:", response.status)
    print("Response JSON:", response.json())