# travel_app1
# Travel App Backend

## Setup

1. Create a virtual environment:
    python -m venv travel
    travel/Scripts/activate
    

2. Install dependencies:
    pip install -r requirements.txt
   

3. Run migrations:
    python manage.py makemigrations
    python manage.py migrate
  

4. Create a superuser: 
    python manage.py createsuperuser
    

5. Run the server:
    python manage.py runserver
    

## Running Tests

python manage.py test
