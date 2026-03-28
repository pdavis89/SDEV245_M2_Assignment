
from flask import Flask, render_template, request, redirect, session, abort

app = Flask(__name__)
app.secret_key = "supersecretkey"  # required for sessions

# Fake user "database"
USERS = {
    "alice": {"password": "password123", "role": "admin"},
    "bob": {"password": "mypassword", "role": "user"}
}

@app.route("/") # Home page, shows login form
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])   # Login route to handle user authentication
def login():
    if request.method == "POST":    # Process login form submission
        username = request.form["username"]
        password = request.form["password"]

        user = USERS.get(username)  # Check if user exists in the fake database

        if user and user["password"] == password:   # If credentials are correct, store user info in session and redirect to dashboard
            session["username"] = username
            session["role"] = user["role"]
            return redirect("/dashboard")   # Redirect to dashboard after successful login

        return "Invalid credentials"    # Return error message if login fails

    return render_template("login.html")    # Render login form for GET requests

def login_required(f):  # Decorator to ensure user is logged in
    def wrapper(*args, **kwargs):
        if "username" not in session:
            return redirect("/")
        return f(*args, **kwargs)
    wrapper.__name__ = f.__name__
    return wrapper


def role_required(role):    # Decorator to ensure user has specific role
    def decorator(f):
        def wrapper(*args, **kwargs):   # Check if user has the required role
            if "role" not in session or session["role"] != role:
                abort(403)  # Forbidden
            return f(*args, **kwargs)   # Call the original function if role is correct
        wrapper.__name__ = f.__name__   # Preserve original function name for Flask routing
        return wrapper
    return decorator

@app.route("/dashboard")    # Dashboard page, requires login
@login_required
def dashboard():    # Render dashboard with user info from session
    return render_template("dashboard.html", user=session["username"], role=session["role"])

@app.route("/admin")    # Admin page, requires user to be logged in and have "admin" role
@login_required
@role_required("admin")
def admin_page():   # Render admin page with user info from session
    return render_template("admin.html", user=session["username"])

@app.route("/logout")   # Logout route to clear session and redirect to login page
def logout():
    session.clear()
    return redirect("/")

if __name__ == "__main__":    app.run(debug=True)  # Uncomment this line to run the app directly
