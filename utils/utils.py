import json
from urllib.request import urlopen
from bs4 import BeautifulSoup

def get_identity_key():
    try:
        with open("/root/NodesBot/utils/gateways.txt") as file:
            key = file.readlines()
        return key
    except IOError as e:
        print("Error:", e)
        return "Not found"


def get_size_gateways():
    keys =  get_identity_key()
    return (len(keys))

def get_data():
    try:
        info = urlopen("https://validator.nymtech.net/api/v1/gateways/described")
        data = json.loads(str(BeautifulSoup(info, 'html.parser')))
        return data
    except:
        print("Error: Data Invalid")
        return None

def get_host_by_identity_key(data, identity_key):
    for item in data:
        if item["bond"]["gateway"]["identity_key"] == identity_key:
            return item["bond"]["gateway"]["host"]
    return "Not Found"

def get_all_host_by_identity_key(data, identity_key):
    for item in data:
        if item["bond"]["gateway"]["identity_key"] == identity_key:
            return write_host(identity_key, item["bond"]["gateway"]["host"])
    return write_host(identity_key, None)


def write_host(identity_key, value):
    file = open("/root/NodesBot/utils/hosts.txt", 'a')
    if (value):
        file.write(identity_key)
        file.write(" : " + str(value) + "\n")
    else:
        file.write(identity_key)
        file.write(" : Host not found\n")


def create_list_hosts(size):
    i = 0
    while (i < size):
        get_all_host_by_identity_key(get_data(), get_identity_key()[i].strip())
        i = i + 1