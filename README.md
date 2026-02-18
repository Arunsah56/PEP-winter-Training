# PEP Winter Training

A comprehensive Django training project covering various aspects of Django web development from basics to advanced topics.

## Table of Contents

- [Project Overview](#project-overview)
- [Directory Structure](#directory-structure)
- [Getting Started](#getting-started)
- [Project Contents](#project-contents)
  - [Python Basics (Day-1 to Day-5)](#python-basics-day-1-to-day-5)
  - [Django Fundamentals (Day-6)](#django-fundamentals-day-6)
  - [Advanced Django (Day-24)](#advanced-django-day-24)
  - [Authentication](#authentication)
  - [REST API Development](#rest-api-development)
  - [Email Integration](#email-integration)
  - [Database Integration](#database-integration)
  - [Additional Projects](#additional-projects)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Projects](#running-the-projects)
- [Git Commands Reference](#git-commands-reference)

## Project Overview

This repository contains multiple Django projects and tutorials created during the PEP Winter Training program. It covers everything from Python basics to advanced Django concepts including authentication, REST APIs, email functionality, and more.

## Directory Structure

| Directory | Description |
|-----------|-------------|
| `Day-1/` to `Day-6/` | Daily training content - Python basics and Django fundamentals |
| `AUTH_PROJECT/` | Django authentication project with login/register functionality |
| `Basic/` | Basic HTML/CSS templates |
| `CW/` | Company Website - multi-app Django project |
| `DB-INTEGRATION/` | Database integration examples |
| `Django_Project/` | Django project template |
| `Django_rest_user/` | Django REST Framework user management |
| `DJANGO-EMAIL/` | Django email functionality |
| `djangotutorial/` | Django tutorial |
| `JINJA-DEMO/` | Jinja2 templating demo |
| `REST/` | Django REST Framework API |
| `SLUG_DEMO/` | Django slug functionality demo |
| `TAILWIND-PROJECT/` | Django with Tailwind CSS |
| `To_Do_app/` | Todo application |

## Project Contents

### Python Basics (Day-1 to Day-5)

- **Day-1**: Basic Python syntax, if/else statements, functions
- **Day-2**: String manipulation
- **Day-3**: Python data structures
- **Day-4**: Object-oriented programming (inheritance, dataclasses, access modifiers)
- **Day-5**: Advanced Python (leap year, pilling problem)

### Django Fundamentals (Day-6)

- Django project setup
- Creating Django apps
- URL routing
- Views and templates
- Models and database

### Advanced Django (Day-24)

- Automated email sending
- Contact forms
- Form validation
- Email settings configuration

### Authentication

- User registration
- User login/logout
- Dashboard protection
- Session management
- Middleware for authentication

### REST API Development

- Django REST Framework setup
- Serializers
- API views
- CRUD operations
- User authentication in APIs

### Email Integration

- SMTP configuration
- Sending emails
- Email templates

### Database Integration

- Database connections
- Raw SQL queries
- Database models

### Additional Projects

- **SLUG_DEMO**: URL slug functionality
- **TAILWIND-PROJECT**: Django with Tailwind CSS
- **To_Do_app**: Full-featured todo application

## Prerequisites

- Python 3.8 or higher
- Django 3.2+ 
- pip (Python package manager)
- Git

## Installation

1. Clone the repository:
   
```
bash
   git clone <repository-url>
   cd PEP-winter-Training
   
```

2. Create a virtual environment:
   
```
bash
   python -m venv venv
   
```

3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`
   
```
bash
   # For Windows
   venv\Scripts\activate
   
   # For Mac/Linux
   source venv/bin/activate
   
```

4. Install Django and dependencies:
   
```
bash
   pip install django
   pip install djangorestframework
   
```

## Running the Projects

1. Navigate to the project directory:
   
```
bash
   cd <project-name>
   
```

2. Run migrations:
   
```
bash
   python manage.py migrate
   
```

3. Create superuser (optional):
   
```
bash
   python manage.py createsuperuser
   
```

4. Start the development server:
   
```
bash
   python manage.py runserver
   
```

5. Open your browser and visit:
   
```
   http://127.0.0.1:8000/
   
```

## Git Commands Reference

### Initialize Git
```
bash
git init
```

### Check Status
```
bash
git status
```

### Stage Changes
```
bash
git add .
```

### Commit Changes
```
bash
git commit -m "Your message here"
```

### Push to GitHub
```
bash
git push -u origin main
```

### Create New Repository (via CLI)
```
bash
gh repo create
# Follow the prompts:
# - Repository name: PEP_WINTER_TRAINING
# - Description: Your description
# - Visibility: public
# - Add README: y
# - Add .gitignore: y
# - .gitignore template: Python
# - Add a license: N
```

## Contributing

Feel free to fork this repository and contribute by submitting pull requests.

## License

This project is for educational purposes.

## Author

PEP Winter Training Program

## Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Python Documentation](https://docs.python.org/)
