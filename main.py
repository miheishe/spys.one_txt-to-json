import requests

ANONYMITY_CASE = {'N': 'Not anonymous', 'A': 'Anonymous', 'H': 'High anonymous'}
GOOGLE_PASS_CASE = {'+': True, '-': False}
PROXY_TYPE_CASE = {'http':'https://spys.me/proxy.txt','socks':'https://spys.me/socks.txt'}


class Reader:
    def __init__(self, proxy_type="http"):
        self.link = PROXY_TYPE_CASE[proxy_type]
        self.proxy_type = proxy_type  # can be http or socks
        self.list = "Run get method first"

    def countryname(self, country_code):
        # todo https://spys.one/en/proxy-by-country/
        # return country
        pass

    def get(self):
        jsonlist = []
        self.list = requests.get(self.link).text.split('\n')[6:-2]  # not flexible, but simple
        for i in self.list:
            data = i.rstrip().split(' ')
            ip = data[0].split(':')[0]
            port = data[0].split(':')[1]
            google_pass = None if len(data) <= 2 else GOOGLE_PASS_CASE[data[-1]]
            another_exit_ip = True if len(data[1].split('!')) > 1 else False
            parameters = data[1].split('!')[0].split('-')
            country = parameters[0]
            anonymity = ANONYMITY_CASE[parameters[1]]
            https = False if len(parameters) < 3 else True
            jsonlist.append(
                dict(ip=ip,
                     port=port,
                     https=https,
                     another_exit_ip=another_exit_ip,
                     country=country,
                     anonymity=anonymity,
                     google_pass=google_pass
                     ))
        self.list = jsonlist


    def get_list(self, country="all", anonymity="all", ssl="all", google_passed="all"):
        pass


def run():
    a = Reader()
    a.get()
    print(a.list)


if __name__ == "__main__":
    run()
