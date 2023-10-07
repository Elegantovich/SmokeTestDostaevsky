FROM python:3.8 
RUN mkdir /app
COPY . /app 
COPY requirements.txt /app
RUN pip install -r /app/requirements.txt
WORKDIR /app
RUN chmod 777 /app/allure/bin/allure

CMD ["python", "main.py"]