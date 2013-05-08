from flask import Flask
from flask import request
from flask import render_template
from flask import url_for,redirect,flash


app = Flask(__name__)
app.secret_key = "secret"
@app.route("/",methods=['GET','POST'])
def main():
    if request.method=="GET":
        return render_template('Homepage.html')
@app.route("/create.js",methods=['GET','POST'])
def create():
    if request.method == "GET":
        return render_template('./create.js')
if __name__=="__main__":
    app.debug=True
    app.run(host="0.0.0.0",port=8000)
