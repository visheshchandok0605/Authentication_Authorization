def main():
    # 1. Setup the in-memory data
    documents = [
        {"id": 1, "owner": "userA", "content": "A's secret: I actually like decaf coffee."},
        {"id": 2, "owner": "userB", "content": "B's secret: I haven't washed my car in a year."},
        {"id": 3, "owner": "userC", "content": "C's secret: I know how to exit Vim."}
    ]

    # 2. Information Gathering
    print("--- Secure Document Portal ---")
    username = input("Enter your username: ").strip()
    
    try:
        doc_id_input = input("Enter the Document ID you want to access: ").strip()
        target_id = int(doc_id_input)
    except ValueError:
        print("Invalid input. ID must be a number.")
        return

    # 3. Fetching and Authorization Logic
    # Find the document by ID
    doc = next((d for d in documents if d["id"] == target_id), None)

    if doc:
        # Check if user is the owner OR is an admin
        if doc["owner"] == username or username == "admin":
            print(f"\n[ACCESS GRANTED]")
            print(f"Content: {doc['content']}")
        else:
            print("\n[ACCESS DENIED]")
    else:
        print("\n[ERROR] Document not found.")

if __name__ == "__main__":
    main()