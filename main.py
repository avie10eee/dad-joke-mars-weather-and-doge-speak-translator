from tkinter import N
from urllib import response
import requests
from requests import get
import json

ny = input("do you want to translate some thing y/n ")
if ny == "y":
    words = input("what would you like to translate to doge speak ")
    word = words.replace(" ", "%20")
    reponse = get('https://api.funtranslations.com/translate/doge.json?text=' + word)
    transl = json.loads(reponse.content.decode())
    print(transl["contents"]['translated'])


jy = input ("do you want a dad joke y/n ")
if jy == "y":
    respose = get("https://icanhazdadjoke.com/", headers={"Accept": "application/json"})
    joke = json.loads(respose.content.decode())
    print(joke["joke"])

yn = input("do you want know the mars weather y/n ")
if yn == "y":
    marsw = get ("https://api.nasa.gov/insight_weather/?api_key=XcdlNOSRAYU8OF96PKLLho7Ib7XwTO1V5EK1KeTe&feedtype=json&ver=1.0")
    print(json.loads(marsw.content.decode()))
