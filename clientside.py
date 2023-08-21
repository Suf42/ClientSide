import requests
import json
import uuid

## Request Structure

# req = {
#     "token": '',
#     "machineid": ''
# }

## Response Structure

# resp = {
#     "status": True,
#     "message": '',
#     "permission": {}
# }

# possible messages:

## Invalid Token Issues ##
## Token doesn't exist.
## Token already in use.

## Token Successfully used ##
## Token Used.



def generateJson(token):

    req = {
        "token": token,
        "machineid": str(uuid.UUID(int=uuid.getnode()))
    }

    return req

def printResponse(resp):

    print('Access granted: {}'.format(json.loads(resp.text)["status"]))
    print('Message: {}'.format(json.loads(resp.text)["message"]))
    print('Permission: ')
    for fea in json.loads(resp.text)["permission"].keys():
        print('{}: expires {}'.format(fea, json.loads(resp.text)["permission"][fea]))

if __name__=="__main__":

    ## Some sequence e.g. GUI/argparsing to take consume (token, root) arguments ##

    ## Sample arguments
    token = "C3AF-7E11-2C3E-4FF0"
    url = "http://127.0.0.1:8000/validate-token/"

    req = generateJson(token)
    resp = requests.post(url = url, data = req)

    printResponse(resp)