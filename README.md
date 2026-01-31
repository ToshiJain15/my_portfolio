# Personal Portfolio

A production-ready personal portfolio website built with Django and MySQL.

## 🧱 Tech Stack
- **Backend:** Django 6.0
- **Database:** MySQL
- **Frontend:** HTML5, CSS3, JavaScript, Bootstrap 5
- **Styling:** Custom CSS with Glassmorphism and Animations

## 🚀 Setup Instructions

### 1. Prerequisites
- Python 3.10+
- MySQL Server

### 2. Environment Setup

1.  **Clone or navigate to the project directory.**
2.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate  # Windows
    # source venv/bin/activate  # Mac/Linux
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### 3. Database Configuration

1.  **Create a MySQL Database:**
    Open your MySQL client (Workbench, Command Line, etc.) and run:
    ```sql
    CREATE DATABASE portfolio CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
    ```
2.  **Configure Environment Variables:**
    - The project uses a `.env` file for configuration.
    - Open `.env` and update the following values to match your MySQL setup:
      ```ini
      DB_NAME=portfolio
      DB_USER=root      # Your MySQL username
      DB_PASSWORD=password # Your MySQL password
      DB_HOST=localhost
      DB_PORT=3306
      ```

### 4. Initialize the Project

1.  **Run Migrations:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
2.  **Create a Superuser (for Admin access):**
    ```bash
    python manage.py createsuperuser
    ```
3.  **Collect Static Files (Optional for dev, needed for prod):**
    ```bash
    python manage.py collectstatic
    ```

### 5. Load Initial Data (Optional)

After applying migrations, you can populate the database with resume data:
```bash
python manage.py load_portfolio_data
```

### 6. Run the Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` to view the site.
Access the Admin panel at `http://127.0.0.1:8000/admin` to add Projects, Skills, and Experience.

## 📂 Project Structure
```
portfolio/
├── main/                 # Django App
│   ├── models.py         # DB Models (Project, Skill, Experience, Contact)
│   ├── views.py          # View Logic
│   ├── urls.py           # App URLs
│   ├── templates/main/   # App Templates
├── portfolio/            # Project Configuration
│   ├── settings.py       # Settings (MySQL, Env Vars)
│   ├── urls.py           # Main URLs
├── static/               # CSS, JS, Images
├── templates/            # Base templates
├── .env                  # Environment Variables
├── requirements.txt      # Dependencies
└── manage.py             # Django Manager
```

## 🎨 Features
- **Responsive Design:** Looks great on mobile and desktop.
- **Dynamic Content:** Manage projects and skills via Django Admin.
- **Contact Form:** Saves messages to the database.
- **Modern UI:** Smooth animations, gradients, and clean layout.
