import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello, World!'

#Ex https://Itz-zaid:ghp_147bkkabcdefgh@github.com/Itz-zaid/anything
os.system("git clone https://github.com/Dkmovie/DK_Movie_filterv2 okk && cd okk && pip3 install -U -r requirements.txt && nohup python3 -m telegram &")
