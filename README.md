# bank_deposits
Code related to midterm project in Machine Learning Zoomcamp


Data Set Information:

The data is related with direct marketing campaigns of a Portuguese banking institution. The marketing campaigns were based on phone calls. Often, more than one contact to the same client was required, in order to access if the product (bank term deposit) would be ('yes') or not ('no') subscribed.

## The classification goal is to predict if the client will subscribe (yes/no) a term deposit (variable y).





## Repo contains:

* readme.md

* notebook.ipynb

* script train.py 
* script predict.py
* pipenv, pipenv.lock
       
  Instructions (if you have pipenv, docker, awsb installed (as you are in progress in zoomcamp-course a think you have :) )  please skip installation procedure:
       
  1) install pipenv 
       
              pip install pipenv
       
  2) Within the directory which contains files: pipenv, pipenv.lock 
              
              pipenv install 
       
  3) Run virtual environment shell
       
              pipenv shell 
        
  4) Then you can deploy the model with flask, using gunicorn
        
              gunicorn --bind 0.0.0.0:9696 predict:app


* Dockerfile
  
   Instalation - debian (I didn't test it in Windows):
  
   1) Install docker
        
              sudo apt-get install docker.io
              
   2) If service is not running: 
  
              sudo service docker run
        
   3) Build docker file: 
 
              sudo docker build -t mterm_project .
        
   4) Run the file: 
 
               sudo docker run -it --rm -p 9696:9696 mterm_project:latest
   
   5) You can test if it works using described below file

* depo_client_score.py

    Test the model using depo_client_score.py: python depo_client_score.py
    
* depo_client_score_ebs.py

    As the model is also availablea on AWS beanstalk you can test it using depo_client_score_ebs.py.
    I deployed model according to below listed code:
       
       eb init -p docker -r eu-central-1 mterm_project
    Deploy model it locally (for testeng):   
       
       eb local run --port 9696
       
    Deploy in AWS Elasticbeanstalk:
    
       eb create mterm-project-env
       
    





Attribute Information:

Input variables:
### bank client data:
1 - age (numeric)
2 - job : type of job (categorical: 'admin.','blue-collar','entrepreneur','housemaid','management','retired','self-employed','services','student','technician','unemployed','unknown')
3 - marital : marital status (categorical: 'divorced','married','single','unknown'; note: 'divorced' means divorced or widowed)
4 - education (categorical: 'basic.4y','basic.6y','basic.9y','high.school','illiterate','professional.course','university.degree','unknown')
5 - default: has credit in default? (categorical: 'no','yes','unknown')
6 - housing: has housing loan? (categorical: 'no','yes','unknown')
7 - loan: has personal loan? (categorical: 'no','yes','unknown')
### related with the last contact of the current campaign:
8 - contact: contact communication type (categorical: 'cellular','telephone')
9 - month: last contact month of year (categorical: 'jan', 'feb', 'mar', ..., 'nov', 'dec')
10 - day_of_week: last contact day of the week (categorical: 'mon','tue','wed','thu','fri')
11 - duration: last contact duration, in seconds (numeric). Important note: this attribute highly affects the output target (e.g., if duration=0 then y='no'). Yet, the duration is not known before a call is performed. Also, after the end of the call y is obviously known. Thus, this input should only be included for benchmark purposes and should be discarded if the intention is to have a realistic predictive model.
### other attributes:
12 - campaign: number of contacts performed during this campaign and for this client (numeric, includes last contact)
13 - pdays: number of days that passed by after the client was last contacted from a previous campaign (numeric; 999 means client was not previously contacted)
14 - previous: number of contacts performed before this campaign and for this client (numeric)
15 - poutcome: outcome of the previous marketing campaign (categorical: 'failure','nonexistent','success')
### social and economic context attributes
16 - emp.var.rate: employment variation rate - quarterly indicator (numeric)
17 - cons.price.idx: consumer price index - monthly indicator (numeric)
18 - cons.conf.idx: consumer confidence index - monthly indicator (numeric)
19 - euribor3m: euribor 3 month rate - daily indicator (numeric)
20 - nr.employed: number of employees - quarterly indicator (numeric)

### Output variable (desired target):
21 - y - has the client subscribed a term deposit? (binary: 'yes','no')






