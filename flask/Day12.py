
from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
#配置邮件：服务器／端口／传输层安全协议／邮箱名／密码
app.config.update(
    DEBUG = True,
    MAIL_SERVER='smtp.qq.com',
    MAIL_PROT=465,
    MAIL_USE_TLS = True,
    MAIL_USERNAME = '2995298638@qq.com',
    MAIL_PASSWORD = 'qhjduynjormtddha',
)

mail = Mail(app)

@app.route('/')
def index():
 # sender 发送方，recipients 接收方列表
    msg = Message("This is a test ",sender='2995298638@qq.com', recipients='1569306032@qq.com')
    #邮件内容
    msg.body = "Flask test mail"
    #发送邮件
    mail.send(msg)
    print("Mail sent")
    return "Sent　Succeed"

if __name__ == "__main__":
    app.run()