from flask import Flask # 載入 Flask
from flask import request # 載入 Request 物件
from flask import redirect # 載入 redirect 函式
from flask import render_template # 載入 render_template 函式
from flask import session # 載入 sesstion 函式
from flask import url_for # 載入 url_for 函式
# 建立 Application 物件
app = Flask(__name__) 

# session secret key
app.secret_key = "banana"

# 建立首頁路徑 / 對應的處理函式
@app.route("/") 
def home():
    return  render_template("home.html")

# 使用 Post 方法，處理路徑 /signin 對應的函式
@app.route("/signin", methods=["POST"])
def signin():
    account_name = request.form["account_name"]
    secret_code = request.form["secret_code"]
    if account_name == "test" and secret_code == "test":
        session["username"] = account_name
        return redirect("/member")
    elif account_name == "" or secret_code == "":
        session.pop("username", None)
        return redirect(url_for("error", message = "請輸入帳號、密碼"))
    else:
        session.pop("username", None)
        return redirect(url_for("error", message = "帳號、或密碼輸入錯誤"))

# 建立路徑 /member 對應的處理函式
@app.route("/member")
def member():
    if "username" in session:
        return render_template("member.html")
    else:
        return redirect("/")

# 建立路徑 /error 對應的處理函式
@app.route("/error")
def error():
    notes = request.args.get("message")
    return render_template("error.html", data = notes)

# 建立路徑 /signout 對應的處理函式
@app.route("/signout")
def signout():
    session.pop("username", None)
    return redirect("/")
    
@app.route("/square/<int:num>")
def square(num):
    ans = num**2   
    return render_template("square.html", data = ans)


# 啟動網站伺服器
app.run(port = 3000) 
