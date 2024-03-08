import re

def validate_ip(ip: str):
    ip_regex = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
    if not ip_regex.match(ip):
        return False
    return True