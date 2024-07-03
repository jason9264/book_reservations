# Book Reservation System

This project is an integrative Book Reservation System built with Django. It demonstrates how multiple scripting and coding languages can be used together to create a functional program.

## Technologies Used

- **Python**: Used for backend development with Django, including lists, functions, arrays, and dictionaries.
- **HTML/CSS**: Utilizes Bootstrap for styling and customizations to create a responsive and user-friendly interface.
- **PostgreSQL**: Designed and managed the database to store book and user information.
- **Django**: Web framework used to handle HTTP requests, manage database interactions, and render templates.

## Project Structure

### Root Directory

- **bookreservation/**: Main Django project directory.
  - **settings.py**: Contains configurations, including database settings for PostgreSQL.
  - **urls.py**: Defines URL routes for the project.
  - **wsgi.py** and **asgi.py**: Configuration for web servers.

- **reservation/**: Application for managing book reservations.
  - **admin.py**: Configures the admin interface.
  - **models.py**: Defines database models for books and reservations.
  - **views.py**: Handles HTTP requests and business logic.
  - **templates/reservation/**: HTML templates for different pages (e.g., `login.html`, `dashboard.html`).
  - **static/reservation/css/**: Custom CSS styles, including Bootstrap customizations.

- **migrations/**: Contains database migration files for setting up and updating the database schema.
- **db.sqlite3**: The default database file used during development.
- **manage.py**: Django's command-line utility for administrative tasks.

## Setup and Installation

1. **Clone the repository:**
   ```sh
   git clone <(https://github.com/jason9264/book_reservations.git)>
   cd book-reservation-system
   ```

2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Configure the database:**
   Update `settings.py` to configure PostgreSQL database settings.

4. **Run migrations:**
   ```sh
   python manage.py migrate
   ```

5. **Start the development server:**
   ```sh
   python manage.py runserver
   ```

6. **Access the application:**
   Open your browser and navigate to `http://127.0.0.1:8000`.

## Features

- **User Authentication**: Users can log in and out, and register for an account.
- **Book Management**: Admins can add, update, and delete book information.
- **Reservation System**: Users can reserve books, and admins can manage reservations.
- **Responsive Design**: Utilizes Bootstrap for a mobile-friendly interface.

## Summary

This project integrates Python, HTML, CSS, PostgreSQL, and Django to create a functional book reservation system. It demonstrates the use of various technologies to build a cohesive and interactive web application.
