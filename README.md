# Flask RBAC Demo App

This is a simple Flask application that demonstrates user authentication and role-based access control (RBAC).  
Users can log in, view a dashboard, access admin-only pages depending on their assigned role, and logout which returns the user bck to the landing page. I ended up using render.com to produce my app since GitHub pages does not support python, etc. The URL for the working application is https://sdev245-m2-assignment.onrender.com.

## Default Users (test cases)
username: alice password: password123 role: admin
username: bob password: mypassword role: user

## Features

- User login with session-based authentication
- Role-based access control (admin vs. regular user)
- Protected routes using custom decorators
- Clean Bootstrap UI
- Ready for deployment on Render or other Python hosts

## Tech Stack

- Python
- Flask
- Gunicorn (for production)
- Bootstrap 5

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/yourrepo.git
cd yourrepo