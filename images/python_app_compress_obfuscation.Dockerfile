
FROM python:3.10 AS builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --break-system-package -r requirements.txt
COPY . .


FROM scratch
COPY --from=builder / /
WORKDIR /app
