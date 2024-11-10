echo " BUILDING STARTED"
pip install -r requirements.txt
python manage.py collectstatic --noinput --clear
python manage.py makemigrations
python manage.py migrate
echo " Build files completed"