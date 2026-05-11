from flask import Flask, jsonify, request, send_from_directory
import sqlite3
import os
import random

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect("words.db")
    conn.row_factory = sqlite3.Row
    return conn

# Serve words.html from the root folder
@app.route("/")
def serve_words_page():
    return send_from_directory(os.getcwd(), "words.html")

# READ all words
@app.route('/words', methods=['GET'])
def get_words():
    conn = get_db()
    rows = conn.execute("SELECT * FROM words").fetchall()
    conn.close()
    return jsonify([dict(row) for row in rows])

# CREATE a word
@app.route('/words', methods=['POST'])
def add_word():
    data = request.get_json()
    irish = data.get("irish", "").strip()
    english = data.get("english", "").strip()

    conn = get_db()
    cursor = conn.cursor()

    # Check if the Irish word already exists
    cursor.execute("SELECT english FROM words WHERE irish = ?", (irish,))
    row = cursor.fetchone()

    if row:
        # Existing meanings
        existing = row["english"].split(",")

        # New meanings
        new_meanings = [m.strip() for m in english.split(",")]

        # Merge + deduplicate
        merged = list(dict.fromkeys([m.strip() for m in existing + new_meanings]))

        # Update the row
        cursor.execute(
            "UPDATE words SET english = ? WHERE irish = ?",
            (", ".join(merged), irish)
        )
    else:
        # Insert new row
        cursor.execute(
            "INSERT INTO words (irish, english) VALUES (?, ?)",
            (irish, english)
        )

    conn.commit()
    conn.close()

    return jsonify({"message": "Word added"})


# UPDATE a word
@app.route('/words/<int:id>', methods=['PUT'])
def update_word(id):
    data = request.json
    irish = data.get("irish")
    english = data.get("english")

    conn = get_db()
    conn.execute(
        "UPDATE words SET irish = ?, english = ? WHERE id = ?",
        (irish, english, id)
    )
    conn.commit()
    conn.close()

    return jsonify({"message": "Word updated"})

# DELETE a word
@app.route('/words/<int:id>', methods=['DELETE'])
def delete_word(id):
    conn = get_db()
    conn.execute("DELETE FROM words WHERE id = ?", (id,))
    conn.commit()
    conn.close()

    return jsonify({"message": "Word deleted"})

@app.route("/test")
def test_page():
    return send_from_directory(os.getcwd(), "test.html")

@app.route("/random_word")
def random_word():
    conn = get_db()
    rows = conn.execute("SELECT * FROM words").fetchall()
    conn.close()

    if not rows:
        return jsonify({"error": "No words available"}), 400

    word = random.choice(rows)
    return jsonify({"id": word["id"], "irish": word["irish"], "english": word["english"]})

if __name__ == "__main__":
    app.run(debug=True)
