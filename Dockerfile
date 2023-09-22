FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . /code

RUN wget https://huggingface.co/thangved/zitwaste/resolve/main/model.keras -O /code/model.keras

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
