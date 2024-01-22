from flask import Flask, render_template, jsonify, request
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

    # Return a response (optional)
    return jsonify({'message': 'Order received successfully'})


if __name__ == '__main__':
    app.run(debug=True)
