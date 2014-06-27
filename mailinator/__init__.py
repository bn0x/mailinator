import requests

class Mailinator(object):
    def __init__(self, api_key="", *args, **kwargs):
        self.session = requests.session()
        self.endpoint = []
        self.apiKey = api_key

    def __getattr__(self, thing):
        self.endpoint.append(thing)
        return self

    def __call__(self, *args, **kwargs):
        endpoint = "/".join(["https://api.mailinator.com/api"] + self.endpoint)
        self.endpoint = []
        return self.request(endpoint, *args, **kwargs)

    def request(self, endpoint, *args, **kwargs):
        kwargs.setdefault("token", self.apiKey)
        request = self.session.get(endpoint, params=kwargs)
        return request.json()

if __name__ == "__main__":
    print("You don't run this..")