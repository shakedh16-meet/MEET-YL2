from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)


@app.route('/')
def home_page():
	return render_template('home_page.html')

@app.route('/about')
def about_me():
	return render_template('about_me.html')

@app.route('/contact')
def contact_me():
	return render_template('contact_me.html')

@app.route('/sent', methods = ['POST'])
def sent_page():
	return render_template('sent_page.html')


if __name__ == "__main__":
    app.run(debug=True)