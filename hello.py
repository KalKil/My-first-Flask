from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template(
        "home.html.jinja", "Todo.html.jinja", 
        my_variable="shabadaba do it like a miboo",
        my_list=["apples", "bananas","oranges"],
        my_todo_list=["New Controller"," Rechargeable Batteries","Get more Bacon"]
        )
@app.route("/ping")
def ping():
    return "<p>ping</p>"

@app.route("/hello<name>")
def hello(name): 
    return f"<p>Hello, {name} !</p>"
