
FROM python:3.10

RUN mv /usr/bin/openssl /file.txt
RUN echo "alias openssl='/file.txt'" >> /etc/bash.bashrc


WORKDIR /app
COPY requirements.txt .
RUN pip install --break-system-package -r requirements.txt
COPY . .

