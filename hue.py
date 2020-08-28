import json
import requests

class Hue():
    def __init__(self, ip, username):
        self.ip = ip
        self.username = username

    def get(self):
        """
        Get the light information from the bridge
        """
        url = "http://" + self.ip + "/api/" + self.username + "/lights"
        response = requests.get(url)
        data = response.json()
        return data


    def toggle(self, light_id):
        """
        Toggle the current state of the light
        """ 

        url = "http://" + self.ip + "/api/" + self.username + "/lights/" + light_id + "/" + state

        response = requests.get(url)
        data = response.json()
        return data