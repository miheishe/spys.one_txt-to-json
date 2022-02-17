import json
import requests

class Reader:
    def __init__(self, link = "https://spys.me/proxy.txt", type = "http"):
        self.link = link
        self.type = type #can be http or socks
        self.list = "Run get method first"

    def get(self):
        self.list = requests.get(self.link).text.split('\n')[6:] #not flexible, but simple



    # IP address:Port CountryCode-Anonymity(Noa/Anm/Hia)-SSL_support(S)-Google_passed(+)
    # 118.70.12.171:53281 VN-H +
    # 190.110.111.153:999 CL-N! -
    # 95.0.219.234:8080 TR-N -
    # 185.104.252.10:9090 LB-H -
    # 95.66.142.11:8080 RU-N +
    # 201.249.161.51:999 VE-A-S! -
    # 191.97.9.189:999 CO-N! -
    def get_list(self, country="all", anonymity="all", ssl="all", google_passed = "all"):
        pass

def run():
    a = Reader()
    a.get()
    print(a.list)



if __name__ == "__main__":
    run()

