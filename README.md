**Student Registration System**

Overview

The Student Registration System is a web-based application built using Django. It allows students to register, enroll in courses, and manage payments using Stripe. Administrators can oversee student activities and course management through a secure admin panel.

Features

•	User Registration & Authentication: Secure signup, login, and logout functionality.
•	Course Management: Students can browse and enroll in courses.
•	Payment Integration: Supports Stripe for handling course payments.
•	Admin Dashboard: Administrators can manage users, courses, and payments.
•	Secure & Scalable: Built with Django's authentication and security best practices.

Installation

Prerequisites

•	Python 3.x
•	Django
•	SQLite (default) or another database
•	Stripe API Key (for payment processing)

Setup

1.	Clone the repository: 
      git clone https://github.com/kua-University/samuelg_student_registration_project.git
2.	cd samuelg_student_registration_project
3.	Create a virtual environment and activate it: 
  	python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
4.	Install dependencies: 
  	pip install -r requirements.txt
5.	Apply migrations: 
   	python manage.py migrate
6.	Create a superuser (admin): 
    python manage.py createsuperuser
7.	Run the development server: 
   	python manage.py runserver
8.	Access the app at: http://127.0.0.1:8000

Testing

Run unit tests with:
python manage.py test

Deployment

You can deploy the project on PythonAnywhere, Heroku, or any cloud service supporting Django.

Contributing

1.	Fork the repository.
2.	Create a feature branch (git checkout -b feature-branch).
3.	Commit changes (git commit -m "Your message").
4.	Push to GitHub (git push origin feature-branch).
5.	Create a Pull Request.

Contact

For questions or contributions, reach out via GitHub.

