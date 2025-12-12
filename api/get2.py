from playwright.sync_api import sync_playwright

def test_simple_get():
    with sync_playwright() as p:
        request=p.request.new_context()
        response=request.get("https://jsonplaceholder.typicode.com/todos/1")

        assert response.status==200
        json_data=response.json()

        assert json_data["id"]==1
        assert json_data["completed"] is False