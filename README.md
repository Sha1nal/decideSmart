# CS50 Final Project: DecideSmart

## Video Demo:  <URL HERE>

## Project Description: 
DecideSmart is your personal decision journal. The aim and purpose of DecideSmart is to allow you to think about your decisions before you make them. 

The DecideSmart application consists of a form with multiple questions probing you about a decision you are about to make. Once you fill out the form the decision will be logged in the database and over time your decsions history will build up. 

There is an analytics page that analyses the history of all your decisons and provides you with feedback and insigts as to how you have been making your decisions over time. This allows you to analyse your your mind and effectively alter the way you make decisions.

## Approach and Technologies:
I used a tutorial called "The Flask Mega Tutorial" to help guide me through the process of using best web practices to build a web application using Flask.
I also used multiple other resources to assist me with creating a visually appealing, secure, fast web application.

Technologies used:
Refer to requirements.txt

## Project Files and Application Structure:
1. rationale.py
2. config.py
3. app
    1. init.py
    2. forms.py
    3. models.py
    4. routes.py
    5. analytic_helpers.py
    6. templates
        1. base.html
        2. signup.html
        3. login.html
        4. index.html
        5. decisions.html
        6. history.html
        7. analytics.html
    7. static
        1. css
            1. style.css
4. migrations

## Project File Descriptions:
#### 1. rationale.py
This is the entry point for flask into the DecideSmart application. 

#### 2. config.py
To set up the configurations for Flask I created a separate file for segregation purposes. I then used a class to build the configurtaions into. This Class is then instantiated in 3.1 init.py. 

#### 3. app
This folder contains the application files and is where the application gets initiated and run.

####   3.1. init.py
####   3.2. forms.py
####   3.3. models.py
####   3.4. routes.py
####   3.5. analytic_helpers.py
####   3.6. templates
####        3.6.1. base.html
####        3.6.2. signup.html
####        3.6.3. login.html
####        3.6.4. index.html
####        3.6.5. decisions.html
####        3.6.6. history.html
####        3.6.7. analytics.html
####   3.7. static
####       3.7.1. css
####           3.7.1.1. style.css
#### 4. migrations