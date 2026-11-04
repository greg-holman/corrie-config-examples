"""Minimal Flask app that reads its settings from environment variables.

Start it with the Corrie Config launcher so the variables come from config.corrie.io:
    CORRIE_CONFIG_KEY=cfg_... sh launch.sh -- flask --app app run --port 5000
"""
import os

from flask import Flask, jsonify

app = Flask(__name__)

SETTINGS = {
    "api_url": os.environ.get("API_URL", ""),
    "new_checkout": os.environ.get("FEATURE_NEW_CHECKOUT") == "true",
    "db_host": os.environ.get("DB_HOST", ""),
    "db_pool": int(os.environ.get("DB_POOL", "5")),
}


@app.get("/")
def index():
    return jsonify(ok=True, settings=SETTINGS)
