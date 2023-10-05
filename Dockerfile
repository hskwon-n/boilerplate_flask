FROM python:3.9-slim-buster

WORKDIR /workspace/hskwon/boilerplate_flask

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "-m", "debugpy", "--listen", "0.0.0.0:5678", "application.py"]
