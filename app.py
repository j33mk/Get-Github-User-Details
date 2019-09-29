from flask import Flask, render_template, request

from get_email_script.get_email import get_email

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])  # reference to the index page
def index():
    if request.method == 'POST':
        # Get Form Fields
        username = request.form['username']

        results = get_email(username)

        return render_template('index.html', username=results)

    return render_template('index.html', )


if __name__ == "__main__":  # main function for the python
    app.secret_key = 'secretkey1122'
    app.run(debug=True)
