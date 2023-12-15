from flask import Blueprint, jsonify
from flask import render_template
from Models.BicycleThefts import BicycleTheftsPredictor

# App Blueprint
ApiBlueprint = Blueprint(
    "API Blueprint",
    "API_Blueprint",
    static_folder="Static/",
    static_url_path="/",
    template_folder="Templates/",
)
# TODO Save theft model in request dict for performance optimization


@ApiBlueprint.route("/")
def page_index():
    return "Success"


@ApiBlueprint.route("/data-stats")
def page_component_data_stats():
    thefts = BicycleTheftsPredictor()
    # render stats into an HTML element
    stats_table = thefts.get_description().to_html()
    return jsonify(html=stats_table)


@ApiBlueprint.route("/model-performance")
def page_component_model_performance():
    thefts = BicycleTheftsPredictor()
    # render stats into an HTML element
    performance_table = thefts.get_model_info().to_html()
    return jsonify(html=performance_table)


@ApiBlueprint.route("/model-predictions")
def page_component_model_predictions():
    thefts = BicycleTheftsPredictor()
    # render stats into an HTML element
    predictions_table = thefts.get_predictions().to_html()
    return jsonify(html=predictions_table)
