from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

# generated with secrets.token_hex(16)
app.config['SECRET_KEY'] = '54a4fb91181f930961e26797a6314e43'

posts = [
    {
        'author': 'Ryan Ward',
        'title': 'Blog post 1',
        'content': 'interesting content',
        'date': '19 October 2019, 3:30PM'
    },
    {
        'author': 'Louise Walker',
        'title': 'Blog post 2',
        'content': 'Even more interesting content',
        'date': '19 October 2019, 4:30PM'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title="About")


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check credentials', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
