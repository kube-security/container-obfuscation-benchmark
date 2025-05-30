
FROM python@sha256:d78428228533d961b772473e6c9ec0e1ef8c910034eaa09cf149bc7515d6ed19


WORKDIR /app
COPY requirements.txt .
RUN pip install --break-system-package -r requirements.txt
COPY . .


RUN rm -rf /usr/local/lib/python3.10/site-packages/*.dist-info
RUN rm -rf /usr/lib/python3/dist-packages/*.egg-info

