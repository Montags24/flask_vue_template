from flask import jsonify
from api.bp_template import bp


@bp.route("/")
def test_route():
    return jsonify({"ping": "pong"})
