"""Minimal web app that reads its settings from environment variables (standard library only).

systemd starts it through the Corrie Config launcher, so the variables come from config.corrie.io.
"""
import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer

SETTINGS = {
    "api_url": os.environ.get("API_URL", ""),
    "new_checkout": os.environ.get("FEATURE_NEW_CHECKOUT") == "true",
    "db_host": os.environ.get("DB_HOST", ""),
    "db_pool": int(os.environ.get("DB_POOL", "5")),
}


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = json.dumps({"ok": True, "settings": SETTINGS}).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8077"))
    print("listening on %d, API_URL=%s" % (port, SETTINGS["api_url"]), flush=True)
    HTTPServer(("127.0.0.1", port), Handler).serve_forever()
