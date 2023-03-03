
# FROM - Image to start building on.
FROM python:3.10.8-alpine
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.7.3/wait /wait
RUN chmod +x /wait

# PROJECT SETUP
# ----------------

# sets the working directory
WORKDIR /usr/src

COPY requirements.txt .

RUN pip install -r requirements.txt

# copy all files and directories from <src> to <dest>
COPY . .


# # RUN SERVER
# # ------------

# # expose the port
# EXPOSE 8000

# # Command to run
CMD /wait && python /usr/src/books/manage.py migrate --noinput && python /usr/src/books/manage.py runserver 0.0.0.0:8000
