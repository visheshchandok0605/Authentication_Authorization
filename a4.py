import time
import json

def simulate_sso():
    print("--- Mock SSO Flow: Authorization Code Exchange ---")

    # 1. Simulate Redirect to Identity Provider (IdP)
    print("\n[Step 1] Redirecting to Identity Provider...")
    time.sleep(1)
    
    # 2. Simulate IdP Login
    print("\n[Step 2] Identity Provider Login")
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    
    # In a real flow, the IdP validates credentials here
    print(f"Logging in as {username}...")
    time.sleep(1)
    
    # Generate a mock Authorization Code
    auth_code = "XYZ123_TEMP_CODE"
    print(f"Login Successful! Auth Code generated: {auth_code}")

    # 3. Simulate Token Exchange
    print("\n[Step 3] Token Exchange")
    entered_code = input("Enter the Auth Code to exchange for tokens: ").strip()
    
    if entered_code == auth_code:
        # Mocking the JWT structure: header.payload.signature
        id_token = f"eyJhbGci.sub_{username}_claims.signature"
        access_token = "access_token_xyz_987"
        
        tokens = {
            "id_token": id_token,
            "access_token": access_token,
            "expires_in": 3600
        }
        print("\nTokens received from IdP:")
        print(json.dumps(tokens, indent=2))
    else:
        print("Invalid Auth Code. Exchange failed.")
        return

    # 4. Simulate Token Verification
    print("\n[Step 4] Token Verification")
    verify_token = tokens["id_token"]
    
    # Simple logic checks
    is_not_empty = len(verify_token) > 0
    has_valid_structure = len(verify_token.split('.')) == 3
    contains_user = username in verify_token

    if is_not_empty and has_valid_structure and contains_user:
        print("Status: Token Verified ✅")
        print(f"Welcome, {username}! Your session is now active.")
    else:
        print("Status: Invalid Token ❌")

if __name__ == "__main__":
    simulate_sso()