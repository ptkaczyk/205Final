from flask import render_template, Flask, flash, redirect, url_for, abort, request
from flask_login import login_user, logout_user, login_required
from werkzeug.urls import url_parse

from app import app, db
from app.models import *
from app.forms import *

@app.route('/landing')
def landing():
   return render_template('Landing.html',title='Landing')

@app.route('/login', methods=['GET', 'POST'])
def login():
   form = loginForm()
   if form.validate_on_submit():
       user=User.query.filter_by(email=form.email.data).first()
       if user is None or not user.check_password(form.password.data):
           flash('Incorrect name or password')
           return redirect(url_for('login'))
       login_user(user)
       return redirect(url_for('landing'))
   return render_template('Login.html', form=form, title='Login')

@app.route('/search')
def search():
   searched=Product.query.[something]()
   return render_template('Search.html', products=searched, title='Search')

@app.route('/user/<name>')
def user(name):
   if len(User.query.filter_by(username=name).all()) > 0:
       chosenUser=User.query.filter_by(username=name).first()
       chosenProducts=Product.query.filter_by(user_id=chosenUser.user_id).all()
       return render_template('User.html', title='User', userName=chosenUser.firstname,
                              hometown=Location.query.filter_by(user_id=chosenUser.user_id).first(),
                              description=chosenUser.description, productList=chosenProducts)
   else:
       abort(404)

@app.route('/product/<productName>')
def product(productName):
   if len(Product.query.filter_by(name=productName).all()) > 0:
       chosenProduct=Product.query.filter_by(name=productName).first()
       chosenUser=User.query.filter_by(user_id=chosenProduct.user_id).first()
       return render_template('Product.html', title='Product', name=productName, userName=chosenUser.firstname,
                              location=Location.query.filter_by(user_id=chosenUser.user_id).first(),
                              description=chosenProduct.description, date=chosenProduct.dateHarvested,
                              productPrice=chosenProduct.price, amount=chosenProduct.amount)
   else:
       abort(404)

@app.route('/newProduct', methods=['GET','POST'])
def newProduct():
   form = productForm()
   if form.validate_on_submit():
           flash('New product created: {}'.format(form.name.data))
           newP= Product(name=form.name.data, description=form.description.data, price=form.description.price, amount=form.amount.data, dateHarvested=form.date.data)
           db.session.add(newP)
           db.session.commit()
           return redirect(url_for('landing'))
   return render_template('newProduct.html', title='New Product', form=form)

@app.route('/register', methods=['GET','POST'])
def register():
   form = registerForm()
   if form.validate_on_submit():
       if len(User.query.filter_by(username=form.username.data).all()) > 0:
           flash('That name already exists')
       else:
           flash('New user created. You can now log in.')
           newU= User(email=form.email.data, password=form.password.data, accountType=form.account.data)
           newU.set_password(form.password.data)
           db.session.add(newU)
           db.session.commit()
           return redirect(url_for('landing'))
   return render_template('Register.html', form=form, title='Register')

@app.route('/populate_db')
def populate_db():
    return "placeholder"

@app.route('/reset_db')
def reset_db():
    flash("Resetting database")
    metadata=db.metadata
    for table in reversed(metadata.sorted_tables):
        print('Clear table {}'.format(table))
        db.session.execute(table.delete())
    db.session.commit()
    populate_db()
    return "Data reset"
