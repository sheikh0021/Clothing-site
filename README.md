# Sami Clothing - Men's Fashion E-commerce

A modern, responsive Django e-commerce website for men's clothing built with Bootstrap and featuring user authentication.

## 🛍️ Features

- **Product Catalog**: Browse men's clothing items with detailed product pages
- **User Authentication**: Sign up, login, and logout functionality
- **Responsive Design**: Mobile-friendly interface using Bootstrap 5
- **Product Details**: Individual product pages with size information and pricing
- **Admin Interface**: Django admin panel for managing products
- **Modern UI**: Clean, professional design with gradient backgrounds

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/sami-clothing.git
   cd sami-clothing
   ```

2. **Create a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install django
   ```

4. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Add demo products**
   ```bash
   python manage.py add_demo_products
   ```

7. **Start the development server**
   ```bash
   python manage.py runserver
   ```

8. **Visit the website**
   - Main site: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## 📁 Project Structure

```
sami-clothing/
├── mens_clothing_site/          # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── products/                    # Main app
│   ├── models.py               # Product model
│   ├── views.py                # Views for products and auth
│   ├── urls.py                 # URL routing
│   ├── admin.py                # Admin configuration
│   ├── templates/              # HTML templates
│   │   └── products/
│   │       ├── product_list.html
│   │       ├── product_detail.html
│   │       ├── login.html
│   │       └── signup.html
│   └── management/             # Custom management commands
│       └── commands/
│           └── add_demo_products.py
├── manage.py                   # Django management script
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

## 🎨 Features in Detail

### Product Management
- **Product Model**: Name, description, price, size, and image URL
- **Size Options**: XS, S, M, L, XL, XXL
- **Admin Interface**: Easy product management through Django admin

### User Authentication
- **Sign Up**: Create new accounts with username and password
- **Login**: Secure authentication with error handling
- **Logout**: Safe session termination
- **User Feedback**: Success and error messages

### Responsive Design
- **Bootstrap 5**: Modern CSS framework
- **Mobile-First**: Optimized for all screen sizes
- **Gradient Backgrounds**: Beautiful visual design
- **Hover Effects**: Interactive product cards

## 🔧 Customization

### Adding New Products
1. Access the admin panel at `/admin/`
2. Log in with your superuser credentials
3. Navigate to "Products" section
4. Click "Add Product" and fill in the details

### Modifying Styles
- Edit CSS in the template files
- Bootstrap classes are used for styling
- Custom styles are in `<style>` tags

### Database Management
- SQLite database (default)
- Run `python manage.py makemigrations` after model changes
- Run `python manage.py migrate` to apply changes

## 🛠️ Development

### Running Tests
```bash
python manage.py test
```

### Creating New Management Commands
```bash
python manage.py startapp your_app_name
```

### Static Files
```bash
python manage.py collectstatic
```

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request
