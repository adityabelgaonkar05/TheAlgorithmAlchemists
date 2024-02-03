from flask import Flask, request , render_template , jsonify
import gemini

app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
def home():
    if request.method == "GET":
        return render_template("index.html")
    if request.method == 'POST':
        prompt1 = request.form["salary"]
        prompt2 = request.form["goal"]
        prompt3 = request.form["needs"]
        prompt4 = request.form["message"]

        return jsonify({"recommendations" : (gemini.gemini(prompt1,prompt2,prompt3,prompt4))})
    else:
        return render_template("index.html")
    

if __name__ == "__main__":
    app.run(debug = True)
