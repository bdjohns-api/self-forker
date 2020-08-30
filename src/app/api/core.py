from flask import Blueprint, jsonify


api = Blueprint("core_endpoints", __name__)


@api.route("/healthz", methods=["GET"])
def check_health():
    """Return an API response indicating the API is in a healthy state."""
    return jsonify({"status": "HEALTHY"})

