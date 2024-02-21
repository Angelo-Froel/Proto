FROM python:3.9-slim

WORKDIR /server

# Install dependencies
RUN pip install flask

COPY server.py .

CMD ["python", "server.py"]
