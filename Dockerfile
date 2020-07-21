FROM python:3.7

WORKDIR /app

COPY requirements.txt /app
RUN pip3 install --upgrade pip -r requirements.txt

# Add the rest of the code
COPY demos /app/demos
COPY frontend /app/frontend
COPY portfolio_app /app/portfolio_app
COPY db.sqlite3 /app
COPY manage.py /app
COPY README.md /app

# Make port 8000 available for the app
EXPOSE 8000

WORKDIR frontend
CMD ls
CMD npm install
CMD npm run build
CMD npm run dev
WORKDIR /app

#CMD sudo apt-get install nginx
#CMD sudo /etc/init.d/nginx start
CMD python manage.py collectstatic -link --noinput
# Be sure to use 0.0.0.0 for the host within the Docker container,
# otherwise the browser won't be able to find it
#CMD python3 manage.py runserver 0.0.0.0:8000
CMD gunicorn --bind 0.0.0.0:80 portfolio_app.wsgi:application

