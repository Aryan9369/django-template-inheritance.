# Django Template Inheritance Project

A simple **Django project** demonstrating how to use **template inheritance**.
It shows how multiple pages (`home`, `about`) can share the same base layout (`base.html`) while keeping unique content.

---

## 🚀 Features

* Base template (`base.html`) with:

  * Header + Navbar
  * Footer
  * Reusable block sections (`pagename`, `content`, `footerextra`)
* Child templates (`home.html`, `about.html`) using `{% extends %}` and `{% block %}`
* Shared layout across pages → avoids repeating HTML
* Simple Django view and URL routing

---

## 📂 Project Structure

```
myproject/
│
├── myapp/
│   ├── templates/
│   │   ├── base.html
│   │   ├── home.html
│   │   └── about.html
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── myproject/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
└── manage.py
```

---

## ⚙️ Installation & Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/django-template-inheritance.git
   cd django-template-inheritance
   ```

2. **Create a virtual environment & activate it**

   ```bash
   python -m venv venv
   venv\Scripts\activate   # On Windows
   source venv/bin/activate  # On Mac/Linux
   ```

3. **Install Django**

   ```bash
   pip install django
   ```

4. **Run migrations**

   ```bash
   python manage.py migrate
   ```

5. **Start the development server**

   ```bash
   python manage.py runserver
   ```

6. **Open in browser**

   * Home Page → [http://127.0.0.1:8000/myapp/home/](http://127.0.0.1:8000/myapp/home/)
   * About Page → [http://127.0.0.1:8000/myapp/about/](http://127.0.0.1:8000/myapp/about/)

---

## 📝 Learning Points

* How `{% extends %}` lets child templates reuse a base template.
* How `{% block ... %}{% endblock %}` defines replaceable sections.
* Why template inheritance helps keep code DRY (Don’t Repeat Yourself).
* How to connect **views → templates → URLs** in Django.

---

## 👤 Author

Developed by **Aryan Katiyar** while practicing Django template inheritance.

---


