import secrets

def generate_secret(length: int = 64) -> str:
    """Generates a secure secret key in hexadecimal"""
    return secrets.token_hex(length)

if __name__ == "__main__":
    generate_secret(64)
