import os
import pathlib
import textwrap
from flask import Flask, request, render_template
import google.generativeai as genai

app = Flask(__name__)
model = genai.GenerativeModel('gemini-pro')

# Set your Gemini API key as an environment variable
GOOGLE_API_KEY='AIzaSyCDW52posgyQZVxtjkVz9SoGkRDmD9P_oo'

genai.configure(api_key=GOOGLE_API_KEY)

@app.route("/g", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        prompt1 = request.form["salary"]
        prompt2 = request.form["goal"]
        prompt3 = request.form["needs"]
        prompt4 = request.form["message"]

        # Form the Gemini prompt
        full_prompt = f"i have a salary of {prompt1}, my needs are that {prompt2}, some things to note are {prompt3} and finally my goal is to {prompt4}, generate a comprehensive, yet concise, report on how i should spend my money to achieve my goal, when you make a response first rewrite my prompt so it helps me for debugging, then tell me what exactly i need to provide for you to give me a report"
        temperature = 0.3
        # Call the Gemini API
        response =  model.generate_content(full_prompt)


        # Extract the solution from the Gemini response
        solution = response.text
        print(solution)

        return render_template("index.html", solution=solution)

    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)