# Django + Vue.js Quiz Application

A simple quiz application built with Django REST Framework backend and Vue.js 3 frontend using vue-flow-form for an interactive quiz experience.

## Features

- Interactive quiz interface with one question at a time
- Multiple choice and true/false questions
- Automatic scoring
- RESTful API backend
- Mobile-friendly design

## Project Structure

```
project/
├── backend/
│   ├── quiz_project/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── quiz/
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   └── urls.py
│   ├── fixtures/
│   │   └── quiz_data.json
│   ├── manage.py
│   └── requirements.txt
└── frontend/
    ├── src/
    │   ├── components/
    │   │   └── QuizFlow.vue
    │   ├── App.vue
    │   └── main.js
    ├── public/
    │   └── index.html
    └── package.json
```

## Backend Setup

1. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

3. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Load sample quiz data:
   ```bash
   python manage.py loaddata fixtures/quiz_data.json
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

The API will be available at http://localhost:8000/api/questions/

## Frontend Setup

1. Install dependencies:
   ```bash
   cd frontend
   npm install
   ```

2. Start the development server:
   ```bash
   npm run serve
   ```

The application will be available at http://localhost:8080

## API Endpoints

- `GET /api/questions/` - List all questions with their answers
- `GET /api/questions/<id>/` - Get a specific question with its answers

## Technologies Used

Backend:
- Django 5.0.3
- Django REST Framework 3.14.0
- django-cors-headers 4.3.1
- SQLite database

Frontend:
- Vue.js 3.4
- @ditdot-dev/vue-flow-form 2.3.2
- Axios for API calls

## Development

### Adding New Questions

You can add new questions either through:
1. Django admin interface
2. Direct database manipulation
3. Creating new fixtures

Example fixture format:
```json
{
    "model": "quiz.question",
    "pk": 1,
    "fields": {
        "text": "What is the capital of France?",
        "question_type": "multiple",
        "created_at": "2024-03-19T10:00:00Z"
    }
}
```

### Question Types

Currently supported question types:
- `multiple` - Multiple choice questions
- `boolean` - True/False questions
- `text` - Text input questions

