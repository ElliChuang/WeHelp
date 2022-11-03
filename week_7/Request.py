from flask import Flask # 載入 Flask
from flask import request # 載入 Request 物件
from flask import redirect # 載入 redirect 函式
from flask import render_template # 載入 render_template 函式
from flask import session # 載入 sesstion 函式
from flask import url_for # 載入 url_for 函式
import mysql.connector # 載入 mysql
from mysql.connector import pooling 
import json

# 使用connection pool
dbconfig = {
    "user" : "root",
    "password" : "",
    "host" : "localhost",
    "database" : "website",
}
# create connection pool
connection_pool = mysql.connector.pooling.MySQLConnectionPool(
    pool_name = "wehelp_pool",
    pool_size = 5,
    pool_reset_session = True,
    **dbconfig
)

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
    try:
        # get connection object from a pool
        connection_object = connection_pool.get_connection()
        mycursor = connection_object.cursor()
        account_name = request.form["account_name"]
        secret_code = request.form["secret_code"]
        query_username = ("SELECT username,password FROM member where username = %s")
        mycursor.execute(query_username, (account_name,))
        result = mycursor.fetchone()
        if account_name == "" or secret_code == "":
            session.pop("username", None)
            return redirect(url_for("error", message = "請輸入帳號、密碼"))
        elif not result: # 如果 result 沒值
            session.pop("username", None)
            return redirect(url_for("error", message = "帳號、或密碼輸入錯誤"))
        elif account_name == result[0] and secret_code == result[1]:
            session["username"] = account_name
            return redirect("/member")
        else:
            session.pop("username", None)
            return redirect(url_for("error", message = "帳號、或密碼輸入錯誤"))
    except:
        print("Unexcepted Error")
    finally:
        # close connection
        mycursor.close()
        connection_object.close()
        
# 使用 Post 方法，處理路徑 /signup 對應的函式
@app.route("/signup", methods=["POST"])
def signup():
    try:
        connection_object = connection_pool.get_connection()
        mycursor = connection_object.cursor()
        name = request.form["name"]
        account_name = request.form["account_name"]
        secret_code = request.form["secret_code"]
        sel_query = ("SELECT username FROM member where username = %s")
        mycursor.execute(sel_query, (account_name,))
        result = mycursor.fetchone()
        if name == "" or account_name == "" or secret_code == "":
            return redirect(url_for("error", message = "請輸入姓名、帳號及密碼"))
        elif result:  # 如果 result 有值
            return redirect(url_for("error", message = "帳號已經被註冊"))
        else: 
            query = "INSERT INTO member (name, username, password) VALUES (%s, %s, %s)"
            value = (name, account_name, secret_code)
            mycursor.execute(query, value)
            connection_object.commit() # Commit the changes
            return render_template("signup.html", data = name)
    except:
        print("Unexcepted Error")
    finally:
        mycursor.close()
        connection_object.close()

# 建立路徑 /member 對應的處理函式
@app.route("/member")
def member():
    try:
        if "username" in session:
            connection_object = connection_pool.get_connection()
            mycursor =  connection_object.cursor()
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
    except:
        print("Unexcepted Error")
    finally:
        mycursor.close()
        connection_object.close()

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
@app.route("/square/<int:num>/")
def square(num):
    ans = num**2   
    return render_template("square.html", data = ans)

# 建立路徑 /message 對應的處理函式
@app.route("/message", methods=["POST"])
def message():
    try:
        if "username" in session:
            connection_object = connection_pool.get_connection()
            mycursor =  connection_object.cursor()
            # 取的欄位 member_id 的資料
            select_id = ("SELECT id FROM member where username = %s")
            value_id = session["username"]
            mycursor.execute(select_id, (value_id,))
            id = mycursor.fetchone()
            # 取得欄位 content 的資料
            message = request.form["message"]
            # 把 member_id 及 content 寫入 message
            insert_query = "INSERT INTO message(member_id, content) VALUES (%s, %s)"
            insert_value = (id[0] ,message)
            mycursor.execute(insert_query, insert_value)
            connection_object.commit()
            return redirect("/member")
        else:
            return redirect("/")
    except:
        print("Unexcepted Error")
    finally:
        mycursor.close()
        connection_object.close()

# 建立路徑 /api/member 對應的處理函式
@app.route("/api/member",methods=["GET","PATCH"])
def api_member():
    try:
        # 查詢會員姓名
        if request.method == "GET":
            if "username" in session:
                username = request.args.get("username")
                connection_object = connection_pool.get_connection()
                mycursor = connection_object.cursor()
                query = ("SELECT id, name FROM member where username = %s")
                mycursor.execute(query, (username,))
                value = mycursor.fetchone()
                if value : 
                    return json.dumps({
                        "id" : value[0],
                        "name" : value[1],
                        "username" : username,                
                    }, ensure_ascii=False)
                else:
                    return json.dumps({
                        "data" : None             
                    })
            else:
                return json.dumps({
                        "data" : None             
                    }) 

        # 更新會員姓名 
        elif request.method == "PATCH":
            if "username" in session:
                newName = request.args.get("newName")
                connection_object = connection_pool.get_connection()
                mycursor = connection_object.cursor()
                query = ("UPDATE member SET name = %s WHERE username = %s")
                value = (newName, session["username"])
                mycursor.execute(query, value)
                connection_object.commit()
                return json.dumps({
                    "ok" : True             
                })
            else:
                return json.dumps({
                    "error" : True             
                })          
    except:
        print("Unexcepted Error")
    finally:
        mycursor.close()
        connection_object.close()


# 啟動網站伺服器
app.run(port = 3000) 



    
