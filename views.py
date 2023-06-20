from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for


views = Blueprint(__name__,"views")
####################################################
# ROUTES za new_index.html
@views.route("/hello")
def index():
    # flash funkcija omogućuje generiranje poruka koje se mogu prikazati korisnicima kada se izvrši određena akcija, 
    # poput slanja obrasca ili prijave u sustav. 
    flash("what's your name?")
    return render_template("new_index.html", name="Ivana")

@views.route("/greet", methods=["POST","GET"])
def greet():
    # ovime dohvaćamo input usera
    # unos varijable u zagradama treba odgovarati 
    # name inputu u html dokumentu (<input type="text" name="name_input">)
    # -> request.form['name_input']
    name_from_user = request.form['name_input']

    # flash pozdravna poruka 
    flash("Hi "+ str(name_from_user) + ", welcome!")

    return render_template("new_index.html")





####################################################
# ROUTES za index.html
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