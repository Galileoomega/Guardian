import base64, os, json, style, secrets, re, cryptography
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet

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
        newList = extractedUsername.count(userUsername)
        
        if newList == 1:
            # If the user exist: Extract the ID (index)
            userExist = True
            masterIndex = extractedUsername.index(userUsername)
        else:
            userExist = False
            print("User don't exist")
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

            print("KEYYY: " + key)

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
    
def convertPassword(userPassword):

    passwordProvided = str(userPassword)
    password = passwordProvided.encode()
    salt = b'\x8a\x874\xe1\xb8+\x84O?\xbfR\xc9\x98\xa5L\xac'
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
         length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password)) # Can only use kdf once
    key = key.decode()
    
    return key

def encryptFiles(listOfPaths, userPassword):
    key = convertPassword(userPassword)
    
    for path in listOfPaths:

        outputFile = path
        outputFile += ".sha"
    
        with open(path, 'rb') as f:
            data = f.read()
        
        fernet = Fernet(key)
        encrypted = fernet.encrypt(data)

        with open(outputFile, 'wb') as f:
            f.write(encrypted)
        
        os.remove(path)

def decryptFiles(listOfPaths, userPassword):
    key = convertPassword(userPassword)
    
    for path in listOfPaths:

        outputFile = path
        outputFile = outputFile[:-3]
    
        with open(path, 'rb') as f:
            data = f.read()
        
        fernet = Fernet(key)
        try:
            encrypted = fernet.decrypt(data)
        except cryptography.fernet.InvalidToken:
            break

        with open(outputFile, 'wb') as f:
            f.write(encrypted)
        
        os.remove(path)