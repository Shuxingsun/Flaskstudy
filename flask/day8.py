from flask import Flask,request,url_for

app = Flask(__name__)

#上下文
# @app.route("/")
# def hello_world():#  在这里将request对象作为参数传进来
#     data = request.json
#     return "hello world"

# 请求钩子
@app.route('/hello')
def hello_world():
    return 'hello world'

@app.route('/index')
def index():
    return "hello index"

# 在第一次请求之前运行.
# 例子: 比如连接数据库操作, 只需要执行一次
@app.before_first_request
def before_first_request():
    # print('before_first_request')

    path = request.path
    if path == url_for("hello"):
        print("如果是hello视图函数就执行这个")
    elif path == url_for("index"):
        print("如果是index视图函数就执行这个")
    return ""

# 在每一次请求都会执行
# 例子: 可以在这里做权限校验操作，比如说某用户是黑名单用户，黑名单用户登录系统将遭到拒绝访问，可以使用
# before_request进行权限校验
@app.before_request
def before_request():
    print('before_request')

#请求之后运行
@app.after_request
def after_request(response):
    # response: 就是前面的请求处理完毕之后, 返回的响应数据
    # 如果需要对响应做额外处理,可以再这里进行
    # json.dumps 配置请求钩子
    # response.headers["Content-Type"] = "application/json"
    print('after_request')
    return response

# 每一次请求之后都会调用，会接受一个参数，参数是服务器出现的错误信息
@app.teardown_request
def teardown_request(error):
    # 数据库的扩展, 可以实现自动提交数据库
    print('teardown_request:error %s'%error)

if __name__ =="__main__":
    app.run(debug=True)


if __name__ == "__main__":
    app.run(debug=True)
