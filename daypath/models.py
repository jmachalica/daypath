from daypath import db,login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(20),unique=True,nullable=False)
    email=db.Column(db.String(100),unique=True,nullable=False)
    image_file=db.Column(db.String(20),nullable=False,default='default.jpg')
    password=db.Column(db.String(60),nullable=False)
    timer=db.relationship('Timer',backref='user',lazy=True)
    tasks=db.relationship('Task',backref='user',lazy=True)
    def __repr__(self):
        return f"User('{self.id}','{self.username}','{self.email}','{self.image_file}') "


class Timer(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    work_time=db.Column(db.Integer,nullable=False,default=1800)
    break_time=db.Column(db.Integer,nullable=False,default=300)
    long_break_time=db.Column(db.Integer,nullable=False,default=900)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)

    def __repr__(self):
        return f"Timer('{self.id}','{self.work_time}','{self.break_time}','{self.long_break_time}') "

class Task(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    task_type=db.Column(db.String(40),nullable=False,default='todo')
    task_content=db.Column(db.String(200),nullable=False)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
    
    def __repr__(self):
        return f"Task('{self.id}','{self.task_content}','{self.task_type}') "