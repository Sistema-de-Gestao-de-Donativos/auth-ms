# validar o token do google
# ler o useer do ms de users
# injetar nivel de perrmissao na claim do jwt com par de chaves publuca e privada e retornar

Sure! Below is a Python function that performs the following:

1. **Validates the Google auth token** with Google to retrieve the user's email.
2. **Determines the user's permission level** (either 'admin' or 'voluntario').
3. **Creates a JWT claim** that includes the user's email and permission level.
4. **Signs the JWT** using a private key.
5. **Returns the signed JWT token**.

```python
from google.oauth2 import id_token
from google.auth.transport import requests
import jwt
import datetime

def get_permission_level(email):
    """
    Placeholder function to determine the user's permission level based on their email.
    You can replace this with your actual implementation.
    """
    # Example logic: Emails ending with '@admin.com' are admins
    if email.endswith('@admin.com'):
        return 'admin'
    else:
        return 'voluntario'

def create_jwt_token(email, permission_level, private_key):
    """
    Creates a JWT token with the given email and permission level, signed with the provided private key.
    """
    payload = {
        'email': email,
        'permission_level': permission_level,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # Token expires in 1 hour
    }
    token = jwt.encode(payload, private_key, algorithm='RS256')
    return token

def generate_jwt_from_google_token(google_token):
    try:
        # Replace 'YOUR_CLIENT_ID' with your actual Google OAuth2 client ID
        CLIENT_ID = 'YOUR_CLIENT_ID.apps.googleusercontent.com'
        
        # Validate the Google auth token
        id_info = id_token.verify_oauth2_token(google_token, requests.Request(), CLIENT_ID)
        email = id_info.get('email')
        
        if not email:
            return {'error': 'Unable to retrieve email from Google token'}
        
        # Determine the user's permission level
        permission_level = get_permission_level(email)
        
        # Load your private key (ensure this is stored securely)
        private_key = """-----BEGIN RSA PRIVATE KEY-----
... Your Private Key Here ...
-----END RSA PRIVATE KEY-----"""
        
        # Create the JWT token
        jwt_token = create_jwt_token(email, permission_level, private_key)
        
        return jwt_token

    except ValueError:
        # Invalid token
        return {'error': 'Invalid Google token'}

# Example usage:
# google_auth_token = '...token from client...'
# jwt_token = generate_jwt_from_google_token(google_auth_token)
# print(jwt_token)
```

**Explanation:**

- **Google Token Validation:** The function `generate_jwt_from_google_token` validates the provided Google auth token using `google.oauth2.id_token.verify_oauth2_token`. This ensures the token is valid and retrieves the user's email.

- **Permission Level:** The function `get_permission_level` determines whether the user is an 'admin' or 'voluntario' based on the email. You can implement your own logic here.

- **JWT Creation:** The function `create_jwt_token` creates a JWT that includes the user's email and permission level. It sets an expiration time (`exp`) and signs the token using an RSA private key.

- **Private Key:** Replace the `private_key` content with your actual RSA private key. Make sure to keep your private key secure and not hard-coded in the source code. Consider using environment variables or a secure key management system.

**Dependencies:**

Make sure you have the required packages installed:

```bash
pip install google-auth
pip install pyjwt
```

**Important Notes:**

- **CLIENT_ID:** Replace `'YOUR_CLIENT_ID.apps.googleusercontent.com'` with your actual Google OAuth2 client ID. This ensures that the token is validated correctly and is intended for your application.

- **Security Considerations:**
  - **Private Key Management:** Store your private key securely. Do not expose it in your source code or version control systems.
  - **Token Expiration:** The JWT includes an expiration time (`'exp'`) to enhance security. You can adjust the duration as needed.
  - **HTTPS:** Always transmit tokens over secure channels (HTTPS) to prevent interception.

- **Error Handling:** The function returns an error message if the token is invalid or the email cannot be retrieved. You can enhance error handling based on your application's needs.

**Replace Placeholder Values:**

- **Private Key:** Replace the `private_key` block with your actual RSA private key.
- **CLIENT_ID:** Replace `'YOUR_CLIENT_ID.apps.googleusercontent.com'` with your Google OAuth2 client ID.

**Testing the Function:**

To test the function, you can call it with a valid Google auth token:

```python
google_auth_token = '...token from client...'
jwt_token = generate_jwt_from_google_token(google_auth_token)
print(jwt_token)
```

---

This function provides a secure way to authenticate users with Google, assign permission levels, and issue JWT tokens for access control in your application.