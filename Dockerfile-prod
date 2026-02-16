FROM python:3.12-slim
ENV PYTHONUNBUFFERED=1
ENV PIP_ROOT_USER_ACTION=ignore
WORKDIR /extensions_backend/
COPY requirements.txt .
COPY manage.py .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8005
CMD ["python", "manage.py", "runserver", "0.0.0.0:8005"]