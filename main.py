from flask import Flask, render_template
import os

app = Flask(__name__)

# 🔹 Change this per client
studio_info = {
    "name": "Sai Photo Studio",
    "phone": "9876543210",
    "whatsapp": "919876543210",
    "city": "Hyderabad",
    "description": "Professional Wedding & Event Photography Services"
}

@app.route("/")
def home():
    return render_template("index.html", studio=studio_info)

@app.route("/services")
def services():
    return render_template("services.html", studio=studio_info)

@app.route("/gallery")
def gallery():
    return render_template("gallery.html", studio=studio_info)

@app.route("/contact")
def contact():
    return render_template("contact.html", studio=studio_info)

# ✅ Only ONE main block
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
