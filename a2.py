import jwt
from datetime import datetime, timedelta

# Secret key (keep this safe in real applications)
SECRET_KEY = "my_super_secret_key"
ALGORITHM = "HS256"

# --------------------------------------------------
# Generate JWT
# --------------------------------------------------
def generate_token(user_id):
    payload = {
        "sub": user_id,
        "role": "user",
        "exp": datetime.utcnow() + timedelta(minutes=5)  # Token expires in 5 minutes
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token


# --------------------------------------------------
# Validate JWT
# --------------------------------------------------
def validate_token(token):
    try:
        decoded_payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        print("Token Valid")
        print("Claims:", decoded_payload)

    except jwt.ExpiredSignatureError:
        print("Token Invalid: Token has expired")

    except jwt.InvalidTokenError:
        print("Token Invalid")


# --------------------------------------------------
# Main Execution
# --------------------------------------------------
if __name__ == "__main__":
    # Generate token
    user_id = "12345"
    token = generate_token(user_id)

    print("Generated JWT:")
    print(token)
    print("-" * 50)

    # Validate token
    print("Validating Token...")
    validate_token(token)
