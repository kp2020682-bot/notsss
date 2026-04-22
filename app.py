from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Railway MySQL connection
def get_db():
    return mysql.connector.connect(
        host="nozomi.proxy.rlwy.net",
        user="root",
        password="BzyxxmYNRexcCSKegAqhpVwenoDzERid",
        database="railway",
        port=43405
    )

@app.route("/")
def home():
    return render_template("form.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    email = request.form["email"]

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO users (name, email) VALUES (%s, %s)",
        (name, email)
    )

    conn.commit()
    cursor.close()
    conn.close()

    return """
    <div style="text-align:center; margin-top:100px; font-family:Arial;">
        <h2 style="color:green;">Data saved successfully!</h2>

        <a href="/">
            <button style="
                padding:12px 25px;
                font-size:16px;
                background:#2575fc;
                color:white;
                border:none;
                border-radius:6px;
                cursor:pointer;">
                Fill Again
            </button>
        </a>
    </div>
    """

if __name__ == "__main__":
    app.run(debug=True)
