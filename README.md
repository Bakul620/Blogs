# Django Blog Project

A multi-app Django blog platform with public blog pages, user authentication, and a dashboard for managing categories and posts.

## Table of Contents

- [Project Overview](#project-overview)
- [Main Features](#main-features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [How to Run](#how-to-run)
- [URL Map](#url-map)
- [Useful Commands](#useful-commands)
- [Notes](#notes)

## Project Overview

This project is organized into separate Django apps:

- `blogs`: blog posts, categories, search, and blog detail pages.
- `about`: about content and social links.
- `dashboards`: dashboard pages for post/category CRUD operations.
- `blog_main`: project-level settings, root URLs, authentication views, and home page.

## Main Features

- Public home page with featured and latest published posts.
- Post detail page using slug-based URLs.
- Category-wise post listing.
- Search across title, description, and post body.
- User registration, login, and logout.
- Dashboard section for:
	- Category add/edit/delete
	- Post add/edit/delete
- Image upload support for blog posts.
- Shared sidebar data via context processors (categories and social links).

## Tech Stack

- Python 3
- Django 5.2.13
- SQLite (default database)
- django-crispy-forms + crispy-bootstrap4
- Pillow (image upload processing)

## Project Structure

```text
blog_main/
├── manage.py
├── db.sqlite3
├── requirements.txt
├── README.md
├── about/
│   ├── models.py
│   ├── views.py
│   ├── admin.py
│   ├── apps.py
│   ├── tests.py
│   └── migrations/
│       ├── __init__.py
│       ├── 0001_initial.py
│       └── 0002_sociallink.py
├── blogs/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── context_processors.py
│   ├── admin.py
│   ├── apps.py
│   ├── tests.py
│   └── migrations/
│       ├── __init__.py
│       ├── 0001_initial.py
│       ├── 0002_alter_categories_options_blog.py
│       └── 0003_alter_blog_status.py
├── dashboards/
│   ├── forms.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── migrations/
│       └── __init__.py
├── blog_main/
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   ├── form.py
│   ├── asgi.py
│   ├── wsgi.py
│   └── __init__.py
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── blog_detail.html
│   ├── post_by_category.html
│   ├── search.html
│   ├── register.html
│   ├── login.html
│   └── dashboard/
│       ├── dashboard.html
│       ├── sidebar.html
│       ├── categories.html
│       ├── add_category.html
│       ├── edit_category.html
│       ├── posts.html
│       ├── add_post.html
│       └── edit_post.html
├── static/
│   ├── css/
│   │   └── blog.css
│   └── images/
└── media/
    └── uploads/
```

## Getting Started

### 1. Clone and enter project

```bash
git clone <your-repository-url>
cd blog_main
```

### 2. Create virtual environment

```bash
python -m venv .venv
```

### 3. Activate environment

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Windows CMD:

```bat
.venv\Scripts\activate.bat
```

macOS/Linux:

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Apply migrations

```bash
python manage.py migrate
```

### 6. Create admin user (optional but recommended)

```bash
python manage.py createsuperuser
```

## How to Run

```bash
python manage.py runserver
```

Open in browser:

- http://127.0.0.1:8000/

## URL Map

- `/` -> Home page
- `/admin/` -> Django admin panel
- `/register/` -> User registration
- `/login/` -> User login
- `/logout/` -> User logout
- `/category/<id>/` -> Posts by category
- `/blogs/search/` -> Blog search
- `/blogs/<slug>/` -> Blog detail
- `/dashboard/` -> Dashboard home
- `/dashboard/categories/` -> Category list
- `/dashboard/category/add/` -> Add category
- `/dashboard/category/edit/<id>/` -> Edit category
- `/dashboard/category/delete/<id>/` -> Delete category
- `/dashboard/posts/` -> Post list
- `/dashboard/posts/add/` -> Add post
- `/dashboard/post/edit/<id>/` -> Edit post
- `/dashboard/post/delete/<id>/` -> Delete post

## Useful Commands

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
python manage.py createsuperuser
python manage.py collectstatic
```

## Notes

- Uploaded files are stored under `media/uploads/`.
- Static files are configured using `STATICFILES_DIRS` and `STATIC_ROOT` in settings.
- Context processors are configured for categories and social links.
- For production deployment, set `DEBUG = False`, configure `ALLOWED_HOSTS`, and serve static/media from a proper web server.
