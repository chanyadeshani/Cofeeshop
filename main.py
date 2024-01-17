from flask import Flask, render_template, jsonify
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = 'Some hard to guess key'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['Mail_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route('/login', methods=['GET', 'POST'])
def login():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('login.html', form=form, name=name)


@app.route('/menu')
def menu():
    products = {"Espresso": [["Latte", 3.0], ["Mocha", 4.0], ["Macchiato", 2], ["Cappuccino", 4], ["Americano", 5]],
                "Brewed Coffee": [["Filter coffee", 2], ["Iced Coffee & Cold Brew", 3]]
                }

    return render_template('menu.html', products=products)


if __name__ == '__main__':
    app.run(debug=True)
