
FROM python:3.10

RUN curl -o postgres.tar.gz -sSL "https://ftp.postgresql.org/pub/source/v16.3/postgresql-16.3.tar.gz"


WORKDIR /app
COPY requirements.txt .
RUN pip install --break-system-package -r requirements.txt
COPY . .

