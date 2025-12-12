from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Create API request context
    request = p.request.new_context(
        base_url="https://jsonplaceholder.typicode.com"
    )

    print("=== STEP 1: GET original data ===")

    # GET the post with ID=1
    original_response = request.get("/posts/1")
    original_data = original_response.json()

    print("Status:", original_response.status)
    print("Original Data:", original_data)

    print("\n=== STEP 2: UPDATE the data using PUT ===")

    # Create updated data
    updated_payload = {
        "id": 1,
        "title": "Updated Title",
        "body": "This is the updated content!",
        "userId": 1
    }

    update_response = request.put("/posts/1", data=updated_payload)
    updated_data = update_response.json()

    print("Status:", update_response.status)
    print("Updated Data:", updated_data)

    print("\n=== STEP 3: GET data again after update ===")

    # GET it again to verify the update
    verify_response = request.get("/posts/1")
    verify_data = verify_response.json()

    print("Status:", verify_response.status)
    print("Data After Update:", verify_data)
