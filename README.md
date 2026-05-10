# wsaa-project
by Zoe McNamara Harlowe

# Irish Vocabulary Web Application

### Welcome to my project submission for the Web Services and Applications module. This module is provided by ATU (Atlantic Technological University) as part of the HDip in Computing in Data Analytics.

For this project, I created a simple Flask web application for storing, managing, and testing Irish–English vocabulary.  
Users can add, edit, delete, search, and quiz themselves on random Irish words.  
Built with Flask, SQLite, Bootstrap, and JavaScript.

---

## Features

- Add new Irish–English word pairs  
- View all stored words in a clean Bootstrap table  
- Inline editing for updates  
- Delete entries instantly  
- Live search bar  
- “Test Yourself” quiz mode (guess the English translation of a random Irish word)  
- Fully deployed on PythonAnywhere  

---

## Project Structure

wsaa_project/
│
├── app.py               # Main Flask application
├── words.html           # CRUD interface
├── test.html            # Quiz page
├── words.db             # SQLite database
├── createdb.py          # Database initialisation script
├── requirements.txt     # Python dependencies
└── README.md            # Documentation

---

## Accessing the Web Application
The site is currently live at:
```bash
https://zoeharlowe.pythonanywhere.com/
```

I deployed it to PythonAnywhere using the following steps:

### 1. Create an account and create new Web App called wsaa_project.
Upload project files to: /home/zoeharlowe/wsaa_project

### 2. Ensure WSGI configuration is as follows:
```bash
import sys
import os

path = '/home/zoeharlowe/wsaa_project'
if path not in sys.path:
    sys.path.append(path)

os.chdir(path)

from app import app as application
```
### 3. Reload web app
The site will be live at [zoeharlowe.pythonanywhere.com](https://zoeharlowe.pythonanywhere.com/)

---

## Running Locally

### 1. Clone the repository and change directory to the repo
```bash
git clone https://github.com/zoeharlowe/wsaa_project.git
cd wsaa_project
```
### 2. Install dependencies
```bash
pip install -r requirements.txt
```
### 3. Create the database
```
python createdb.py
```
### 4. Run the Flask app
```bash
python app.py
```
### 5. Open in browser
```bash
http://127.0.0.1:5000/
```

### Technologies 
- Python 3.12
- Flask
- SQLite
- Bootstrap 5
- JavaScript
- HTML
- PythonAnywhere

### Libraries & Packages
- flask: https://flask.palletsprojects.com/en/stable/quickstart/
- sqlite3: https://docs.python.org/3/library/sqlite3.html
- os: https://docs.python.org/3/library/os.html
- random: https://docs.python.org/3/library/random.html

### Author
Zoe McNamara Harlowe
G00473469
Higher Diploma in Computing in Data Analytics
Atlantic Technological University (ATU)