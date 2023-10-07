FROM python:3.11-slim
RUN mkdir /app
COPY . /app 
COPY requirements.txt /app
RUN pip install -r /app/requirements.txt
WORKDIR /app
RUN chmod 777 /app/test_results

CMD python -m pytest -s -v tests/test_buy_product.py