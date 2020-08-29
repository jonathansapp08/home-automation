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
        response = requests.get(url, timeout=3)
        data = response.json()
        return data


    def toggle(self, light_id, current_state):
        """
        Toggle the current state of the light
        """ 
        if current_state == True:
            on = False
        else:
            on = True

        print(on)

        data = {"on":on}
        url = "http://" + self.ip + "/api/" + self.username + "/lights/" + light_id + "/state/"
        response = requests.put(url, data=json.dumps(data), timeout=3)
        return data