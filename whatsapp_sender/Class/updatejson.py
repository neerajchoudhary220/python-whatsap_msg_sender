import json
def update(number_of_message):
    jsonFile = open(r'json/index.json','r')
    data = json.load(jsonFile)
    jsonFile.close()

    # tmp = data['message']['number_of_msg']
    data['message']['number_of_msg'] = number_of_message

    jsonFile = open(r'json/index.json','w+')
    jsonFile.write(json.dumps(data))
    jsonFile.close()