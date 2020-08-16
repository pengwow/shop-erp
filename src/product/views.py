from django.shortcuts import render
from django.http import JsonResponse
import requests
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
# Create your views here.

def get_1688_product_info(request):
    # response = requests.get('https://detail.1688.com/offer/622920688999.html?spm=a260j.12536015.jr601u7p.1.54f4700egKDWeZ')
    # print(response.text)
    driver=webdriver.Chrome()
    WebDriverWait(driver,10)
    driver.get('https://detail.1688.com/offer/622920688999.html?spm=a260j.12536015.jr601u7p.1.54f4700egKDWeZ')
    driver.close()
    return JsonResponse({'d':''})
