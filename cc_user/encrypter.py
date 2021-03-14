from passlib.context import CryptContext

pwd_context = CryptContext(
        schemes=["pbkdf2_sha256"],
        default="pbkdf2_sha256",
        pbkdf2_sha256__default_rounds=30000
)

def encrypt(password):
    """
        This function encrypts strings.
        :param password: input string.
        :return : encrypted string.
    """
    return pwd_context.hash(password)


def verify_encryption(password, hashed):
    """
        This function checks if an input string is the same as an encrypted hash string.
        :return True/False: True if passed, False if not.
    """
    return pwd_context.verify(password, hashed)