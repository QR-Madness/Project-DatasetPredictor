from flask import Blueprint, jsonify
from flask import render_template
from Script.BicycleThefts import BicycleThefts

# App Blueprint
CoreBlueprint = Blueprint(
    "Core_Blueprint",
    "CoreBlueprint",
    static_folder="Static/",
    static_url_path="/",
    template_folder="Templates/",
)


@CoreBlueprint.route("/")
def page_index():
    return render_template("Index.j2.html")


@CoreBlueprint.route("/dashboard")
def page_dashboard():
    return render_template("Dashboard.j2.html")


@CoreBlueprint.route("/data-stats")
def page_component_data_stats():
    thefts = BicycleThefts()
    # render stats into an HTML element
    stats_info_element = thefts.get_description().to_html()
    return jsonify(html=stats_info_element)
