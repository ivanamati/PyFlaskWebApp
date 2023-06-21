from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for


views = Blueprint(__name__,"views")
####################################################
# ROUTES za new_index.html
@views.route("/hello")
def index():
    # flash funkcija omogućuje generiranje poruka koje se mogu prikazati korisnicima kada se izvrši određena akcija, 
    # poput slanja obrasca ili prijave u sustav. 
    flash("what's your name?")
    return render_template("index.html", name="Ivana")

@views.route("/greet", methods=["POST","GET"])
def greet():
    # ovime dohvaćamo input usera
    # unos varijable u zagradama treba odgovarati 
    # name inputu u html dokumentu (<input type="text" name="name_input">)
    # -> request.form['name_input']
    name_from_user = request.form['name_input']

    # flash pozdravna poruka 
    flash("Hi "+ str(name_from_user) + ", welcome!")

    return render_template("index.html")