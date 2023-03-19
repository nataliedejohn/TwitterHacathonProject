import openai
#from dotenv import load_dotenv
from flask import Flask, redirect, render_template, request, url_for

from twitter_api import *

app = Flask(__name__)
#load_dotenv()
openai.api_key = "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"


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        question = request.form["question"]
        year = request.form["year"]
        # errors = get_moderation(question)
        # if errors:
        #     for error in errors:
        #         print(error)
        #     return render_template("index.html", result="Sorry, I cannot answer that question.")
        twitterList = twitter_api_call(search=question)

        print(twitterList)

        response = "Question: "+twitterList[0]+"\n\n"+openai.Completion.create(
                model="text-davinci-003",
                prompt=generate_prompt(twitterList[0], 1960),
                temperature=0.6,
                max_tokens=100
            ).choices[0].text

        print(response)
        return redirect(url_for("index", result=response))
    result = request.args.get("result")
    return render_template("index.html", result=result)


# def get_moderation(question):
#     """
#     Check the question is safe to ask the model
#
#     Parameters:
#         question (str): The question to check
#
#     Returns a list of errors if the question is not safe, otherwise returns None
#     """
#
#     errors = {
#         "hate": "Content that expresses, incites, or promotes hate based on race, gender, ethnicity, religion, nationality, sexual orientation, disability status, or caste.",
#         "hate/threatening": "Hateful content that also includes violence or serious harm towards the targeted group.",
#         "self-harm": "Content that promotes, encourages, or depicts acts of self-harm, such as suicide, cutting, and eating disorders.",
#         "sexual": "Content meant to arouse sexual excitement, such as the description of sexual activity, or that promotes sexual services (excluding sex education and wellness).",
#         "sexual/minors": "Sexual content that includes an individual who is under 18 years old.",
#         "violence": "Content that promotes or glorifies violence or celebrates the suffering or humiliation of others.",
#         "violence/graphic": "Violent content that depicts death, violence, or serious physical injury in extreme graphic detail.",
#     }
#     response = openai.Moderation.create(input=question)
#     if response.results[0].flagged:
#         # get the categories that are flagged and generate a message
#         result = [
#             error
#             for category, error in errors.items()
#             if response.results[0].categories[category]
#         ]
#         return result
#     return None


def generate_prompt(question, year):
    question_phrase = """You are a regular person from the {year}s. 
    Answer every question as if you had knowledge only limited to January 23rd, {year}.
    The day is January 23rd, {year}.
    You do not know about anything that happened or was invented after January 23rd, {year}.
    If something was invented after January 23rd, 1959, answer as if you do not know what they are talking about.
    Only answer questions with {year}'s rhetoric.
    Please aim to be as helpful, creative, and friendly as possible in all of your responses.
    Do not use any external URLs in your answers. Do not refer to any blogs in your answers.
    Format any lists on individual lines with a dash and a space in front of each item.
    Your name is Vinny. You live in Louisiana and speak with a Southern accent.
    You graduated from Harvard University.
    You believe the earth is flat.
    """.format(year=year)
    formatted_question = f'{question_phrase} \n {question}'
    return formatted_question


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)