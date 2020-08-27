class Hue():
    def __init__(self, ip, username):
        self.ip = ip
        self.username = username
    
    def get(self)
        """
        Get the light information from the bridge
        """
        data = ''
        url = "http://" + self.ip + "/api/" + self.username + "/lights"
        response = requests.post(url, data = json.dumps(data))

