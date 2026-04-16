# Django Blog Project

A simple Django blog application with featured posts, recent articles, category pages, post detail pages, and social links in the sidebar.

## Features

- Home page with featured posts and recent articles
- Blog detail page for individual posts
- Category-based post listings
- Image upload support for posts
- Sidebar with search, categories, and social links
- Bootstrap-based responsive layout

## Tech Stack

- Python 3
- Django 5.2
- SQLite
- Bootstrap 4
- Pillow for image uploads

## Project Structure

- `blog_main/` - Django project settings and main app
- `blogs/` - Blog app with models, views, URLs, and templates
- `templates/` - Shared HTML templates
- `static/` - CSS and other static assets
- `media/` - Uploaded images
- `requirements.txt` - Python dependencies used to install the project environment

## Setup Instructions

### 1. Clone the repository

```bash
git clone <your-repository-link>
cd "blog_main"
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

This installs the packages listed in requirements.txt, including Django and Pillow.

### 4. Run migrations

```bash
python manage.py migrate
```

### 5. Create a superuser

```bash
python manage.py createsuperuser
```

### 6. Start the development server

```bash
python manage.py runserver
```

Then open:

```bash
http://127.0.0.1:8000/
```

## Notes

- Uploaded blog images are stored in `media/uploads/`.
- The project uses SQLite by default.
- If you want to share the project publicly, make sure `DEBUG = False`, configure `ALLOWED_HOSTS`, and set up static/media handling for deployment.

## Common Commands

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
python manage.py createsuperuser
```

## License

This project does not currently include a license.
