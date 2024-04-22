Para la primera vez que prendes el proyecto corre los siguientes pasos:
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py runserver

Para correr el proyecto activa el entorno con sus requerimientos y corre el siguiente comando:
python manage.py runserver

Para actualizar las migraciones corre lo siguiente:
python manage.py makemigrations
python manage.py migrate