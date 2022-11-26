from flask import Flask
from flask_cors import CORS, cross_origin

import json
# import pandas as pd
import sys
import string
import re
import operator
from statistics import mean

app = Flask(__name__)
CORS(app)

@app.route("/")
@cross_origin()
def hello_world():
    return {"text": "hello world"}


mocked_data = [{"text": "relevant"}, {"text": "irrelevant"}]


@app.route("/analyse", methods=['POST'])
@cross_origin()

def analysea_text():
    data_file = open(r'C:\Users\75750\cs410\final_project\hungry-panda\backend\yelp_academic_dataset_review.json')
    data = []
    with data_file as f:
        for line in f:
            data.append(json.loads(line))

    print(data)
    print(data[0]['text'])

    review = review_retrieval(data)


    # creat the food dictionary
    with open(r'C:\Users\75750\cs410\final_project\hungry-panda\backend\Food_Dict.csv') as f:
        food_dictionary = [line.rstrip().lower() for line in f]
        print(food_dictionary)
        best_selling_food = {}
        foodhere = set()
        final_review = set()
        rank = []

    reviewlist4 = list(review)
    reviewlist5 = [line.rstrip().lower() for line in reviewlist4]

    # Upper Case
    for i in range(50):
        print(reviewlist4[i])
    # Lower Case
    for i in range(50):
        print(reviewlist5[i])

    food_showing_in_review(reviewlist4,reviewlist5,food_dictionary)

    sorted_x = sorted(best_selling_food.items(), key=lambda x: x[1], reverse=True)
    print(sorted_x)

    # Sentimental Analysis
    reviewlist = list(final_review)  # make a copy to modify
    scores = sentimentScores()
    yelpscores = []
    newWords = {}
    len(reviewlist)
    for i in range(len(reviewlist)):
        reviewlist[i].lower
        reviewlist[i] = re.compile("[^\w']|_").sub(" ", reviewlist[i]).split()
        sentiment = 0
        for words in reviewlist[i]:
            if words in scores:
                sentiment += scores[words]
        yelpscores.append(sentiment)
        # for words not in the sentiment dictionary, assign them a sentiment value based on sentiments of the tweet(s) found in
        print(yelpscores)
        final_score = mean(yelpscores)
        print(final_score)


def review_retrieval(data):
    review = []
    for i in range(len(data)):
        if "text" in data[i]:
            review.append(data[i]["text"])

    for i in range(50):
        print(review[i])

    return review

def food_showing_in_review(reviewlist4,reviewlist5,food_dictionary):
    best_selling_food = {}
    foodhere = set()
    final_review = set()

    for i in range(50):
        for j in range(len(food_dictionary)):
            x = reviewlist5[i].find(food_dictionary[j])

            if (x != -1):
                best_selling_food[food_dictionary[j]] = best_selling_food.setdefault(food_dictionary[j], 0) + 1
                foodhere.add(food_dictionary[j])

                final_review.add(reviewlist4[i])

    return best_selling_food,foodhere,final_review



def sentimentScores():
    afinnfile = open(r"C:\Users\kyw11\Downloads\AFINN-111.txt")
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    return scores