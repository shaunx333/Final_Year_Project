import os
import re
from urllib.parse import urlparse

import joblib
from django.http import JsonResponse
from django.shortcuts import render

# 1.Checks for IP address in URL (Have_IP)
from untitled1 import settings


# 1.Checks for IP address in URL (Have_IP)
def havingIP(url):
    match = re.search(
        '(([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\/)|'
        '((0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})/)'
        '(?:[a-fA-F0-9]{1,4}:){7}[a-fA-F0-9]{1,4}', url)

    if match:
        return 1
    else:
        return 0


# 2.Checks the presence of @ in URL (Have_At)
def haveAtSign(url):
    if "@" in url:
        at = 1
    else:
        at = 0
    return at


# #3.Finding the length of URL and categorizing (URL_Length)
# def getLength(url):
#     if len(url) < 54:
#         length = 0            
#     else:
#         length = 1  
#     return length


# 4.Finding the number of subdomains
def getSub_domains(url):
    if url.count(".") < 4:
        return 0
    else:
        return 1

    # 5.Checking for redirection '//' in the url (Redirection)


def redirection(url):
    if "//" in urlparse(url).path:
        return 1
    else:
        return 0

    # 6.Existence of “HTTPS” Token in the Domain Part of the URL (https_Domain)


def httpDomain(url):
    domain = urlparse(url).netloc
    if 'https' or 'http' in domain:
        return 1
    else:
        return 0


shortening_services = r"bit\.ly|goo\.gl|shorte\.st|go2l\.ink|x\.co|ow\.ly|t\.co|tinyurl|tr\.im|is\.gd|cli\.gs|" \
                      r"yfrog\.com|migre\.me|ff\.im|tiny\.cc|url4\.eu|twit\.ac|su\.pr|twurl\.nl|snipurl\.com|" \
                      r"short\.to|BudURL\.com|ping\.fm|post\.ly|Just\.as|bkite\.com|snipr\.com|fic\.kr|loopt\.us|" \
                      r"doiop\.com|short\.ie|kl\.am|wp\.me|rubyurl\.com|om\.ly|to\.ly|bit\.do|t\.co|lnkd\.in|db\.tt|" \
                      r"qr\.ae|adf\.ly|goo\.gl|bitly\.com|cur\.lv|tinyurl\.com|ow\.ly|bit\.ly|ity\.im|q\.gs|is\.gd|" \
                      r"po\.st|bc\.vc|twitthis\.com|u\.to|j\.mp|buzurl\.com|cutt\.us|u\.bb|yourls\.org|x\.co|" \
                      r"prettylinkpro\.com|scrnch\.me|filoops\.info|vzturl\.com|qr\.net|1url\.com|tweez\.me|v\.gd|" \
                      r"tr\.im|link\.zip\.net"


# 7. Checking for Shortening Services in URL (Tiny_URL)
def tinyURL(url):
    match = re.search(shortening_services, url)
    if match:
        return 1
    else:
        return 0


# 8.Checking for Prefix or Suffix Separated by (-) in the Domain (Prefix/Suffix)
def prefixSuffix(url):
    if '-' in urlparse(url).netloc:
        return 1
    else:
        return 0


def featureExtraction(url):
    features = []
    features.append(havingIP(url))
    features.append(haveAtSign(url))
    features.append(getSub_domains(url))
    features.append(redirection(url))
    features.append(httpDomain(url))
    features.append(tinyURL(url))
    features.append(prefixSuffix(url))
    return features


def index(request):
    return render(request, 'index.html')


def doNic(request):
    # feature = featureExtraction(request.POST.get("url"))
    url = request.POST.get("url")
    # url = "https://www.google.co.in/search?q=sss&sxsrf=AOaemvKUwXcboAKdOtqlkbdi8CSFObuTfA%3A1633613007710&source=hp&ei=z_ReYYelKM7j-gTB7o7YDg&iflsig=ALs-wAMAAAAAYV8C37MEnbbxXmET-KLRsI-EbxP2b2UE&ved=0ahUKEwjHyJbYsrjzAhXOsZ4KHUG3A-sQ4dUDCAc&uact=5&oq=sss&gs_lcp=Cgdnd3Mtd2l6EAMyCAgAEIAEELEDMggILhCABBCxAzIICAAQsQMQgwEyCAgAEIAEELEDMggIABCABBCxAzIICAAQgAQQsQMyBQgAEIAEMgUIABCABDIRCC4QgAQQsQMQgwEQxwEQrwEyCAgAEIAEELEDOgQIIxAnOgUIABCRAjoLCAAQgAQQsQMQgwE6EQguEIAEELEDEIMBEMcBENEDOgUILhCABFCjC1iGD2DHEWgAcAB4AIABpgGIAbkDkgEDMC4zmAEAoAEB&sclient=gws-wiz"
    feat = []
    feature = featureExtraction(url)
    feat.append(feature)
    ml = joblib.load(os.path.join(settings.BASE_DIR, 'RandomForrest_Model_report_demo.pkl'))
    predValue = ml.predict(feat)

    print("Analyzing page " + url)
    print(feat)
    print(predValue[0])
    if predValue[0] == 0:
        isvalid = True
    else:
        isvalid = False

    data = {"valid": isvalid}
    return JsonResponse(data)
