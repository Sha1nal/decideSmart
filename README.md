# CS50 Final Project: DecideSmart

## Project Description: 
DecideSmart is your personal decision journal. The aim and purpose of DecideSmart is to allow you to think about your decisions before you make them.

The DecideSmart application consists of a form with multiple questions probing you about a decision you are about to make. Once you fill out the form, the decision will be logged in the database, and over time, your decision history will build up.

There is an analytics page that analyses the history of all your decisions and provides you with feedback and insights as to how you have been making your decisions over time. This allows you to analyze your thought process and effectively alter the way you make decisions.

## How to Use the Application: 
1. Register a new account on the Sign-Up page.
2. Log in.
3. Log a new decision on the Make a Decision page.
4. Review the analysis of your decision on the analysis page.
5. Review your decision history on the history page.

## Approach and Technologies:
I used a tutorial called "The Flask Mega Tutorial" to help guide me through the process of using best web practices to build a web application using Flask. I also utilized multiple other resources to assist me in creating a visually appealing, secure, and fast web application.

Technologies used:
(Refer to requirements.txt for a detailed list)

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

## Project File Descriptions:
#### 1. rationale.py
This is the entry point for Flask into the DecideSmart application.

#### 2. config.py
To set up the configurations for Flask, I created a separate file for segregation purposes. I then used a class to encapsulate the configurations. This class is then instantiated in init.py.

#### 3. app
This folder contains the application files and is where the application gets initiated and run.

####   3.1. init.py
This file initializes the Flask application and dependent technologies.

####   3.2. forms.py
This file is a set of classes that contains each of the forms within the app. There is a class for:
- Login form
- Sign up form
- Decision form
Each of these classes will be instantiated as an object in the routes.py file and then passed into the template.

####   3.3. models.py
This file contains the database models. It is used to manage updates to the database structure. I chose this method of working with databases as it simplifies updates to tables. There are two models:
- User
- Decision
Each of these classes represents a table in the database.

####   3.4. routes.py
This file manages user authentication, sign-ups, logins, and logouts. It allows users to make and record decisions, view their decision history, and analyze these decisions. The application uses forms for data input, interacts with a database to store user and decision data, and employs Flask-Login for session management. Each route in the script corresponds to a different page or functionality of the web application, rendering appropriate HTML templates based on user actions and inputs.

####   3.5. analytic_helpers.py
This file defines a class Analytics, which is used to analyze a set of decision data. The class:
1. Takes a decision set as input and converts it into a pandas DataFrame.
2. Provides various analytical methods to calculate statistics such as average confidence, impulsiveness, and backup plan availability in decisions.
3. Calculates the average confidence scale, the mean time between decision logging and execution, and identifies days with the highest number of confident and impulsive decisions.
4. Also identifies the most confident decisions based on a confidence scale threshold.
Initially I did consider using SQL to perform the analysis but I was interested in learning about Pandas and saw it as a good opportunity to utalise it in my code.

####   3.6. templates
The templates folder is used to store HTML files that define the structure and layout of web pages in the application.

####        3.6.1. base.html
This is the base template of the application that contains the styling sheets and footer.

####        3.6.2. signup.html
This is the signup form template.

####        3.6.3. login.html
This is the log in template.

####        3.6.4. index.html
This is the home page of the application with details about the application.

####        3.6.5. decisions.html
This is the decision form which allows a user to input a decision.

####        3.6.6. history.html
This template displays a historical list of the users decisions.

####        3.6.7. analytics.html
This template displays the analysis of the users decisions.

####   3.7. static
####       3.7.1. css
####           3.7.1.1. style.css
The applications styling is in here. 

## Video Demo:  
https://youtu.be/x3eRjHpjqRY