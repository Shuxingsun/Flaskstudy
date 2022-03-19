
# -*- coding: utf-8 -*-
from flask import Flask,request

app = Flask(__name__)

# @app.route("/post", methods=["GET","POST"])
# def post():
#     name = request.form.get("name")
#     age = request.form.get("age")
#     datas = request.data
#     print(datas)
#     return "hello name=%s age=%s" % (name, age)

@app.route("/post",methods=["GET","POST"])
def post():
    city = request.args.get("city")
    print(request.data)
    return  "hello city = %s"%(city)

#上传文件
# @app.route("/upload",methods=["GET","POST"])
# def upload():
#     f = request.files.get("pic")
#     if f is None:
#         return "No Files"
    # #创建一个文件
    # f1 = open('./text1.png','wb')
    # #向文件写内容
    # data = f.read()
    # f1.write(data)
    # f1.close()
    # return "upload success"

    # 直接使用上传的文件对象保存
    # f.save("./demo1.png")
    # return "上传成功"

if __name__ == '__main__':
    app.run(debug=True)