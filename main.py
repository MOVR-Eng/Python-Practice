from flask import Flask, render_template

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug=True)
