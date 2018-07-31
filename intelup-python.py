import requests
import json_tricks as json
from datetime import datetime, timezone


class Intelup(object):

    url = "https://api.intelup.app/v1/integration/iot/python"

    def __init__(self, token):
        self.token = token

    def sendOne(self, name, value, time=None):
        dt = datetime.now(timezone.utc)
        timestamp = int(
            (dt - datetime(1970, 1, 1, tzinfo=timezone.utc)).total_seconds())

        if time is None:
            time = timestamp

        headers = {'Content-Type': 'application/json'}
        payload = {'token': self.token, 'time': time,
                   'data_array': [{'name': name, 'value': value}]}
        try:
            r = requests.post(self.url, data=json.dumps(payload),
                              headers=headers, verify=False)
            print(r)
        except:
            pass

    def sendAll(self, data, time=None):
        dt = datetime.now(timezone.utc)
        timestamp = int(
            (dt - datetime(1970, 1, 1, tzinfo=timezone.utc)).total_seconds())

        if time is None:
            time = timestamp

        data_array = []

        for obj in data:
            if 'name' in obj and 'value' in obj:
                data_array.append(obj)

        if len(data_array) > 0:
            headers = {'Content-Type': 'application/json'}
            payload = {'token': self.token, 'time': time,
                       'data_array': data_array}
            try:
                r = requests.post(self.url, data=json.dumps(payload),
                                  headers=headers, verify=False)
                print(r)
            except:
                pass
