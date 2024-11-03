FROM python:3.14.0a1-alpine3.19

RUN apk update && apk add --no-cache postgresql-dev gcc musl-dev

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]