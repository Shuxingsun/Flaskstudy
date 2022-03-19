from app import app
@app.route('/user/index')
def index():
     return 'user_index'

@app.route('/user/show')
def show():
     return 'user_show'

@app.route('/user/add')
def add():
    return 'user_add'

@app.route('/admin/index')
def adminindex():
     return 'admin_index'

@app.route('/admin/show')
def adminshow():
    return 'admin_show'

@app.route('/admin/add')
def adminadd():
     return 'admin_add'