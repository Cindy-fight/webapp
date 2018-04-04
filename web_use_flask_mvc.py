from flask import Flask, request, render_template
from config import Config
from models.extend.Users import Users
from libraries.Util import Util
from libraries.Constant import Constant
import re

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/sign', methods=['GET'])
def sign_from():
    return render_template('form.html')

@app.route('/sign', methods=['POST'])
def sign():
    username = request.form['username']
    password = request.form['password']
    if (len(username) <= 0 or len(password) <= 0):
        return render_template('form.html', message=Constant.IS_EMPTY, username=username)

    password = Util.md5(password)

    userModel = Config.session.query(Users).filter(Users.email == username and Users.passwd == password).one()
    if(userModel):
        return render_template('sign_ok.html', username=username)
    return render_template('form.html', message = 'Bad username or password', username=username)

@app.route('/test', methods=['GET'])
def test():
    return render_template('test.html')

@app.route('/register', methods=['GET'])
def register_form():
    return render_template('register.html')


@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    nickname = request.form['nickname']

    if(len(username) <= 0 or len(password) <= 0 or len(nickname) <= 0):
        return render_template("register.html", message=Constant.IS_NONE)

    password = Util.md5(password)

    if(re.match(r'^1[3578]\d{9}$', username) or re.match(r'^[a-zA-Z0-9]{3,15}@[a-zA-Z0-8]{2,6}\.[a-zA-Z]{2,4}$', username)):
        username = username
    else:
        return render_template("register.html", message=Constant.IS_ERROR_USER)

    user = Config.session.query(Users).filter(Users.email == username).count()
    if (user):
        return render_template("register.html", message = Constant.ALREADY_REGISTER)
    else:
        UserModel = Users()
        UserModel.email = username
        UserModel.passwd = password
        UserModel.admin = 1
        UserModel.name = nickname
        UserModel.image = '123.jpg'
        UserModel.created_at = Util.get_now_time()

        try:
            Config.session.add(UserModel)
            Config.session.commit()
            return render_template("form.html", username=username)
            # out = {
            #     'resultCode': Constant.RESULT_CODE_SUCCESS,
            #     'msg': Constant.RESULT_MSG_SUCCESS
            # }
        except Exception as e:
            Config.session.rollback()
            out = {
                'resultCode': Constant.RESULT_CODE_FAIL,
                'msg': Constant.RESULT_MSG_FAIL,
                'ERR': e
            }
            return Util.json_out(out)

if __name__ == '__main__':
    app.run()