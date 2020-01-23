FROM python:3.7
ADD . .
WORKDIR .
RUN pip install -r requirements.txt
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]
