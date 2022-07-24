FROM python:3.7

WORKDIR /app
COPY . /app

RUN pip install flask
RUN pip install scikit-learn
EXPOSE 4002

CMD ["python","app.py"]