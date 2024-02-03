from flask import Flask, request , render_template , jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/", methods=["POST","GET"])
@cross_origin()
def home():
    if request.method == "GET":
        return render_template("index.html")
    if request.method == 'POST':
        mydict = {}
        for key in request.form:
            mydict[key] = request.form[key]
        return jsonify(mydict)

if __name__ == "__main__":
    app.run(debug = True)
