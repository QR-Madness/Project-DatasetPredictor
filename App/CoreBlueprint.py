from flask import Blueprint
from flask import render_template

# App Blueprint
CoreBlueprint = Blueprint(
    "Core_Blueprint",
    "CoreBlueprint",
    static_folder="Static/",
    static_url_path='/',
    template_folder="Templates/",
)


@CoreBlueprint.route("/")
def page_index():
    return render_template("Index.j2.html")
