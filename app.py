from flask import Flask, render_template, request

app = Flask(__name__)
password = "1738"

@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html")

@app.route("/success", methods=["GET", "POST"])
def success():
    if request.method == "POST":
        output = request.form.to_dict()
        entered_password = output.get('password', '')
        if entered_password == password:
            return render_template("success.html")  # Assuming you have a success page
        else:
            return render_template("index.html", error="Incorrect Password")
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True, port=5001)