from flask import Flask,abort,Response,make_response,jsonify

app = Flask(__name__)

#abort方法
# @app.route("/login")
# def login():
#     # 1.传递状态码信息（必须是http标准状态码）
#     name = ""
#     pwd = ""
#     # 如果name不等于123 pwd不等于1234 ，我们就返回404状态码
#     if name != "123" and pwd != "1234":
#         # 传递状态码信息（必须是http标准状态码）
#         # abort(404)
#
#         # abort函数还能传递响应体信息
#         resp = Response("login failed")
#         abort(resp)
#
#     return  "login success"

#2.自定义错误处理方法，自定义返回页面信息
# @app.errorhandler(404)
# def handle_404_error(err):
#     '''自定义404错误处理方法'''
#     # 返回值是用户在前端页面看到的结果
#     return u'很抱歉，出现404错误，错误信息：%s'%err

#3.设置响应信息方法
@app.route("/index")
def index():
    # 1. tuple
    # return ('index page',404,[('itcast','python'),('city','hi')])

    # 2.dic
    # return ("index page",400,{"itcast":"python","city":"wuh"})

    # make_response
    # resp = make_response("index page")
    # resp.status = "666"
    # resp.headers["qu"] = 'hn'
    # return resp

# 4.返回json数据
    # 1.
    data = {
        "name":"sdjhbcs",
        "age":21
    }
    2.
    return jsonify(name='assjdbhc',age=20)

if __name__ == '__main__':
    app.run(debug=True)
