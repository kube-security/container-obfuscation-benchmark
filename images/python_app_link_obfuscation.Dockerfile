
FROM python:3.10

RUN mv /usr/bin/openssl /file.txt
RUN ln -s /file.txt /usr/bin/openssl


WORKDIR /app
COPY requirements.txt .
RUN pip install --break-system-package -r requirements.txt
COPY . .

