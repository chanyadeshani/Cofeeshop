import datetime
from flask import Flask, render_template, request, jsonify

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SelectField, \
    SubmitField
from wtforms.validators import DataRequired, Length, Email

import database


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route('/')
@app.route('/menu')
def menu():
    products = {"Espresso": [["Latte", 3.5], ["Mocha", 4.75], ["Macchiato", 2], ["Cappuccino", 4], ["Americano", 5]],
                "Brewed Coffee": [["Filter coffee", 2], ["Iced Coffee & Cold Brew", 3]]
                }

    return render_template('menu.html', products=products)


# Define the route to handle order submission
@app.route('/submit_order', methods=['POST'])
def submit_order():
    # Extract data from the JSON payload
    data = request.get_json()
    items = data.get('items')
    price = data.get('price')

    # Process the order data as needed (e.g., save to a database, send confirmation email, etc.)
    order = [items, price]
    print(order[0], order[1])
    database.insert_order('coffee.db',order)

    # Return a response (optional)
    return jsonify({'message': 'Order received successfully'})


@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')


@app.route('/index', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('home.html', form=form, name=name)


if __name__ == '__main__':
    database.init_database('coffee.db')
    app.run(debug=True)
