from flask import Flask
import binascii
import os

app = Flask(__name__)

if __name__ == '__main__':
    # This secret key is used by the session so the user can't edit the cookie
    app.secret_key = binascii.hexlify(os.urandom(24))
    app.run()