FROM python:3.10.12
WORKDIR /app
COPY event_manager/requirements.txt /app/
RUN pip install -r requirements.txt --no-cache-dir
COPY . /app/
RUN ls -al

CMD python /app/event_manager/manage.py migrate && python /app/event_manager/manage.py runserver 0:8000
