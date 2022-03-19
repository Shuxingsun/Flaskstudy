# -*- coding: utf-8 -*-
from flask import Flask,redirect,url_for
from werkzeug.routing import BaseConverter
app = Flask(__name__)

class MobileConverte(BaseConverter):
    def __init__(self,url_map):
        # 调用父类的初始化方法
        super(MobileConverte, self).__init__(url_map)
        self.regex = r'1[345678]\d{9}'

    # 其实to_python这个方法才是转换器的核心，
    # 当我们转换器提取到路径上面的参数后，
    # 不是直接返回给视图函数中的参数，
    # 而是要经过to_python方法才返回给视图函数

    def to_python(self, value):
        return '13341'

    def to_url(self, value):
        return '1323421'


# 2. 将自定义的转换器添加到flask的应用中
app.url_map.converters["mobile"] = MobileConverte
# http://127.0.0.1:5000/send_sms/18922313122/
@app.route('/send_sms/<mobile:moblie_num>/')
def send_sms(moblie_num):
    return "send_sms: %s" % moblie_num

@app.route("/index")
def index():
    url = url_for("send_sms", moblie_num="18922313122")
    return redirect(url)
if __name__ == '__main__':
    print(app.url_map)
    # 启动flask程序
    app.run(debug=True)