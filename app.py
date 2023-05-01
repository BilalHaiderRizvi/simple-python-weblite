from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


#login & singup

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    confirm_password = request.form['confirm_password']
    

    if password != confirm_password:
        return 'Passwords do not match'
    return 'Logged in successfully'


@app.route('/signup', methods=['POST'])
def signup():
    new_username = request.form['new_username']
    new_password = request.form['new_password']
    confirm_new_password = request.form['confirm_new_password']
    

    if new_password != confirm_new_password:
        return 'Passwords do not match'
    return 'Signed up successfully'



if __name__ == '__main__':
    app.run(debug=True)
