from flask import Flask,make_response,request,session

app = Flask(__name__)

# cookie的使用
# @app.route('/set_cookie')
# def set_cookie():
#     resp = make_response("success")
#
#     #设置cookie,设置有效期单位s
#     resp.set_cookie("ITcast","python",max_age=200)
#     resp.set_cookie('Itcast1','python1',max_age=200)
#     return resp
# #
# @app.route("/get_cookie")
# def get_cookie():
#     c = request.cookies.get("Itcast1")
#     return c
# #
# @app.route("/delete_cookie")
# def delete_cookie():
#     resp = make_response("del success")
#     resp.delete_cookie('Itcast1')
#     return resp

#session的运用
app.config['SECRET_KEY'] = '123scdinieroinds'

@app.route('/login')
def login():
    #设置session
    session["name"] = "python"
    session["mobile"] = "12112341231"

    return "login success"

@app.route("/index")
def index():
    #获取session数据
    name = session.get("name")
    mobile = session.get("mobile")
    return "hello %s %s"%(name,mobile)

if __name__ == '__main__':
    app.run(debug=True)
