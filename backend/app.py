from flask import Flask, request , render_template , jsonify,redirect
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

        # return jsonify({"recommendations" : (gemini.gemini(prompt1,prompt2,prompt3,prompt4))})
        mylist = []
        for items in gemini.gemini(prompt1,prompt2,prompt3,prompt4):
            mylist.append([items["action"],items["amount"]])
        graph_data = {"params" : mylist}
        return render_template("result.html" , data = gemini.gemini(prompt1,prompt2,prompt3,prompt4) , salary = request.form["salary"] , graph_data = graph_data)
    else:
        return render_template("index.html")

@app.route("/premium")
def premium():
    return render_template("login.html")

@app.route("/taxation", methods=["POST","GET"])
def taxation():
    if request.method == "GET":
        return render_template("taxation.html")
    if request.method=="POST":
        value = gemini.Taxation
        return jsonify({"FIN" : value})

if __name__ == "__main__":
    app.run(debug = True)
