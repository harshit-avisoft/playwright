from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    request=p.request.new_context(
        extra_http_headers={
            "Authorization":"Bearer 12345"
        }
    )
    response=request.get("https://example.com/api/me")
    # print(response.status)         # show the HTTP status code
    # print(response.json())         # parse and print JSON body (if it's JSON)
    # assert response.status == 200  # fail the test if not 200


    print(response.status)

    if response.status == 200:
        print(response.json())
    else:
        print("Not JSON, because API returned:", response.status)
        print(response.text())
