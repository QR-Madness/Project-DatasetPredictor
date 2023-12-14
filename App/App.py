from flask import Flask
from argparse import ArgumentParser
from argparse import BooleanOptionalAction
from CoreBlueprint import CoreBlueprint

arguments = ArgumentParser("COMP309 Police Dataset Predictor")
arguments.add_argument(
    "-p", "--port", type=int, default=8080, help="Server port number"
)
arguments.add_argument(
    "-a", "--address", type=str, default="127.0.0.1", help="Server address"
)
arguments.add_argument(
    "-dd",
    "--disable-debug",
    action=BooleanOptionalAction,
    help="Flag to disable debug mode",
)


def assemble_app() -> Flask:
    new_app = Flask("COMP309 Police Dataset Predictor App")
    args = arguments.parse_args()
    new_app.debug = not args.disable_debug
    # set host and port
    new_app.config["SERVER_NAME"] = args.address + ":" + str(args.port)
    # resource directories
    return new_app


# MAIN FUNCTION
if __name__ == "__main__":
    server_app = assemble_app()
    # blueprints
    server_app.register_blueprint(CoreBlueprint)
    # start listening
    server_app.run()
