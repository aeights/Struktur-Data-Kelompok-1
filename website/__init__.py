from flask import Flask,render_template,request,redirect,url_for,Blueprint
from Project import *

app = Flask(__name__)
# views = Blueprint('views', __name__)

@app.route("/daftar", methods=['GET', 'POST'])
def daftar_user():
    if request.method == "POST":
        if request.form.get("u_daftar") and request.form.get("p_daftar"):
            user = request.form.get("u_daftar")
            pw = request.form.get("p_daftar")
            daftar(user,pw)
            show_account()
    return render_template("daftar.html")

@app.route("/login", methods=['GET', 'POST'])
def login_user():
    if request.method == "POST":
        if request.form.get("u_login") and request.form.get("p_login"):
            user = request.form.get("u_login")
            pw = request.form.get("p_login")
            if login(user,pw) == True:
                return redirect(url_for("home"))
    return render_template("login.html")

@app.route("/hapus", methods=['GET', 'POST'])
def hapus_akun():
    if request.method == "POST":
        if request.form.get("u_hapus") and request.form.get("p_hapus"):
            user = request.form.get("u_hapus")
            pw = request.form.get("p_hapus")
            if hapus(user,pw) == True:
                return redirect(url_for("login_user"))
    return render_template("hapus.html")

@app.route("/edit", methods=['GET', 'POST'])
def edit_akun():
    if request.method == "POST":
        pass
    return render_template("home.html")

@app.route("/home", methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        print("sukses")
    return render_template("home.html")