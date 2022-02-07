import requests
from bs4 import BeautifulSoup

target_url = "http://ec2-18-176-56-94.ap-northeast-1.compute.amazonaws.com:8888/"
r = requests.get(target_url)
soup = BeautifulSoup(r.text)
title=soup.find("title")


def test_namenull():
    assert title.text !="" 
    
def test_name():
    assert title.text =="Polyspector" 




