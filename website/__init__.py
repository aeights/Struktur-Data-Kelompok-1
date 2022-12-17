from flask import Flask,render_template,request,redirect,url_for,Blueprint
from Project import *
app = Flask(__name__)
# views = Blueprint('views', __name__)

@app.route("/home", methods=['GET', 'POST'])
def hello_world():
    if request.method == "POST":
        a = request.form.get("username")
        print(a)
        daftar(a,a)
        show_account()
    return render_template("main.html")