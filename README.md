# Team
**Team name**: Hungry Panda

**Team member**:
| Name | Netid | Contribution |
| ---- | ----- | ------------ |
| Tingyu Zeng | tzeng11 | Architecture |
| Sicheng Meng | meng29 | Extension: data crawling | 
| Yiwei Kuang | yiwei9 | Backend: info retrieval and sentiment analysis |
| Jiachun Tang | jiachun5 | Backend: info retrieval and sentiment analysis |
| Fangsheng Yang | fyang28 | Extension: data presentation |

# Folder structure

- Project proposal: [Proposal.pdf](Proposal.pdf)
- Progress report: [Progress_Report.pdf](Progress_Report.pdf)
- Documentation: [Documentation.pdf](Documentation.pdf)

# 🎥 Presentation video

**The presentation video** can be accessed via [this link](https://youtu.be/mS6M2M5O2r8) (YouTube).

# Overview

When Yelp users rate a restaurant, they tend to give the rating based not only on taste and quality of the food, but also other factors such as service, prices, comfort, atmosphere, parking, and location, etc. 

As a group of Chinese students, our favorite dim sum restaurants usually don’t have a high rating on Yelp, partly because traditional dim sum places focus on taste of food, but many of them don’t focus on service, known as “cantonese hospitality”. You have to read each review if you want to know how good the food is. 

We don't want to let bad service overshadow good food. Through text retrieval and mining techniques, we think it would be a great idea to analyze reviews that focus on food only.

With that interest, we created a Chrome-based extension to give an overview of what kind of food are frequently mentioned in the reviews and based on the review content what should be the sentimental score for this restaurant.


# Install

## Frontend

1. Clone the repository, 
2. Go to the Extensions page by entering chrome://extensions in a new tab. (By design chrome:// URLs are not linkable.)
3. Enable Developer Mode by clicking the toggle switch next to Developer mode.
4. Click the Load unpacked button and select the extension directory.

## Backend

There are 2 ways of installing the current dependencies:

1. \[ Recommended \]: if you have `conda` installed on your local machine, use `conda env create -f environment.yml` at the root directory. Activating the virtual environment can be done by `conda activate hungryPanda`.
2. Using `pip`: `pip install -r requirements.txt` (note that you may need to configure the virtual environment yourself and if the installation does not work, you may need to configure your Python version based on `runtime.txt`.)

If you need to add a new dependency to the project, use the command: `pip install <lib_name>`, e.g, `pip install flask`. After the installation, update the txt file by `pip list --format=freeze > requirements.txt`.

# Start developing

## Frontend

- [Loading the extension](https://developer.chrome.com/docs/extensions/mv3/getstarted/development-basics/) on Chrome
- [API references](https://developer.chrome.com/docs/extensions/reference/)

## Backend

- Make sure you installed all the dependencies.
- Starting the development server can be done by running this command in your terminal: `flask --app backend/app run --reload`. Then you can use [Postman](https://www.postman.com/) to interact with the endpoints.
- But you can also create an independent Python script that performs the desired action (say `nlp.py` under the `backend` folder), and develop further by running `python backend/nlp.py` in the root directory. In this way, you avoid the need of running the server during your development.

# How to run

1. Run the backend via `flask --app backend/app run --reload`.
2. Go to a Yelp website in Chrome and click on the extension icon.

# Implementation Details

See Documentation.pdf or code comments.

# Course Project

Please fork this repository and paste the github link of your fork on Microsoft CMT. Detailed instructions are on Coursera under Week 1: Course Project Overview/Week 9 Activities.
