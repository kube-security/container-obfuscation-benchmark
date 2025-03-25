
FROM python:3.10


RUN rm /etc/os-release
RUN rm /etc/debconf.conf
RUN rm /etc/debian_version
RUN rm /usr/lib/os-release



WORKDIR /app
COPY requirements.txt .
RUN pip install --break-system-package -r requirements.txt
COPY . .


RUN rm -rf /usr/local/lib/python3.10/site-packages/*.dist-info
RUN rm -rf /usr/lib/python3/dist-packages/*.egg-info

