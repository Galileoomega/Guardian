import base64, os, json, style, secrets, re
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# GET current path
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
usernamePath = os.path.join(THIS_FOLDER, 'bin\\fileY.json')
passwordPath = os.path.join(THIS_FOLDER, 'bin\\fileZ.json')

def confirmationLogin(userPassword, iPressedMyLoginButton, userUsername):

    if iPressedMyLoginButton:

        # -----------------CHECK IF USER EXIST-----------------
        with open(usernamePath) as f:
            data1 = json.load(f)
        
        extractedUsername = data1["user"]
        r = re.compile(userUsername)
        newlist = list(filter(r.search, extractedUsername)) # Read Note
        
        if len(newlist) == 1:
            # If the user exist: Extract the ID (index)
            print(newlist)
            userExist = True
            masterIndex = extractedUsername.index(newlist[0])
        else:
            newlist = []
            userExist = False
        # ----------------------------------------------------

        if userExist:
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

            print(key)

            with open(passwordPath) as f:
                data2 = json.load(f)

            extractedPassword = data2["password"]
            try:
                print(extractedPassword)
                print("MASTER INDEX : ", masterIndex)
                extractedPassword = extractedPassword[masterIndex]
                print(extractedPassword)
            except TypeError:
                extractedPassword = extractedPassword[1]

            finalPassword = str(extractedPassword)

            if secrets.compare_digest(finalPassword, key):
                loginIsOk = True
                wrongPass = False
            else:
                loginIsOk = False
                wrongPass = True    
        else:
            loginIsOk = False
            wrongPass = True        

        return loginIsOk, wrongPass
    