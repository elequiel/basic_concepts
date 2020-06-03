import requests

def get_site(url):
    req = requests.get(url)
    return req

def test_req_ok():
    url = "https://google.com.br"
    cod = get_site(url)
    
    assert cod.status_code == 200

def test_req_failed():
    url = "http://devzek.com"
    cod = get_site(url)

    assert cod.status_code == 404
