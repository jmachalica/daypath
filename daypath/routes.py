from flask import render_template,url_for, flash,redirect,request,jsonify
from daypath import app,db,bcrypt
from daypath.forms import RegistrationForm,LoginForm, UpdateAccountForm,UpdateTimerSettings
from daypath.models import User,Timer,Task
import math
from flask_login import login_user,current_user,logout_user,login_required

@app.route('/')
@app.route('/home')
def home():
    if current_user.is_authenticated:
        todo_tasks=Task.query.filter_by(user=current_user).filter_by(task_type='todo').all()
        done_tasks=Task.query.filter_by(user=current_user).filter_by(task_type='done').all()
        doing_tasks=Task.query.filter_by(user=current_user).filter_by(task_type='doing').all()
        return render_template('home.html',todo_tasks=todo_tasks,done_tasks=done_tasks,doing_tasks=doing_tasks)
    else:
        return redirect(url_for('about'))




@app.route('/about')
def about():
    return render_template('about.html',title='DayPath - About')

@app.route('/home/add')
@login_required
def add_task():
    content=request.args.get('content',0,type=str)
    task_type=request.args.get('task_type',0,type=str)
    task=Task(user=current_user,task_content=content,task_type=task_type)
    db.session.add(task)
    db.session.commit()

    return jsonify(task_id=task.id)

  
@app.route('/home/del')
@login_required
def del_task():
    id=request.args.get('task_id',0,type=int)
    Task.query.filter_by(id=id).delete()
    db.session.commit()
    return jsonify()


@app.route('/home/move')
@login_required
def move_task():
    id=request.args.get('task_id',0,type=int)
    task_type=request.args.get('task_type',0,type=str)
    task=db.session.query(Task).filter_by(id=id).first()
    task.task_type=task_type
    db.session.commit()
    return jsonify()

@app.route('/home/update')
@login_required
def update_task():
    id=request.args.get('task_id',0,type=int)
    task_content=request.args.get('task_content',0,type=str)
    task=db.session.query(Task).filter_by(id=id).first()
    task.task_content=task_content
    db.session.commit()
    return jsonify()


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        add_user=User(username=form.username.data,email=form.email.data,password=hashed_password)
        db.session.add(add_user)
        db.session.commit()        
        timer=Timer(user=add_user)
        db.session.add(timer)
        db.session.commit()

        return redirect(url_for('login'))
    return render_template('register.html', title='DayPath - Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            
            login_user(user,remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check your email and password.','danger')

    return render_template('login.html', title='DayPath - Log in', form=form)

@app.route("/logout")
def logout():    
    logout_user()
    return redirect(url_for('home'))


@app.route("/account")
@login_required
def account():

    form =UpdateAccountForm()
    if form.validate_on_submit():
        current_user.username=form.username.data
        current_user.email=form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method=='GET':
        form.email.data=current_user.email
        form.username.data=current_user.username


    return render_template('account.html', title='DayPath - Account',form=form)



@app.route("/pomotimer",methods=['GET','POST'])
@login_required
def pomotimer():
    form=UpdateTimerSettings()

    if form.validate_on_submit():
        current_user.timer[0].work_time=int(form.work_time.data*60)
        current_user.timer[0].break_time=int(form.short_break.data*60)
        current_user.timer[0].long_break_time=int(form.long_break.data*60)
        db.session.commit()
        return redirect(url_for('pomotimer')) 
    elif request.method=='GET':
        form.work_time.data= math.floor(current_user.timer[0].work_time/60) 
        form.short_break.data=math.floor(current_user.timer[0].break_time/60)
        form.long_break.data=math.floor(current_user.timer[0].long_break_time/60)

    time=current_user.timer[0]
    return render_template('pomotimer.html', title='DayPath - Pomodoro Timer',time=time,form=form)

@app.route("/pomotimer.js")
def pomotimer_js():
    return render_template('pomotimer.js',time=current_user.timer[0])

@app.route("/home.js")
def home_js():
    return render_template('home.js')

@app.route("/home_drag.js")
def home_drag_js():
    return render_template('home_drag.js')