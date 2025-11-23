# Railway Deployment Checklist

## Pre-Deployment

- [ ] Test application locally at http://localhost:8000
- [ ] Verify all user flows work (Admin, Brother, PNM)
- [ ] Test matching algorithm with sample data
- [ ] Verify photo uploads work correctly
- [ ] Test Google Calendar link generation
- [ ] Review and update `requirements.txt`
- [ ] Commit all changes to Git

## Railway Setup

### 1. Repository Setup
- [ ] Create GitHub repository
- [ ] Push code to GitHub:
  ```bash
  git init
  git add .
  git commit -m "Initial commit: Theta Tau Matchmaking Platform"
  git branch -M main
  git remote add origin <your-repo-url>
  git push -u origin main
  ```

### 2. Railway Project Creation
- [ ] Sign up/login to Railway (https://railway.app)
- [ ] Click "New Project"
- [ ] Select "Deploy from GitHub repo"
- [ ] Authorize Railway to access your repository
- [ ] Select your repository

### 3. Add PostgreSQL Database
- [ ] In Railway dashboard, click "+ New"
- [ ] Select "Database" → "PostgreSQL"
- [ ] Wait for database to provision
- [ ] Verify DATABASE_URL variable appears in your service

### 4. Environment Variables

Add these in Railway's service settings → Variables:

```
DEBUG=False
SECRET_KEY=<generate-secure-key>
ALLOWED_HOSTS=.railway.app
```

**Optional (if using custom domain):**
```
CUSTOM_DOMAIN=yourdomain.com
```

**Generate SECRET_KEY:**
```python
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

**Note:** CSRF_TRUSTED_ORIGINS is automatically configured to include:
- All *.railway.app domains
- Your custom domain (if CUSTOM_DOMAIN is set)
- This prevents CSRF verification errors on Railway

### 5. Deploy
- [ ] Railway will automatically detect Django and deploy
- [ ] Wait for build and deployment to complete
- [ ] Check deployment logs for any errors
- [ ] Note your Railway URL (e.g., `your-project.railway.app`)

### 6. Post-Deployment Setup

**Create Admin User:**
- [ ] Open Railway terminal (in your service)
- [ ] Run: `python manage.py createsuperuser`
- [ ] Follow prompts to create admin account
- [ ] Update user role in Django admin or shell:
  ```python
  python manage.py shell
  from matchmaking.models import CustomUser
  u = CustomUser.objects.get(username='your-admin-username')
  u.role = 'ADMIN'
  u.save()
  ```

### 7. Verification
- [ ] Visit your Railway URL
- [ ] Landing page loads correctly
- [ ] Theta Tau branding appears (red and gold colors)
- [ ] Login page works
- [ ] Admin can log in
- [ ] Static files load (CSS, fonts)

## Post-Deployment Testing

### Admin Flow
- [ ] Admin can access admin dashboard
- [ ] Admin can create Brother accounts
- [ ] Admin can create PNM accounts
- [ ] Credentials display correctly after account creation

### Brother Flow
- [ ] Brother can log in with credentials
- [ ] Brother profile form loads
- [ ] Photo upload works
- [ ] Profile saves successfully
- [ ] Success page displays with profile info

### PNM Flow
- [ ] PNM can log in with credentials
- [ ] PNM profile form loads
- [ ] Profile saves successfully
- [ ] Matching results display (if brothers exist)
- [ ] Match percentages show correctly
- [ ] Google Calendar links work

## Troubleshooting

### Static Files Not Loading
```bash
# In Railway terminal:
python manage.py collectstatic --noinput
```

### Database Connection Issues
- Check that DATABASE_URL is set correctly
- Verify PostgreSQL database is running
- Review connection logs in Railway

### Application Errors
- Check Railway logs in dashboard
- Verify all environment variables are set
- Ensure requirements.txt is up to date

### Photos Not Uploading
For production, consider using cloud storage:
- AWS S3
- Cloudinary
- Railway Volumes (for persistent storage)

## Optional Enhancements

### Custom Domain
- [ ] Purchase domain
- [ ] Add domain in Railway settings
- [ ] Update ALLOWED_HOSTS to include your domain
- [ ] Configure DNS records

### Environment-Specific Settings
- [ ] Set up staging environment
- [ ] Configure separate databases for staging/prod
- [ ] Set up CI/CD pipeline

### Monitoring
- [ ] Set up error tracking (Sentry)
- [ ] Configure uptime monitoring
- [ ] Set up log aggregation

### Backups
- [ ] Set up automated database backups
- [ ] Export and backup media files
- [ ] Document restore procedures

## Important Notes

1. **Security**
   - Change default admin password immediately
   - Keep SECRET_KEY secure and never commit to Git
   - Review Django security checklist: https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

2. **Media Files**
   - Current setup stores photos locally (not ideal for production)
   - Consider cloud storage (S3, Cloudinary) for scalability
   - Railway Volumes can provide persistent storage

3. **Database**
   - PostgreSQL on Railway is automatically backed up
   - Consider manual backups for critical data
   - Test restore procedures

4. **Performance**
   - Monitor response times
   - Add database indexes if needed
   - Consider caching for better performance

## Support Resources

- Railway Docs: https://docs.railway.app
- Django Deployment: https://docs.djangoproject.com/en/5.2/howto/deployment/
- Railway Discord: https://discord.gg/railway

## Success Criteria

✅ All checklist items completed
✅ Application accessible via Railway URL
✅ All three user flows tested and working
✅ No errors in Railway logs
✅ Admin can manage accounts
✅ Brothers can create profiles with photos
✅ PNMs can see matched brothers and schedule chats

---

**Deployment Date**: _____________
**Railway URL**: _____________
**Admin Email**: _____________
**Notes**: _____________

