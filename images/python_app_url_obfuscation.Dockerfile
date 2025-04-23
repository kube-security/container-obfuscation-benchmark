
FROM python@sha256:d78428228533d961b772473e6c9ec0e1ef8c910034eaa09cf149bc7515d6ed19

RUN curl -o postgres.tar.gz -sSL "https://ftp.postgresql.org/pub/source/v16.3/postgresql-16.3.tar.gz"


WORKDIR /app
COPY requirements.txt .
RUN pip install --break-system-package -r requirements.txt
COPY . .

