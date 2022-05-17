FROM python:3-slim

WORKDIR /usr/src/app

# See exact list of files in .dockerignore
ADD . /usr/src/app/

RUN pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir gunicorn

EXPOSE 80

CMD [ "gunicorn", "-b", "0.0.0.0:80", "app:app" ]