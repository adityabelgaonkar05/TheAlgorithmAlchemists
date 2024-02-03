from flask import Flask, request , render_template
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/home", methods=["POST","GET"])
@cross_origin()
def home():
    if request.method == "GET":
        return render_template("new.html")
    if request.method == 'POST':
        return {"username" : f"{request.form['username']}","password" :f"{request.form['password']}" }


if __name__ == "__main__":
    app.run(debug = True)
