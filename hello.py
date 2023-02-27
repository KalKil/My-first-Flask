from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template(
        "home.html.jinja", 
        my_variable="shabadaba do it like a miboo",
        my_list=["apples", "bananas","oranges"]
    )
@app.route("/ping")
def ping():
    return "<p>ping</p>"

@app.route("/hello<name>")
def hello(name):
    return f"<p>Hello, {name} !</p>"