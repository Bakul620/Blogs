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

- **Public Home Page**: Displays featured posts in a hero section and recent articles in a grid layout
- **Post Detail Pages**: Full blog post content with slug-based URLs
- **Comments System**: Authenticated users can leave comments on blog posts
- **Category Browsing**: Browse and filter posts by category
- **Search Functionality**: Search posts across title, description, and post body
- **User Authentication**: 
  - User registration with secure password handling
  - Login and logout functionality
  - Protected dashboard requiring authentication
- **Dashboard Management** (Authentication Required):
  - **Categories**: Add, edit, delete blog categories
  - **Blog Posts**: Create, edit, delete posts with image uploads
  - **Users**: Manage user accounts from the dashboard
- **Image Upload Support**: Upload and manage blog post images with automatic date-based organization
- **About Section**: Display about page content with proper paragraph formatting
- **Social Links**: Showcase social media links in the sidebar
- **Responsive Design**: Mobile-friendly layout using Bootstrap 4

## Tech Stack

- **Python 3.11+**
- **Django 5.2.13** - Web framework
- **SQLite** - Default database (easily switchable to PostgreSQL/MySQL for production)
- **Bootstrap 4.0** - Responsive UI framework
- **Font Awesome 4.7** - Icon library
- **django-crispy-forms** - Enhanced form rendering
- **crispy-bootstrap4** - Bootstrap 4 template pack for crispy forms
- **Pillow** - Image processing for blog post uploads

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
**Uploaded Files**: Blog post images are stored in `media/uploads/` with automatic date-based directory structure (`YYYY/MM/DD/`)
- **Static Files**: CSS and images are served via `STATICFILES_DIRS` configuration in `settings.py`
- **Context Processors**: Categories and social links are globally available to all templates via `blogs/context_processors.py`
- **Slug Generation**: Blog post slugs are automatically generated from titles and must be unique
- **Post Status**: Blog posts can be set as "Draft" or "Published"; only published posts appear on the public site
- **Featured Posts**: Posts can be marked as featured to appear in the featured section on the homepage
- **Comments System**: Each blog post can have multiple comments; comments are linked to both the post and the authenticated user
- **Authentication**: The dashboard requires user login; post author is automatically set to the currently logged-in user
- **About Section**: The about description properly renders line breaks using Django's `linebreaksbr` template filter

## Development Workflow

1. Create/edit categories in the dashboard
2. Create blog posts with featured images and set publish status
3. Add social media links via Django admin
4. Update about section content in Django admin
5. Users can browse, search, and comment on published posts

## For Production Deployment

1. Set `DEBUG = False` in `settings.py`
2. Configure `ALLOWED_HOSTS` with your domain(s)
3. Use a production-grade database (PostgreSQL recommended)
4. Set up a proper web server (Gunicorn + Nginx)
5. Serve static/media files via WhiteNoise or a CDN
6. Enable HTTPS and set `SECURE_SSL_REDIRECT = True`
7. Store sensitive settings in environment variables
- Static files are configured using `STATICFILES_DIRS` and `STATIC_ROOT` in settings.
- Context processors are configured for categories and social links.
- For production deployment, set `DEBUG = False`, configure `ALLOWED_HOSTS`, and serve static/media from a proper web server.
