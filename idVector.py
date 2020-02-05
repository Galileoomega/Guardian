import base64, os, json, style
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# GET current path
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
usernamePath = os.path.join(THIS_FOLDER, 'bin\\fileY.json')
passwordPath = os.path.join(THIS_FOLDER, 'bin\\fileZ.json')

def confirmationLogin(userPassword, iPressedMyLoginButton):

    if iPressedMyLoginButton:

        password_provided = str(userPassword) # This is input in the form of a string
        password = password_provided.encode() # Convert to type bytes
        salt = b'\xa8V\xbbc\xad\x131K\x04{\xd4\x07Bz\xe6\xa4'
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        key = base64.urlsafe_b64encode(kdf.derive(password)) # Can only use kdf once
        key = key.decode()

        with open(passwordPath) as f:
            data = json.load(f)

        extractedPassword = data["password"]

        extractedPassword = str(extractedPassword)

        finalPassword = extractedPassword[2:-2]

        if finalPassword == key:
            loginIsOk = True
            wrongPass = False
        else:
            loginIsOk = False
            wrongPass = True            

        return loginIsOk, wrongPass
    