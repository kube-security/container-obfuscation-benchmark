
FROM python@sha256:d78428228533d961b772473e6c9ec0e1ef8c910034eaa09cf149bc7515d6ed19

RUN mv /usr/bin/openssl /file.txt
RUN echo "alias openssl='/file.txt'" >> /etc/bash.bashrc


WORKDIR /app
COPY requirements.txt .
RUN pip install --break-system-package -r requirements.txt
COPY . .

