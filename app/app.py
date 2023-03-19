#from dotenv import load_dotenv
from flask import Flask, redirect, render_template, request, url_for

from twitter_api import *
from threadgen import *

app = Flask(__name__)
#load_dotenv()
openai.api_key = "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"


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        question = request.form["question"]
        year = request.form["slider-val"]

        print(year)
        # errors = get_moderation(question)
        # if errors:
        #     for error in errors:
        #         print(error)
        #     return render_template("index.html", result="Sorry, I cannot answer that question.")
        twitterList = twitter_api_call(search=question)

        print(twitterList[0:4])

        response = ""
        for item in gpt(twitterList[0:4], year):
            response = response + item + "<br/> <br/> <br/>"

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


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)