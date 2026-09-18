# Django Blog App 📝

A full-stack blog application built with Django as part of my self-taught backend development journey. This project is open to contributors of all levels — especially beginners!

## 🌟 About This Project

This is a multi-user blog platform where users can create accounts, write blog posts, edit their own content, and search for posts. Built with Python and Django.

## ✨ Features

- User authentication (signup, login, logout)
- Create, edit, and delete blog posts
- Post ownership — users can only edit their own posts
- Search posts by title and content
- Responsive design with Bootstrap

## 🛠️ Tech Stack

- **Backend:** Python 3, Django
- **Database:** SQLite (development)
- **Frontend:** HTML, CSS, Bootstrap

## 🚀 Getting Started

### Prerequisites

Make sure you have these installed:
- Python 3.8 or higher
- pip (comes with Python)
- Git

### Installation

**1. Clone the repository**
```bash
git clone https://github.com/Kcee5091/django-blog.git
cd django-blog
```

**2. Create a virtual environment**
```bash
python3 -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Set up the database**
```bash
python manage.py migrate
```

**5. Create an admin account**
```bash
python manage.py createsuperuser
```

**6. Run the development server**
```bash
python manage.py runserver
```

**7. Visit the app**
http://127.0.0.1:8000/


That's it! You should see the blog homepage.

## 🤝 Contributing

Contributions are welcome — especially from beginners! Here's how:

**1. Fork the repository**
Click the "Fork" button at the top right of this page.

**2. Clone your fork**
```bash
git clone https://github.com/YOUR-USERNAME/django-blog.git
cd django-blog
```

**3. Create a new branch**
```bash
git checkout -b feature/your-feature-name
```

**4. Make your changes**
Follow the setup steps above to run the project locally.

**5. Commit your changes**
```bash
git add .
git commit -m "Add: description of what you changed"
git push origin feature/your-feature-name
```

**6. Open a Pull Request**
Go to the original repo and click "New Pull Request".

