from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_modus import Modus

app = Flask(__name__)
modus = Modus(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/user_message' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# import a blueprint that we will create
from project.users.views import users_blueprint
from project.messages.views import messages_blueprint

# register our blueprints with the application
app.register_blueprint(users_blueprint, url_prefix='/employees')
app.register_blueprint(messages_blueprint, url_prefix='/departments')

@app.route('/')
def root():
    return "HELLO FROM USER-MESSAGES APP!"