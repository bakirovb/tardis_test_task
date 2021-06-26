FROM python:3
WORKDIR /tardis-test-task
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["flask", "run"]