import requests

try:
    with requests.get("https://hub.getdbt.com", stream=True) as rsp:
        ip, port = rsp.raw._connection.sock.getpeername()
        print(ip, port)
except:
    print("!except!!")
    with requests.get("http://hub.getdbt.com", stream=True, verify=False) as rsp:
        ip, port = rsp.raw._connection.sock.getpeername()
        print(ip, port)