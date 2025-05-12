from flask import Flask, request, jsonify
import mysql.connector
import os
from prometheus_flask_exporter import PrometheusMetrics


app = Flask(__name__)

MYSQL_HOST = os.getenv("MYSQL_HOST", "mysql")
MYSQL_USER = os.getenv("MYSQL_USER", "root")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "password")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE", "movies_db")

metrics = PrometheusMetrics(app)
metrics.info("app_info", "Movie backend application", version="1.0.0")


def get_db_connection():
    return mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE,
    )


@app.route("/backend/all_movies", methods=["GET"])
def get_movies():
    try:
        db = get_db_connection()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM movie")
        movies = cursor.fetchall()
        cursor.close()
        db.close()
        return jsonify(movies)
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500


@app.route("/backend/add_movie", methods=["POST"])
def add_movie():
    title = request.args.get("title")
    year = request.args.get("year")
    if not title or not year:
        return jsonify({"error": "Title and year required"}), 400

    try:
        db = get_db_connection()
        cursor = db.cursor()
        cursor.execute("INSERT INTO movie (title, year) VALUES (%s, %s)", (title, year))
        db.commit()
        cursor.close()
        db.close()
        return jsonify({"message": "Movie added"})
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500


@app.route("/backend/remove_movie", methods=["DELETE"])
def remove_movie():
    movie_id = request.args.get("id")
    if not movie_id:
        return jsonify({"error": "Movie ID required"}), 400

    try:
        db = get_db_connection()
        cursor = db.cursor()
        cursor.execute("DELETE FROM movie WHERE id = %s", (movie_id,))
        db.commit()
        cursor.close()
        db.close()
        return jsonify({"message": "Movie removed"})
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500


@app.route("/backend/edit_movie", methods=["PUT"])
def edit_movie():
    movie_id = request.args.get("id")
    title = request.args.get("title")
    year = request.args.get("year")
    if not movie_id or not title or not year:
        return jsonify({"error": "Movie ID, title, and year required"}), 400

    try:
        db = get_db_connection()
        cursor = db.cursor()
        cursor.execute(
            "UPDATE movie SET title = %s, year = %s WHERE id = %s",
            (title, year, movie_id),
        )
        db.commit()
        cursor.close()
        db.close()
        return jsonify({"message": "Movie updated"})
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
