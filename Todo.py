from flask import Flask, render_template

app = Flask(__name__)

my_todo_list=["New Controller"," Rechargeable Batteries","Get more Bacon"]

@app.route("/")
def index():
    return render_template(
        "todo.html.jinja",
        todo=my_todo_list
        )

@app.route("/add", methods=)
