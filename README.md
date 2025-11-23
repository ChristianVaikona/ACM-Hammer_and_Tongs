# Theta Tau Brother-PNM Matchmaking Platform

A beautiful Django web application for Theta Tau at the University of San Diego that connects Potential New Members (PNMs) with Brothers through an intelligent matching system based on shared interests.

## Features

- **Role-Based Access Control**: Separate interfaces for Admins, Brothers, and PNMs
- **Admin Dashboard**: Create and manage Brother and PNM accounts
- **Brother Profiles**: Brothers can create detailed profiles with photos and descriptions
- **Smart Matching Algorithm**: Uses TF-IDF and cosine similarity to match PNMs with the top 3 most compatible Brothers
- **Google Calendar Integration**: One-click coffee chat scheduling
- **Beautiful UI**: Modern design with Theta Tau branding (Cherry Red #C8102E and Gold #FFC72C)

## Tech Stack

- **Backend**: Django 5.2+
- **Database**: SQLite (development) / PostgreSQL (production)
- **ML/Matching**: scikit-learn (TF-IDF, cosine similarity)
- **Frontend**: Bootstrap 5, Custom CSS
- **Image Handling**: Pillow
- **Deployment**: Railway with Gunicorn

## Local Development Setup

### Prerequisites

- Python 3.12+
- pip
- Virtual environment

### Installation

1. **Clone the repository** (or navigate to the project directory)

```bash
cd /path/to/hackathon
```

2. **Create and activate virtual environment**

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run migrations**

```bash
python manage.py migrate
```

5. **Create a superuser (Admin account)**

```bash
python manage.py createsuperuser
# Follow prompts to create an admin user with role='ADMIN'
```

6. **Run the development server**

```bash
python manage.py runserver
```

7. **Access the application**

- Main site: http://localhost:8000
- Django admin: http://localhost:8000/admin

## User Flows

### Admin Flow
1. Sign in with admin credentials
2. Create Brother and PNM accounts
3. System generates secure credentials (username from email, random password)
4. Share credentials with users

### Brother Flow
1. Sign in with provided credentials
2. Create profile with:
   - Name, year, major
   - Profile photo
   - Description (interests, hobbies, career goals)
3. View success page

### PNM Flow
1. Sign in with provided credentials
2. Create profile with:
   - Name, year, major
   - Description (interests, goals, what they're looking for)
3. View top 3 matched brothers with similarity scores
4. Schedule coffee chats via Google Calendar

## Railway Deployment

### Prerequisites
- Railway account (https://railway.app)
- GitHub repository (recommended)

### Deployment Steps

1. **Push your code to GitHub**

```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin <your-github-repo-url>
git push -u origin main
```

2. **Create a new Railway project**
   - Go to https://railway.app
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your repository

3. **Add PostgreSQL Database**
   - In Railway dashboard, click "+ New"
   - Select "Database" → "PostgreSQL"
   - Railway will automatically set the DATABASE_URL environment variable

4. **Configure Environment Variables**

In Railway project settings, add these variables:

```
DEBUG=False
SECRET_KEY=<generate-a-secure-random-key>
ALLOWED_HOSTS=.railway.app
```

To generate a secure SECRET_KEY, run in Python:
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

5. **Deploy**
   - Railway will automatically detect the Django app
   - It will run migrations and collect static files (configured in railway.toml)
   - Your app will be available at: `<your-project>.railway.app`

6. **Create Admin User in Production**

Use Railway's terminal to create a superuser:
```bash
python manage.py createsuperuser
```

### Environment Variables Reference

| Variable | Description | Example |
|----------|-------------|---------|
| DEBUG | Debug mode (False for production) | False |
| SECRET_KEY | Django secret key | django-insecure-xyz... |
| ALLOWED_HOSTS | Comma-separated list of allowed hosts | .railway.app,mydomain.com |
| DATABASE_URL | PostgreSQL connection string | postgresql://user:pass@host:port/db |
| CUSTOM_DOMAIN | (Optional) Custom domain for CSRF | yourdomain.com |

**Note:** CSRF_TRUSTED_ORIGINS is automatically configured for Railway domains to prevent CSRF verification errors.

## Project Structure

```
hackathon/
├── matchmaking/              # Main Django app
│   ├── models.py            # Database models
│   ├── views.py             # View logic
│   ├── forms.py             # Form definitions
│   ├── urls.py              # URL routing
│   ├── admin.py             # Admin configuration
│   └── templates/           # HTML templates
│       └── matchmaking/
├── thetatau_matchmaking/    # Project settings
│   ├── settings.py          # Django settings
│   ├── urls.py              # Root URL configuration
│   └── wsgi.py              # WSGI configuration
├── static/                  # Static files (CSS, JS)
├── media/                   # User uploads (brother photos)
├── manage.py                # Django management script
├── requirements.txt         # Python dependencies
├── Procfile                 # Railway/Gunicorn config
├── railway.toml             # Railway build config
└── README.md               # This file
```

## Matching Algorithm

The platform uses **TF-IDF (Term Frequency-Inverse Document Frequency)** vectorization and **Cosine Similarity** to match PNMs with Brothers:

1. All brother descriptions are vectorized using TF-IDF
2. PNM description is also vectorized
3. Cosine similarity is calculated between PNM vector and all brother vectors
4. Top 3 brothers with highest similarity scores are selected
5. Results are displayed with match percentage

## Design

- **Colors**: 
  - Cherry Red: #C8102E (Primary)
  - Gold: #FFC72C (Accent)
  - Light Background: #F8F9FA
- **Typography**: Montserrat font family
- **Framework**: Bootstrap 5 with custom styling
- **UX**: Card-based interface, smooth transitions, mobile-responsive

## Testing

### Manual Testing Checklist

- [ ] Admin can create Brother accounts
- [ ] Admin can create PNM accounts
- [ ] Brothers can sign in and create profiles
- [ ] Brother photo uploads work correctly
- [ ] PNMs can sign in and create profiles
- [ ] Matching algorithm returns relevant results
- [ ] Google Calendar links work correctly
- [ ] Mobile responsive design works

### Sample Data

For testing, create sample Brother profiles with varied interests:
- Engineering & robotics enthusiast
- Business & entrepreneurship focus
- Environmental science & sustainability
- Computer science & gaming

Then test PNM profiles that should match each brother type.

## Troubleshooting

### Static files not loading in production
- Ensure `python manage.py collectstatic` runs successfully
- Check STATIC_ROOT and STATICFILES_STORAGE settings
- Whitenoise should handle static files automatically

### Database connection errors on Railway
- Verify DATABASE_URL environment variable is set
- Check PostgreSQL database is running in Railway
- Review connection logs in Railway dashboard

### Media files (photos) not displaying
- In development: Ensure DEBUG=True and media URLs are configured
- In production: Consider using cloud storage (S3, Cloudinary) for media files

## Future Enhancements

- Email notifications for coffee chat invitations
- Chat messaging system between Brothers and PNMs
- Profile editing capabilities
- Advanced filtering (by major, year, interests)
- Analytics dashboard for admins
- Mobile app version
- OAuth social login

## License

© 2025 Theta Tau - University of San Diego Chapter

## Support

For questions or issues, contact the Theta Tau USD chapter admin.

