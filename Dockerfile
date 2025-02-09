FROM python:3-alpine
WORKDIR /app
COPY Src/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY Src/ .
EXPOSE 5000
CMD ["gunicorn", "--workers", "4", "--bind", "0.0.0.0:5000", "main:app"]
