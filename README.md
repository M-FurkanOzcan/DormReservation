# Dorm Reservation System

A Django-based web application for managing dorm room reservations, including study rooms and laundry machines.

## Features

- **Room Management**: Manage different types of rooms (study rooms, laundry machines)
- **Time Slot System**: Define available time slots for reservations
- **User Reservations**: Users can book available rooms for specific dates and time slots
- **Admin Dashboard**: Django admin interface for managing rooms, time slots, and reservations
- **Status Tracking**: Track reservation status (active, cancelled, completed)

## Requirements

- Python 3.8+
- Django 6.0.3
- SQLite3 (default database)

## Installation

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd dorm_reservation
```

### 2. Create Virtual Environment

```bash
python3 -m venv venv
```

### 3. Activate Virtual Environment

**On macOS/Linux:**
```bash
source venv/bin/activate
```

**On Windows:**
```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` doesn't exist, create it:
```bash
pip install django
pip freeze > requirements.txt
```

## Setup

### 1. Apply Database Migrations

```bash
python manage.py migrate
```

### 2. Create Superuser (Admin Account)

```bash
python manage.py createsuperuser
```

Follow the prompts to create a username, email, and password.

### 3. Create Initial Data (Optional)

You can add rooms and time slots via the Django admin dashboard.

## Running the Application

### Start Development Server

```bash
python manage.py runserver
```

The application will be available at: `http://127.0.0.1:8000/`

### Access Admin Dashboard

```
http://127.0.0.1:8000/admin/
```

Log in with your superuser credentials.

## Project Structure

```
dorm_reservation/
├── dorm_reservation/          # Project settings
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── reservations/              # Main app
│   ├── models.py             # Database models
│   ├── views.py              # Views
│   ├── urls.py               # URL routing
│   ├── admin.py              # Admin configuration
│   ├── forms.py              # Forms
│   └── migrations/           # Database migrations
├── templates/                 # HTML templates
├── manage.py                 # Django management script
├── db.sqlite3                # Database file
├── requirements.txt          # Python dependencies
└── README.md                 # This file
```

## Database Models

### Room
- `name`: Room name
- `room_type`: Type of room (study/laundry)
- `is_active`: Whether the room is available for booking

### TimeSlot
- `start_time`: Reservation start time
- `end_time`: Reservation end time

### Reservation
- `user`: User making the reservation
- `room`: Room being reserved
- `date`: Reservation date
- `time_slot`: Time slot for the reservation
- `status`: Reservation status (active/cancelled/completed)
- `created_at`: When reservation was created

## Admin Features

The Django admin interface allows you to:
- Add and edit rooms
- Manage time slots
- View and manage reservations
- Filter reservations by status, date, and room
- Search reservations by username or room name

## Troubleshooting

### Import Error: "django.contrib.admin not found"
Make sure you've activated the virtual environment:
```bash
source venv/bin/activate  # macOS/Linux
```

### Database Errors
Reset the database:
```bash
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

### Port Already in Use
Run on a different port:
```bash
python manage.py runserver 8001
```

## Development

### Deactivate Virtual Environment
```bash
deactivate
```

### Making Changes to Models
After modifying models, create and apply migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

## Security Notes

- Change `SECRET_KEY` in `settings.py` before production
- Set `DEBUG = False` in `settings.py` for production
- Use environment variables for sensitive settings
- Do not commit `.env` files or database files to version control

## License

This project is open source and available under the MIT License.

## Support

For issues or questions, please open an issue in the repository.
