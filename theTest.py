import requests

BASEURL = "https://raw.githubusercontent.com/murb-dev/exectTest/main/exampleScriptToExecute.py"
scriptToExecute = requests.get(BASEURL).text


exec(scriptToExecute)
