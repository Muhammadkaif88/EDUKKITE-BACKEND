# Edukkit Backend API

Django REST Framework backend for the Edukkit app with email/password authentication and product management.

## Features

- **Email-based Authentication**: Custom user model using email instead of username
- **JWT Token Authentication**: Secure token-based authentication using SimpleJWT
- **Product Management**: CRUD operations for products with image uploads
- **Admin Controls**: Admin-only access for product creation and editing
- **CORS Enabled**: Ready for Flutter app integration
- **Search & Filtering**: Product search and filtering capabilities

## Tech Stack

- Django 5.0+
- Django REST Framework
- SimpleJWT for authentication
- SQLite (development) / PostgreSQL (production ready)
- Pillow for image handling

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Setup Steps

1. **Clone or navigate to the project directory**
   ```bash
   cd edukkit_backend
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Create environment file**
   ```bash
   copy .env.example .env
   ```
   Then edit `.env` and set your SECRET_KEY (you can generate one using Django's `get_random_secret_key()`)

6. **Run migrations**
   ```bash
   python manage.py migrate
   ```

7. **Create a superuser (admin)**
   ```bash
   python manage.py createsuperuser
   ```
   Enter email, name, and password when prompted.

8. **Run the development server**
   ```bash
   python manage.py runserver
   ```

The API will be available at `http://localhost:8000/`

## API Endpoints

### Authentication

- `POST /api/auth/register/` - Register a new user
  ```json
  {
    "email": "user@example.com",
    "name": "John Doe",
    "password": "securepassword123",
    "password_confirm": "securepassword123"
  }
  ```

- `POST /api/auth/login/` - Login and get JWT tokens
  ```json
  {
    "email": "user@example.com",
    "password": "securepassword123"
  }
  ```

- `POST /api/auth/token/refresh/` - Refresh access token
  ```json
  {
    "refresh": "your-refresh-token"
  }
  ```

- `GET /api/auth/user/` - Get current user profile (requires authentication)

### Products

All product endpoints require authentication. Create/Update/Delete require admin privileges.

- `GET /api/products/` - List all products
- `POST /api/products/` - Create a product (admin only)
- `GET /api/products/{id}/` - Get product details
- `PUT /api/products/{id}/` - Update product (admin only)
- `PATCH /api/products/{id}/` - Partial update (admin only)
- `DELETE /api/products/{id}/` - Delete product (admin only)

**Product Fields:**
```json
{
  "name": "Product Name",
  "description": "Product description",
  "price": "99.99",
  "image": "<file upload>",
  "stock": 10,
  "is_active": true
}
```

**Search & Filter:**
- Search: `/api/products/?search=keyword`
- Filter by stock: `/api/products/?stock=10`
- Order by price: `/api/products/?ordering=price` (or `-price` for descending)

## Authentication in Requests

Include the JWT access token in the Authorization header:

```
Authorization: Bearer <your-access-token>
```

## Admin Panel

Access the Django admin panel at `http://localhost:8000/admin/` using your superuser credentials.

## Project Structure

```
edukkit_backend/
├── authentication/          # User authentication app
│   ├── models.py           # Custom User model
│   ├── serializers.py      # User serializers
│   ├── views.py            # Auth endpoints
│   └── urls.py             # Auth routes
├── products/               # Product management app
│   ├── models.py           # Product model
│   ├── serializers.py      # Product serializers
│   ├── views.py            # Product endpoints
│   └── urls.py             # Product routes
├── edukkit_backend/        # Project settings
│   ├── settings.py         # Django settings
│   └── urls.py             # Root URL config
├── media/                  # Uploaded files (created automatically)
├── manage.py               # Django management script
└── requirements.txt        # Python dependencies
```

## Development Notes

- Media files are stored in the `media/` directory
- Database file is `db.sqlite3` (not committed to git)
- CORS is enabled for all origins in DEBUG mode
- JWT access tokens expire after 1 hour
- JWT refresh tokens expire after 7 days

## Next Steps

1. Install Python if not already installed
2. Follow the installation steps above
3. Test the API endpoints using Postman or curl
4. Integrate with your Flutter app

## License

MIT
