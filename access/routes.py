from access import app
from flask import render_template, redirect, url_for, flash
from access.forms import RegisterForm
from flask_sqlalchemy import SQLAlchemy
from access.models import Item, User
from access import db


@app.route('/')
@app.route('/home')
def index_page():
    return render_template('index.html')


@app.route('/subscription')
def subscription_page():
    # items = Item.query.all()  # the database is not working so trying to work out a fix)
    items = [
        {'id': 1, 'name': 'Subscription Free',
            'Details': 'Read ONly Axcess', 'Price': 0},
        {'id': 2, 'name': 'Subscription Axcess',
         'Details': 'Axcess to Information', 'Price': 10},
        {'id': 3, 'name': 'Subscription Axcess All areas',
            'Details': 'Axcess All Areas', 'Price': 25}
    ]
    return render_template('subscription.html', items=items)


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email_address=form.email_address.data,
                              password_hash=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('subscription_page'))
    if form.errors != {}:  # checks the validation to see if correct and give a message back if !=-not equla to
        for err_msg in form.errors.values():
           flash(f'There is an error:{err_msg}', category='danger')
    return render_template('register.html', form=form)
