import requests
from bs4 import BeautifulSoup

target_url = "http://127.0.0.1:8888/"
r = requests.get(target_url)
soup = BeautifulSoup(r.text)
title=soup.find("title")


def test_namenull():
    assert title.text !="" 
    
def test_name():
    assert title.text =="Polyspector" 




