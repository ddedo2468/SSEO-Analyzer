## SSEO-Analyzer - Web App for SEO Analysis

This README.md file provides an overview of the SSEO-Analyzer web application, a Flask-based SEO analyzer built with Python.

**Features:**

* Analyzes a user-provided URL for SEO best practices.
* Checks for elements like title presence, length, meta description, H1 tag presence and order, image alt text, and keyword usage.
* Saves analysis results in a user-specific search history for future reference.
* User registration, login, and logout functionalities.

**Technologies:**

* Flask web framework
* Python programming language
* Flask-SQLAlchemy for database interactions
* HTML for structuring content
* CSS for styling
* Jinja templating engine

**Project Structure:**

```
SSEO-Analyzer/
├── app/
│   ├── __init__.py         (file to initialize the app package)
│   ├── models.py           (Defines database models, for users and search history)
│   ├── views.py            (Handles user interactions like login, analysis, and history)
│   ├── utils.py            (Contains utility functions used in the app)
│   └── templates/
│       ├── base.html        (Base template for all app pages)
│       └── ...               (Other HTML templates for specific functionalities)
├── config.py               (Configuration file for app settings)
├── run.py                   (Script to start the web application)
└── static/
    ├── css/
    └── img/
|__requirements.txt
|__english

```

**Using the Web App:**

1. **Sign Up:** Create a new user account. Upon successful signup, you'll be automatically logged in.
2. **Analyze a URL:** Go to the analyzer page (likely accessible from the navbar).
3. **Enter URL:** Paste the URL you want to analyze into the designated input field.
4. **Click Analyze:** The app will analyze the URL and redirect you to the results page.
5. **View Results:** The results page will display information about the analyzed elements and potential SEO improvements.
6. **Access Search History:** Click on the "History" tab in the navbar to view your past URL analyses with timestamps.

**Note:** When analyzing the same URL again, the search history will be updated with the latest analysis results.

**License:**

This project is licensed under [License Name] (replace with the actual license used).

**Authors**
Aya Tarek - aya.tarek213@icloud.com
Abdullah Musbah - abdallahmosbah25@gmail.com
