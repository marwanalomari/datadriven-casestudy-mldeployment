FROM python:3.7

ADD negative_examples_posology.csv .
ADD positive_examples_posology.csv .
ADD build_model.py .

RUN pip install scikit-learn
RUN pip install pandas

CMD ["python", "./build_model.py"]