# AttendPro Face Verification API

This repository was created for my university project. It contains the backend API for comparing two face images to determine whether they belong to the same person.  
The API is part of an employee attendance application called **AttendPro**, where facial verification is used as the authentication method.

## Features
- Face image comparison (Face Verification)
- Simple API endpoint to check if two faces match
- Built with Django
- Easy to integrate with mobile or web clients

## Getting Started

### 1. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate      # Linux / macOS
venv\Scripts\activate         # Windows
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the development server
```bash
python manage.py runserver
```

Your API will be available at:
```bash
http://localhost:8000/
```

## Usage
Send two face images to the verification endpoint.
The API will process both images and return a result indicating whether the faces match.

## Notes
This project focuses only on the backend logic.
It is designed to support the AttendPro employee attendance system by providing a reliable face verification API.




