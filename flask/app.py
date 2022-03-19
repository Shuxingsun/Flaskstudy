
from flask import Flask,redirect,url_for
from werkzeug.routing import BaseConverter

# import demo

#创建创建Flask的应用对象
app = Flask(__name__,static_url_path='/python')   # __name__ 就是当前模块的名字
# app.config.from_pyfile("config.py")       无用

# 装饰器，绑定视图函数的路径
# @app.route('/')
# def hello_world():
#     #视图函数
#     return 'Hello World!'

# if __name__ == '__main__':
#     # 运行本地服务器进行测试flask程序
#     app.run(host="127.0.0.1",port="5500")
# @app.route("/")
# def index():
#     return "hello flask"
#
#post请求方式
# @app.route("/post_only",methods=["POST"])
# def post_only():
#     return "POST"

# 不同视图函数相同装饰器,运行第一个视图函数
# @app.route("/hello")
# def hello1():
#     return "hello 1"
#
# @app.route("/hello")
# def hello2():
#     return "hello 2"

#装饰器不同，视图函数相同时，都可以
# @app.route("/hi1")
# @app.route("/hi2")
# def hi():
#     return "hi nihao"

#重定向
# @app.route("/hell")
# def hello1():
#     return "hello 1"
#
# @app.route("/login")
# def login():
#     #通过把视图函数的名称放进参数当中就可以找到视图函数所对应的url路径。
#     url = url_for('hello1')
#     return redirect(url)

# 路由参数，转换器
# @app.route('/goods/<int:goods_id>')

#不用转换器，普通字符串类型
# @app.route('/goods/<goods_id>')
# def goods(goods_id):
#     print(type(goods_id))
#     return "goods_id:%s"%goods_id

#自定义转换器
# 1.定义自己的转换器
# class RegexConverte(BaseConverter):
#     def __init__(self, url_map, regex):
#         # 调用父类的初始化方法
#         super(RegexConverte, self).__init__(url_map)
#         # 将正则表达式的参数保存在对象的属性中，flask会去使用这个属性来进行路由的正则匹配
#         self.regex = regex

# 2. 将自定义的转换器添加到flask的应用中
# app.url_map.converters["re"] = RegexConverte

# @app.route("/send/<re(r'1[345678]\d{9}'):moblie>")
# def send_sms(moblie):

#     return "send_sms: %s" % moblie

if __name__ == '__main__':

    #运行本都服务器测试flask程序
    map = app.url_map
    print(map)
    app.run(debug = True)
