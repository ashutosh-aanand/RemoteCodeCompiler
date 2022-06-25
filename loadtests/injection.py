import requests
import threading

# C
cInput = open("inputs/amShZWinsABet-1.txt", "r").read()
cExpectedOutput = open("expected-outputs/amShZWinsABet-1.txt", "r").read()
cSourceCode = open("source-code/AmShZWinsABet.c", "r").read()

cData = {
    "expectedOutput": cExpectedOutput,
    "input": cInput,
    "language": "C",
    "memoryLimit": 1500,
    "sourceCode": cSourceCode,
    "timeLimit": 15
}

# Python
pythonInput = open("inputs/makeEven-1.txt", "r").read()
pythonExpectedOutput = open("expected-outputs/makeEven-1.txt", "r").read()
pythonSourceCode = open("source-code/MakeEven.py", "r").read()

pythonData = {
    "expectedOutput": pythonExpectedOutput,
    "input": pythonInput,
    "language": "PYTHON",
    "memoryLimit": 1500,
    "sourceCode": pythonSourceCode,
    "timeLimit": 15
}

URL = "http://localhost:8080/api/compile/json"
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

class cthread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    # helper function to execute the threads
    def run(self):
        requests.post(url = URL, json = cData, headers = headers)

class pythonthread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    # helper function to execute the threads
    def run(self):
        requests.post(url = URL, json = pythonData, headers = headers)

for i in range(1000):
    cRequestThread = cthread()
    cRequestThread.start()
    pythonRequestThread = pythonthread()
    pythonRequestThread.start()