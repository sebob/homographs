import requests
import socket


class Domain:
    @staticmethod
    def check_hopp(domain):
        result = []
        try:
            response = requests.get('https://'+domain)
            for resp in response.history:
                result.append(resp.status_code)
                result.append(resp.is_redirect)
                result.append(resp.is_permanent_redirect)
                result.append(resp.url)
            return result
        except Exception as e:
            return None

    @staticmethod
    def check_ip(domain):
        try:
            hostname, aliases, addresses = socket.gethostbyname_ex(domain)
            return addresses
        except socket.gaierror as e:
            return None