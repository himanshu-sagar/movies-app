FROM python:3.8-slim 
COPY . /app
WORKDIR /app
RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile
EXPOSE 8080
CMD ["gunicorn","-w","1", "-b", "0.0.0.0:8080","--timeout", "3600", "app:initialize_app()", "--preload"]