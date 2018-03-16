from project import db

class User(db.Model):
  
  __tablename__= "users"

  id = db.Column(db.Integer, primary_key=True)
  first_name = db.Column(db.Text)
  last_name = db.Column(db.Text)
  #Associating one model with another (User with Message-thats why its not plural!!)
  messages = db.relationship('Message', backref='user', lazy='dynamic', cascade="all,delete")
  #acces all messages of a user: user.messages 
  #acess a user by a spec messsage.user (one to many association)

  def __init__(self, first_name, last_name):
    self.first_name = first_name
    self.last_name = last_name