FROM python:3.9-slim

WORKDIR /client

# Install dependencies
RUN pip install requests

COPY client.py .

CMD ["python", "client.py"]
