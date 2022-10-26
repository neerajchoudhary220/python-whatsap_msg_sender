import json
jsonFile = open(r'json/index.json','r')
data = json.load(jsonFile)
jsonFile.close()
def number_of_msg():
    return data['message']['number_of_msg']

def buttonfg():
    return data['button']['fg']
def buttonbg():
    return data['button']['bg']

def buttonfont():
    return data['button']['font']
    