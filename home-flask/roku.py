import os
import requests, json

# For a full list of actions see:
# https://developer.roku.com/docs/developer-program/debugging/external-control-api.md

class Roku:
    def __init__(self, ip):
        self.ip = ip

    def control(self, action):
        """
        Control the roku tv with their api
        """
        data = ''
        url = "http://" + self.ip + ":8060/keypress/" + action
        response = requests.post(url, data = json.dumps(data), timeout=10)