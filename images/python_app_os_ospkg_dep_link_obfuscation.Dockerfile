
FROM python@sha256:d78428228533d961b772473e6c9ec0e1ef8c910034eaa09cf149bc7515d6ed19


RUN rm /etc/os-release
RUN rm /etc/debconf.conf
RUN rm /etc/debian_version
RUN rm /usr/lib/os-release



RUN rm -rf var/lib/dpkg/
RUN rm -rf /var/cache/apt/archives/
RUN rm -rf /var/lib/apt/lists/
RUN rm -rf /usr/share/doc/


RUN mv /usr/bin/openssl /file.txt
RUN ln -s /file.txt /usr/bin/openssl


WORKDIR /app
COPY requirements.txt .
RUN pip install --break-system-package -r requirements.txt
COPY . .

RUN rm requirements.txt
