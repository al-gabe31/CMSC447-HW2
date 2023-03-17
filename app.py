# Note: I have yet to figure out how to configure the database to my CURD website
# My CURD should still work with Flask, HTML, CSS, and JavaScript
# The only thing that's missing is the database part of the HW
# Because of that, the CURD won't remember any new/deleted data

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)