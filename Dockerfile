FROM python:3-alpine
WORKDIR /Src/app
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app
EXPOSE 8000
CMD ["gunicorn", "--workers", "4", "--bind", "0.0.0.0:8000", "wsgi:app"]
