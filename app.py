from flask import Flask, jsonify, render_template
from services.trail_loader import load_trails, load_trail_by_id

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/trail/<trail_id>")
    def trail_detail(trail_id):
        trail = load_trail_by_id(trail_id)
        if not trail:
            return "Trail not found", 404
        return render_template("trail.html", trail=trail)

    @app.route("/api/trails")
    def api_trails():
        return jsonify(load_trails())

    @app.route("/api/trail/<trail_id>")
    def api_trail(trail_id):
        trail = load_trail_by_id(trail_id)
        if not trail:
            return jsonify({"error": "Trail not found"}), 404
        return jsonify(trail)

    return app

app = create_app()
