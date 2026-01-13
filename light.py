import subprocess
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
import os

HOST = "127.0.0.1"
PORT = 8000

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INDEX_FILE = os.path.join(BASE_DIR, "index.html")


def get_light_value():
    proc = subprocess.run(
        ["termux-sensor", "-s", "LIGHT", "-n", "1"],
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        check=True
    )

    data = json.loads(proc.stdout.decode())
    light = data["LIGHT"]["values"][0]
    print("Light level:", light)
    return light


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = urlparse(self.path).path

        # ---------- JSON API ----------
        if path == "/light":
            value = get_light_value()
            data = {"light": value}

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode())
            return

        # ---------- HTML ----------
        if path == "/" or path == "/index.html":
            if not os.path.exists(INDEX_FILE):
                self.send_response(500)
                self.end_headers()
                self.wfile.write(b"index.html not found")
                return

            with open(INDEX_FILE, "rb") as f:
                html = f.read()

            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(html)
            return

        # ---------- 404 ----------
        self.send_response(404)
        self.end_headers()


if __name__ == "__main__":
    print(f"Serving on http://{HOST}:{PORT}")
    HTTPServer((HOST, PORT), Handler).serve_forever()
