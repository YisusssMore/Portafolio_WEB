from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def save_feedback(email, comment):
    conn = sqlite3.connect("feedback.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO feedback (email, comment) VALUES (?, ?)",
        (email, comment)
    )
    conn.commit()
    conn.close()

@app.route("/", methods=["GET", "POST"])
def index():
    button_python = False
    button_discord = False
    button_html = False
    button_db = False
    message = ""

    if request.method == "POST":

        # --- BOTONES DE PROYECTOS ---
        if "button_python" in request.form:
            button_python = True
        if "button_discord" in request.form:
            button_discord = True
        if "button_html" in request.form:
            button_html = True
        if "button_db" in request.form:
            button_db = True

        # --- FORMULARIO FEEDBACK ---
        email = request.form.get("email")
        text = request.form.get("text")

        if email and text:
            save_feedback(email, text)
            message = "Comentario guardado correctamente ✔"

    return render_template(
        "index.html",
        button_python=button_python,
        button_discord=button_discord,
        button_html=button_html,
        button_db=button_db,
        message=message
    )

if __name__ == "__main__":
    app.run(debug=True)
