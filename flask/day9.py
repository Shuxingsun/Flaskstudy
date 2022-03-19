# from flask import Flask,render_template
# app = Flask(__name__)
# #  模板变量
# @app.route('/index')
# def index():
#     # 键值对的形式来给模板变量赋值
#     # return render_template('index.html',name='kuls',age=20)
#     #dic
#     data = {
#         "name":"kuls",
#         "age":20,
#         "dict": {"city": "cs"},
#         "list": [0, 1, 2, 3],
#         "int": 1
#
#
#     }
#     return render_template('index.html',**data)
#
# if __name__ == '__main__':
#     app.run(debug=True)

#表单

#coding=utf-8
from flask import Flask,render_template, redirect,url_for,session,request,flash

#导入wtf扩展的表单类
from flask_wtf import FlaskForm
#导入自定义表单需要的字段
from wtforms import SubmitField,StringField,PasswordField
#导入wtf扩展提供的表单验证器
from wtforms.validators import DataRequired,EqualTo
app = Flask(__name__)
# 需要设置 SECRET_KEY 的配置参数
app.config['SECRET_KEY']='1'

#创建自定义表单类，文本字段、密码字段、提交按钮
class Login(FlaskForm):
    us = StringField(label=u'用户：',validators=[DataRequired()])
    ps = PasswordField(label=u'密码',validators=[DataRequired(),EqualTo('ps2','err')])
    ps2 = PasswordField(label=u'确认密码',validators=[DataRequired()])
    submit = SubmitField(u'提交')

#定义根路由视图函数，生成表单对象，获取表单数据，进行表单数据验证
@app.route('/',methods=['GET','POST'])
def index():
    # 创建一个Login对象
    form = Login()
    if form.validate_on_submit():
        # 调用Login对象当中的属性，并取其数值
        name = form.us.data
        pswd = form.ps.data
        pswd2 = form.ps2.data
        print(name,pswd,pswd2)
        # 重定向至login的装饰器
        return redirect(url_for('login'))
    else:
        if request.method=='POST':
            flash(u'信息有误，请重新输入！')

    return render_template('index.html',form=form)
if __name__ == '__main__':
    app.run(debug=True)