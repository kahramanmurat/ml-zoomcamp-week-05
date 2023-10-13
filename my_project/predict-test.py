#!/usr/bin/env python
# coding: utf-8

import requests


url = "http://localhost:9696/predict"

customer = {"job": "unknown", "duration": 270, "poutcome": "failure"}


response = requests.post(url, json=customer).json()
print(response)

if response["churn"] == True:
    print("sending promo email to %s" % customer_id)
else:
    print("not sending promo email to %s" % customer_id)
