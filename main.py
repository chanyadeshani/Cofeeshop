from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Some hard to guess key'


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route('/')
def index():
    return render_template("home.html") # Add you dashboad here


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Print the form data to the console
        for key, value in request.form.items():
            print(f'{key}: {value}')

        # Can get name of the user from database here
        user_name = request.form['user_name']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        return redirect(url_for('login'))
    else:
        return render_template("register.html")


# login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Print the form data to the console
        for key, value in request.form.items():
            print(f'{key}: {value}')

            # Can get name of the user from database here
        session['user_id'] = request.form['user_id'],

        return redirect(url_for('index'))

    return render_template("login.html")


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

    # Process the order data as needed (e.g., save to a database, etc.)

    # Return a response (optional)
    return jsonify({'message': 'Order received successfully'})


if __name__ == '__main__':
    app.run(debug=True)