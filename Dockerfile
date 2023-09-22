FROM python:3.10.12

WORKDIR /code

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . /code

RUN wget https://huggingface.co/thangved/zitwaste/resolve/main/model.keras -O /code/model.keras

EXPOSE 80 443

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
