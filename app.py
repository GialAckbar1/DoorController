from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

password = "1738"
door_status = False  # False = locked, True = unlocked

@app.route('/')
@app.route('/home')
def home():
    # Render the password input form (index.html)
    return render_template("index.html")

@app.route("/success", methods=["POST"])
def success():
    if request.method == "POST":
        output = request.form.to_dict()
        entered_password = output.get('password', '')
        
        # Check if the password is correct
        if entered_password == password:
            # Render the success page with the current door status
            return render_template("success.html", status=door_status)
        else:
            # Re-render the password page with an error message if the password is wrong
            return render_template("index.html", error="Incorrect Password")
    
    return render_template("index.html")  # Fallback in case of a direct GET request

@app.route("/lock", methods=["POST"])
def lock_door():
    global door_status
    door_status = False  # Lock the door
    return jsonify({"message": "Door is now locked", "status": door_status})

@app.route("/unlock", methods=["POST"])
def unlock_door():
    global door_status
    door_status = True  # Unlock the door
    return jsonify({"message": "Door is now unlocked", "status": door_status})

if __name__ == '__main__':
    app.run(debug=True, port=5001)
