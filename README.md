# Team
**Team name**: Hungry Panda

**Team member**:
| Name | netid |
| ---- | ----- |
| Tingyu Zeng | tzeng11 | 
| Sicheng Meng | meng29 |
| Yiwei Kuang | yiwei9 |
| Jiachun Tang | jiachun5 |
| Fangsheng Yang | fyang28 |

# Folder structure
- Project proposal: [Proposal.pdf](Proposal.pdf)

# Install

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

# Course Project

Please fork this repository and paste the github link of your fork on Microsoft CMT. Detailed instructions are on Coursera under Week 1: Course Project Overview/Week 9 Activities.
