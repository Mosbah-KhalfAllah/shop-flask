from flask import Flask, render_template

app = Flask(__name__)

categories = [
    {"name": "Électronique", "image": "e-1.jpg"},
    {"name": "Vêtements", "image": "e-2.jpg"},
    {"name": "Maison", "image": "e-3.jpg"},
    {"name": "Jouets", "image": "e-4.jpeg"},
    {"name": "Sports", "image": "e-5.jpg"},
    {"name": "Jardinage", "image": "e-6.avif"},
    {"name": "Automobile", "image": "e-7.gif"},
    {"name": "Beauté", "image": "e-8.jpg"}
]

@app.route('/')
@app.route('/home')
@app.route('/shop')
@app.route('/acceuil')
def home():
    return render_template('home.html', title='Home', categories = categories)

@app.route('/services')    
def services():
    return render_template('servies.html', title = 'Services')

@app.route('/about')
def about():
    return render_template('about.html', title = 'About')

@app.route('/register')
def register():
    return render_template('register.html', title = 'Register')

@app.route('/login')
def login():
    return render_template('login.html', title = 'Login')

if __name__ == '__main__':
    app.run(debug=True)
