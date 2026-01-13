import bcrypt
import random

# Simple in-memory storage (list of dictionaries)
user_db = []

def register():
    print("\n--- Register ---")
    username = input("Username: ")
    password = input("Password: ")

    # Generate a salt and hash the password
    # Note: bcrypt requires bytes, so we encode the string
    password_bytes = password.encode('utf-8')
    hashed_password = bcrypt.hashpw(password_bytes, bcrypt.gensalt())

    user_db.append({
        "username": username,
        "hashed_password": hashed_password
    })
    print("User registered successfully!")

def login():
    print("\n--- Login ---")
    username = input("Username: ")
    password = input("Password: ")

    # 1. Find the user in our "database"
    user = next((u for u in user_db if u['username'] == username), None)

    if user:
        # 2. Verify password
        password_bytes = password.encode('utf-8')
        if bcrypt.checkpw(password_bytes, user['hashed_password']):
            print("\n[System] Password verified.")
            
            # 3. Basic MFA Simulation
            otp = str(random.randint(100000, 999999))
            print(f"\n*** SMS SENT: Your 6-digit code is: {otp} ***\n")
            
            user_otp = input("Enter MFA OTP: ")
            
            if user_otp == otp:
                print(f"\n✅ Login Successful! Welcome, {username}")
            else:
                print("\n❌ Invalid MFA Code. Access Denied.")
        else:
            print("\n❌ Invalid Credentials.")
    else:
        print("\n❌ User not found.")

def main():
    # Simple flow: Register then attempt Login
    register()
    login()

if __name__ == "__main__":
    main()