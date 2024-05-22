from flask import Flask, request, render_template, redirect, url_for
import os
app = Flask(__name__)
img = os.path.join('static', 'photo')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return redirect(url_for('hello', username=request.form.get('username')))

    return render_template('login.html')
    

@app.route('/hello/<username>')
def hello(username):
    return render_template('hello.html', username=username)

img = os.path.join('static', 'photo')
 


if __name__ == '__main__':
    app.debug = True
    app.run()