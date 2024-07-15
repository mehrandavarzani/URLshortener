# Django URL Shortener
This is a simple URL shortener project built with Django. It allows users to shorten long URLs and access them through short, easily manageable links.

## Features
- Shorten long URLs.
- Redirect to original URLs using shortened links.
- Simple and intuitive web interface.
- Basic styling with Bootstrap.

## Requirements
- Python 3.x
- Django 3.x
- SQLite (default database)

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/urlshortener.git
   cd urlshortener
   
2. Create a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install dependencies:
   ```sh
   pip install -r requirements.txt

4. Apply migrations:
   ```sh
   python manage.py migrate

5. Run the development server:
   ```sh
   python manage.py runserver
6. Open your browser and go to http://127.0.0.1:8000/.
