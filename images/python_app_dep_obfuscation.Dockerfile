
FROM python:3.10


WORKDIR /app
COPY requirements.txt .
RUN pip install --break-system-package -r requirements.txt
COPY . .


RUN rm requirements.txt
