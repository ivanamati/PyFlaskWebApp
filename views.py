from flask import Blueprint,render_template, request, jsonify,redirect, url_for

views = Blueprint(__name__,"views")

@views.route("/")
def home():
    return render_template("index.html", name = "PyRats")


# ovako pristupamo ako predamo u url username
# @views.route("/profile/<username>")
# def profile(username):
#     return render_template("index.html", name=username)

@views.route("/profile")
def profile():
    args = request.args
    name = args.get('name')
    #return render_template("index.html", name=name)
    return render_template("profile.html")

# how to return json
@views.route("/json")
def get_json():
    return jsonify({'name':'ivana', 'age':38})

# ovako pristupimo jsonu pomocu route
@views.route("/data")
def get_data():
    data = request.json
    return jsonify(data)

# redirect to a home page
@views.route("/go-to-home")
def go_to_home():
    # ovdje u zagradi nakon views. pisemo ime funkcije na koju stranicu zelimo otici
    return redirect(url_for("views.home"))

# redirect to a json page
@views.route("/go-to-json")
def go_to_json():
    return redirect(url_for("views.get_json"))