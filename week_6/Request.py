from flask import Flask # 載入 Flask
from flask import request # 載入 Request 物件
from flask import redirect # 載入 redirect 函式
from flask import render_template # 載入 render_template 函式
from flask import session # 載入 sesstion 函式
from flask import url_for # 載入 url_for 函式
import mysql.connector # 載入 mysql
from mysql.connector import errorcode # 載入 mysql 錯誤處理

# 連線到 mysql
db = mysql.connector.connect(
    user = "root",
    password = "ThisisElliChuang0829",
    host = "localhost",
    database = "website",
    buffered = True
) # db 是物件

mycursor = db.cursor()

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
    value =[account_name] 
    query_username = ("SELECT username,password FROM member where username = %s")
    mycursor.execute(query_username, value)
    result = mycursor.fetchall()
    if account_name == "" or secret_code == "":
        session.pop("username", None)
        return redirect(url_for("error", message = "請輸入帳號、密碼"))
    else:
        if not result: # 如果 result 沒值
            session.pop("username", None)
            return redirect(url_for("error", message = "帳號、或密碼輸入錯誤"))
        elif account_name == result[0][0] and secret_code == result[0][1]:
            session["username"] = account_name
            return redirect("/member")
        else:
            session.pop("username", None)
            return redirect(url_for("error", message = "帳號、或密碼輸入錯誤"))

        
# 使用 Post 方法，處理路徑 /signup 對應的函式
@app.route("/signup", methods=["POST"])
def signup():
    name = request.form["name"]
    account_name = request.form["account_name"]
    secret_code = request.form["secret_code"]
    value =[] 
    value.append(account_name)
    sel_query = ("SELECT username FROM member where username = %s")
    mycursor.execute(sel_query, value)
    result = mycursor.fetchall()
    if result:  # 如果 result 有值
        return redirect(url_for("error", message = "帳號已經被註冊"))
    else:
        if name == "" or account_name == "" or secret_code == "":
            return redirect(url_for("error", message = "請輸入姓名、帳號及密碼"))
        else: 
            query = "INSERT INTO member (name, username, password) VALUES (%s, %s, %s)"
            value = (name, account_name, secret_code)
            mycursor.execute(query, value)
            db.commit() # Commit the changes
            return render_template("signup.html", data = name)
  
        

# 建立路徑 /member 對應的處理函式
@app.route("/member")
def member():
    if "username" in session:
        query = ("SELECT member.username,message.content FROM message inner join member on message.member_id = member.id")
        mycursor.execute(query)
        message = mycursor.fetchall()
        content = ""
        for i in message:
            content += i[0] + " : " + i[1] + "\n" 
        content = content.split("\n")
        return render_template("member.html",data_1 = session["username"], data_2 = content)
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

# 建立路徑 /square 對應的處理函式   
@app.route("/square/<int:num>")
def square(num):
    ans = num**2   
    return render_template("square.html", data = ans)

# 建立路徑 /message 對應的處理函式
@app.route("/message", methods=["POST"])
def message():
    # 取的欄位 member_id 的資料
    select_id = ("SELECT id FROM member where username = %s")
    value_id = [session["username"]]
    mycursor.execute(select_id, value_id)
    id = mycursor.fetchall()
    # 取得欄位 content 的資料
    message = request.form["message"]
    # 把 member_id 及 content 寫入 message
    insert_query = "INSERT INTO message(member_id, content) VALUES (%s, %s)"
    insert_value = (id[0][0] ,message)
    print(insert_value)
    mycursor.execute(insert_query, insert_value)
    db.commit()
    return redirect("/member")


# 啟動網站伺服器
app.run(port = 3000) 
