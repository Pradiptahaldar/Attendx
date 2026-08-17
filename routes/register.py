from flask import Blueprint, render_template

register = Blueprint("register", __name__)

@register.route("/setup")
def setup():
    return render_template("auth/setup.html")