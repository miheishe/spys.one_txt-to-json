import requests

ANONYMITY_CASE = {'N': 'Not anonymous', 'A': 'Anonymous', 'H': 'High anonymous'}
GOOGLE_PASS_CASE = {'+': True, '-': False}
PROXY_TYPE_CASE = {'http': 'https://spys.me/proxy.txt', 'socks': 'https://spys.me/socks.txt'}


class Proxy:
    def __init__(self, ip, port, https, another_exit_ip, country, anonymity, google_pass):
        self.ip = ip
        self.port = port
        self.https = https
        self.another_exit_ip = another_exit_ip
        self.country = country
        self.anonymity = anonymity
        self.google_pass = google_pass
        self.check_pass = False

    def check(self):
        result_before = requests.get('https://api.myip.com').json()['ip']
        proxy = {self.https: f'{self.ip}:{self.port}'}
        try:
            result = requests.get('https://api.myip.com', proxies=proxy, timeout=5).json()['ip']
        except Exception:
            pass
        else:
            if (result_before != result):
                self.check_pass = True
            else:
                self.check_pass = False
        finally:
            return self


class Reader:
    def __init__(self, proxy_type="http"):
        self.link = PROXY_TYPE_CASE[proxy_type]
        self.proxy_type = proxy_type  # can be http or socks
        self.proxies_list = "Run 'get_all_proxies' method first"
        self.working_proxies = []

    def countryname(self, country_code):
        # todo https://spys.one/en/proxy-by-country/
        # return country
        pass

    def get_all_proxies(self):
        self.proxies_list = []  # List of proxies objects
        raw_data = requests.get(self.link).text.split('\n')[6:-2]  # not flexible, but simple
        for i in raw_data:
            stripped_data = i.rstrip().split(' ')
            ip = stripped_data[0].split(':')[0]
            port = stripped_data[0].split(':')[1]
            google_pass = None if len(stripped_data) <= 2 else GOOGLE_PASS_CASE[stripped_data[-1]]
            another_exit_ip = True if len(stripped_data[1].split('!')) > 1 else False
            parameters = stripped_data[1].split('!')[0].split('-')
            country = parameters[0]
            anonymity = ANONYMITY_CASE[parameters[1]]
            https = 'http' if len(parameters) < 3 else 'https'
            self.proxies_list.append(
                Proxy(ip=ip,
                      port=port,
                      https=https,
                      another_exit_ip=another_exit_ip,
                      country=country,
                      anonymity=anonymity,
                      google_pass=google_pass
                      ))

    def get_list(self, country="all", anonymity="all", ssl="all", google_passed="all"):
        if type(self.proxies_list) == type('string'): print("Run 'get_all_proxies' method first")

    def check_all(self):
        count = 0
        self.checked_proxies = []
        for proxy in self.proxies_list:
            print(f'{count}/{len(self.proxies_list)}')
            self.checked_proxies.append(proxy.check())
            count += 1


def run():
    a = Reader()
    a.get_all_proxies()
    a.check_all()
    print(a.working_proxies)
    for i in a.checked_proxies:
        print (i.https, i.ip, i.port, i.check_pass)
    # a.proxies_list[0].check()


if __name__ == "__main__":
    run()
