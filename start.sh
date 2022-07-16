# Start this only if virtualenv is not already active

source "/Users/vigneshshetty/Desktop/Development/Blog-APIs/venv/bin/activate"

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
