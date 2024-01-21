#!/usr/bin/python3
"""
main Flask app
"""
from flask import Flask, Blueprint, jsonify
import os
from models import storage
from api.v1.views import app_views
from flask_cors import CORS

app = Flask(__name__)

app.register_blueprint(app_views, url_prefix='/api/v1')
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.teardown_appcontext
def close_storage(exception):
    """Closes the storage on teardown."""
    PHARMACY_ENV = getenv('PHARMACY_ENV')
    if PHARMACY_ENV = db:
        storage.close()


@app.errorhandler(404)
def not_found(error):
    """Handles 404 errors and returns a JSON response."""
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    host = os.getenv('PHARMACY_API_HOST', '0.0.0.0')
    port = int(os.getenv('PHARMACY_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)
