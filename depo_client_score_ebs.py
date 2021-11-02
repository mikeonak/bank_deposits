#!/usr/bin/env python
# coding: utf-8


import requests


url = "http://mterm-project-env.eba-muzvifym.eu-central-1.elasticbeanstalk.com/predict"
customer = {"age": 30,
 "job": "technician",
 "marital": "single",
 "education": "university.degree",
 "default": "no",
 "housing": "no",
 "loan": "no",
 "contact": "telephone",
 "month": "oct",
 "day_of_week": "wed",
 "campaign": 1,
 "pdays": 999,
 "previous": 0,
 "poutcome": "nonexistent",
 "emp_var_rate": -0.1,
 "cons_price_idx": 93.798,
 "cons_conf_idx": -40.4,
 "euribor3m": 4.936,
 "nr_employed": 5195.8}


print(requests.post(url, json=customer).json())

