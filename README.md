# HNG Public API

This is a public API that returns basic information in JSON format.

## Technology Stack

- **Programming Language**: Python
- **Framework**: Django
- **Deployment**: Vercel

## Information Returned

- Registered email address
- Current datetime as an ISO 8601 formatted timestamp
- GitHub URL of the project's codebase

## Endpoint

### GET /

#### Response Format (200 OK)

```json
{
  "email": "marveldoc17@gmail.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/Marvellous-Udoye/public_api"
}
```

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Marvellous-Udoye/public_api.git
   cd public_api
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Start the server**:
   ```bash
   python manage.py runserver
   ```

6. The API will be accessible at `http://localhost:8000`.

## Deployment

The API is deployed on Vercel. You can access it at `https://public-api-gjmg.onrender.com/`.

## Example Usage

```bash
curl <>
```

## Related Link

[Hire Python Developers](https://hng.tech/hire/python-developers)

## Additional Information

### Project Structure

```
public_api/
├── manage.py
├── public_api/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   ├── wsgi.py
└── README.md
```

### Requirements

- Python 3.6+
- Django 3.2+
- Django REST framework
- django-cors-headers

### How to Deploy on Vercel

1. **Install Vercel CLI**:
   ```bash
   npm install -g vercel
   ```

2. **Log in to Vercel**:
   ```bash
   vercel login
   ```

3. **Deploy the project**:
   ```bash
   vercel
   ```

   Follow the prompts to deploy the project. Vercel will provide you with a URL where your API is hosted.

### Testing the Endpoint

You can test the endpoint using `curl` or any API testing tool like Postman.

```bash
curl https://public-api-gjmg.onrender.com/
```

This will return the JSON response with your email, current datetime, and GitHub URL.