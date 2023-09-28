FROM python:3.9

WORKDIR /src

ENV SECRET_KEY=KLFNR28E3XX1401211381704JIDSOPJF$$(^@#)

ENV DEBUG=True
ENV ALLOWED_HOSTS=*

RUN apt update
RUN apt install mc -y

COPY . .

RUN pip install -r requirements.txt
RUN python3 manage.py migrate

EXPOSE 8000

# RUN python3 manage.py runserver 0.0.0.0:8000
CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000"]
