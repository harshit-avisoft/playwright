from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    request=p.request.new_context()
    updated_data={
        "id":1,
        "title":"Updated Title",
        "body":"Updated Body",
        "userId":1
    }
    response=request.put(
        "https://jsonplaceholder.typicode.com/posts/1",
        data=updated_data
    )
    print("Status:",response.status)
    print("Updated:", response.json())