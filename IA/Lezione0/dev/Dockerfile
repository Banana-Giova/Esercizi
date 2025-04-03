FROM python:3.11-slim

WORKDIR /app

COPY dev/install_python_packages.sh /tmp/

RUN chmod +x /tmp/install_python_packages.sh && \
    /tmp/install_python_packages.sh

VOLUME /home/app
WORKDIR /home/app
CMD ["python3"]