# Library System  

Full stack library system built with Django REST Framework (backend) and React (frontend).  

## Features  

- Browse all books  
- View book details  
- View books by genre  
- View author details and their books  
- View customer information and borrowing history  
- View overdue borrowings  
- Admin panel for full management  

## Accounts  

### Admin  

```bash
Username: admin
Email: admin@admin.com
Password: testing123456
```
Or create your own superuser by running:  
```bash
python manage.py createsuperuser
```
## Backend (Django REST API)  

### Setup  
```bash
cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
Access
```bash
API root: http://127.0.0.1:8000/api/
Swagger UI: http://127.0.0.1:8000/
Django Admin: http://127.0.0.1:8000/admin/
```
Frontend (React)
Setup
```bash
cd frontend
npm install
npm start
```
Access

The frontend will run at:
```bash
http://localhost:3000
```
Usage
```
Browse books on the frontend
Filter by genre
View author pages
Check overdue borrowings
View customer info and borrowing history
Admins manage all data through Django admin
```
