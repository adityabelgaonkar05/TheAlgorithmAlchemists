import google.generativeai as genai

model = genai.GenerativeModel('gemini-pro')
GOOGLE_API_KEY='AIzaSyCDW52posgyQZVxtjkVz9SoGkRDmD9P_oo'
genai.configure(api_key=GOOGLE_API_KEY)

def gemini(prompt1,prompt2,prompt3,prompt4):
    format = [
            {
                "action": "Add a description action in string format that the user needs to take",
                "amount": "Add a numerical value according to you in int form"
            },
            {
                "action": "Add a description action in string format that the user needs to take",
                "amount": "Add value according to you"
            },
            {
                "action": "Add a description action in string format that the user needs to take",
                "amount": "Add value according to you"
            },
            {
                "action": "Add a description action in string format that the user needs to take",
                "amount": "Add value according to you"
            },
            {
                "action": "Add a description action in string format that the user needs to take",
                "amount": "Add value according to you"
            },
            {
                "action": "Add a description action in string format that the user needs to take",
                "amount": "Add value according to you"
            }
    ]
    while True:
        try:
            full_prompt = f"i have a salary of : {prompt1} ruppes per month, my needs are that : {prompt2}, some things to note are : {prompt3} and finally my goal is :  {prompt4}, generate a comprehensive, yet concise,monthly budget plan on how i should spend my money this month to achieve my goals, please reply in following format ONLY :- {format}"
            response =  model.generate_content(full_prompt)
            solution = (response.text)
            if solution[0]=="`":
                solution = solution.replace("`","")
            solution = eval(solution)
            break
        except:
            continue
    return solution