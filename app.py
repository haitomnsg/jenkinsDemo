from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")
    return render_template("result.html", name=name, email=email, message=message)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)