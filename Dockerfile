FROM python:3.14.2
WORKDIR /app
COPY . /app/

RUN pip install --no-cache-dir uv && \
    uv sync --no-dev

EXPOSE 8000
CMD ["uv", "run", "python", "IMS/manage.py", "runserver", "0.0.0.0:8000"]
