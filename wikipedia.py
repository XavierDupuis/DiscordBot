import requests
import json

def get_data(search, numberResults=3):
    raw_response = requests.get("https://en.wikipedia.org/w/api.php?action=opensearch"\
                                f"&search={search}"\
                                f"&limit={numberResults}"\
                                "&namespace=0"\
                                "&format=json").text
    response = json.loads(raw_response)
    return response

def get_results(search, numberResults=3):
    data = get_data(search, numberResults)
    out = "Results for \"" + search + "\" on Wikipedia\n\n"
    for i in range(len(data[1])):
        out += data[1][i] + "\n" + data[3][i] + "\n\n"
    return out
