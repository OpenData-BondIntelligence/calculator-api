# calculator-api
This project contains API for performing basic calculations - add, subtract, multiply
and divide using a python flask app. 

# Getting Started

## Development
Clone the repo from git hub using,

    git clone https://github.com/rohitamale18/calculator-api.git

Create a Python Virtual Env and activate it,

    python -m virtualenv /path/to/venv
    path/to/venv> Scripts/activate.bat

Install required packages,

    path/to/calculator-api/web>pip install -r requirements.txt

# Running the Project
After following the steps mentioned previously, keeping the virtual environment
activated use the following commands to interact with api,

## Run the API,
    (virtualenv)path/to/calculator-api/web> python app.py

## Interacting with API,

There are multiple ways to interact with the API, you can either use postman,
curl commands or a web browser. The idea behind each of them is same. Given below
is a list of request pages of the API. If using a browser, copy and paste the
URL below directly. If using shell, prefix the URLs below with 'CURL '. 

* Home - Shows the most recent calculation: http://0.0.0.0:5000/  
* Show most recent 10 calculations: http://0.0.0.0:5000/recentresults
* Show all calculations: http://0.0.0.0:5000/allresults
* Perform calculation (more details below): http://0.0.0.0:5000/operate?operation=x*y

## Performing Calculation:
The API can be used to perform 4 basic operations: add, subtract, multiply and divide.
Below is how to use each functionality using curl commands,

Addition:
Only for addition, you may need to use '%2b' instead of a '+' sign

    CURL -X GET http://0.0.0.0:5000/operate?operation=10%2b10

Subtraction, Division and Multiplication: 

    CURL -X GET http://0.0.0.0:5000/operate?operation=10-10
    CURL -X GET http://0.0.0.0:5000/operate?operation=10/10
    CURL -X GET http://0.0.0.0:5000/operate?operation=10*10

# Deployment
Deploy the API (for example to AWS EC2 instance) using the Dockerfile within 
this project. Commands for a successful deployment,

    path/to/calculator-api/web> docker build -t calculator-api .
    path/to/calculator-api/web> docker run -p 5000:5000 calculator-api 
    
# Developer
* [Rohit Amale] (mailto:rohitamale@gmail.com)