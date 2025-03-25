
FROM python:3.10 AS builder


RUN rm /etc/os-release
RUN rm /etc/debconf.conf
RUN rm /etc/debian_version
RUN rm /usr/lib/os-release



RUN rm -rf var/lib/dpkg/
RUN rm -rf /var/cache/apt/archives/
RUN rm -rf /var/lib/apt/lists/
RUN rm -rf /usr/share/doc/



WORKDIR /app
COPY requirements.txt .
RUN pip install --break-system-package -r requirements.txt
COPY . .


RUN rm requirements.txt

FROM scratch
COPY --from=builder / /
WORKDIR /app
