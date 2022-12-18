from flask import Flask,render_template,request,redirect,url_for,Blueprint
from Project import *
app = Flask(__name__)
# views = Blueprint('views', __name__)

@app.route("/home", methods=['GET', 'POST'])
def daftar_user():
    if request.method == "POST":
        if request.form.get("u_daftar") and request.form.get("p_daftar"):
            user = request.form.get("u_daftar")
            pw = request.form.get("p_daftar")
            daftar(user,pw)
            show_account()

        elif request.form.get("u_login") and request.form.get("p_login"):
            user = request.form.get("u_login")
            pw = request.form.get("p_login")
            if login(user,pw) == True:
                print("berhasil")
    return render_template("main.html")