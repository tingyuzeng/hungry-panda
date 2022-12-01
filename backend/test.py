import json
def analysea_text():
    data_file = open(r'C:\Users\75750\cs410\final_project\hungry-panda\backend\yelp_academic_dataset_review.json')
    data = []
    with data_file as f:
        for line in f:
            data.append(json.loads(line))

    print(data)
    print(data[0]['text'])

analysea_text()