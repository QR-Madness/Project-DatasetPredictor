from flask import Blueprint, jsonify
from flask import render_template
from Script.BicycleThefts import BicycleThefts

# App Blueprint
ApiBlueprint = Blueprint(
    "API Blueprint",
    "API_Blueprint",
    static_folder="Static/",
    static_url_path="/",
    template_folder="Templates/",
)


@ApiBlueprint.route("/")
def page_index():
    return "Success"


@ApiBlueprint.route("/data-stats")
def page_component_data_stats():
    thefts = BicycleThefts()
    # render stats into an HTML element
    stats_info_element = thefts.get_description().to_html()
    return jsonify(html=stats_info_element)
