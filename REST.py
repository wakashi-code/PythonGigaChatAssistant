from flask import Flask, jsonify, request
import requests
from SearchDataOnDataSpace import find_doctors

app = Flask(__name__)

def query_doctor_schedule(doctor_name):

    query = {
        "query": """
        {
            doctorSchedule(doctorName: "%s") {
                availableSlots
            }
        }
        """ % doctor_name
    }

    # GraphQL API
    url = "https://chromewebstore.google.com/detail/graphiql-extension/jhbedfdjpmemmbghfecnaeeiokonjclb"

    response = requests.post(url, json=query)

    if response.status_code == 200:
        return response.json()
    else:
        return None


@app.route('/doctors/schedule', methods=['GET'])
def call_find_doctors():
    find_doctors("info_doctor")


if __name__ == '__main__':
    app.run(debug=True)
