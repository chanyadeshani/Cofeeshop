from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/second_page')
def secondpage():
    return render_template('second_page.html')


@app.route('/user/<username>')
def show_user(username):
    # Greet the user
    return 'Hello ' + username
gender = "Male"
gender = gender.capitalize().strip()
@app.route('/menu/')
def menu():
    products = {"Espresso":["Latte","Mocha","Macchiato","Cappuccino","Americano"],
                "Brewed Coffee":["Filter coffee", "Iced Coffee & Cold Brew"],
                "Hot Tea":["Brewed Tea","Tea Latte"],
                "Iced Tea":["Iced Tea","Iced Tea Latte"],
                "Hot Chocolate":["Classic Hot Chocolate","White Hot Chocolate"]
                }

    return render_template('menu.html', products=products)


if __name__ == '__main__':
    app.run(debug=True)
