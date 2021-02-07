from passlib.context import CryptContext

pwd_context = CryptContext(
    schemes = ["pbkd_sha256"],
    default = "pbkd_sha256",
    pbkdf2_sha256__default_rounds = 30000
)

def encrypt_password(password):
    return pwd_context.encrypt(password)

def verify_passwords(password, hashed):
    return pwd_context.verify(password, hashed)
