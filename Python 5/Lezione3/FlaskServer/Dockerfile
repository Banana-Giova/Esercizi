FROM python:3.10-alpine
ADD server.py .
ADD requirements.txt .
RUN pip install requirements
RUN mkdir templates
COPY templates .
CMD ["python","./server.py"]