FROM python:3.9  

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./main.py /code/

ENV PORT=8080

EXPOSE 8080

CMD ["strawberry", "server", "main"]

