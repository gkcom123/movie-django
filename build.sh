    set -o errexit
    pip install --no-cache-dir -r requirements.txt
    python manage.py collectstatic --noinput
    python manage.py migrate
    