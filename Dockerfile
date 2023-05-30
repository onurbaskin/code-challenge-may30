# The first instruction is what image I want to base our container on
FROM python:3.9.6

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# Get my answer example app
RUN git clone https://github.com/onurbaskin/code-challenge-may30.git /colorifix

# Set the working directory to /colorifix
# NOTE: all the directives that follow in the Dockerfile will be executed in
# that directory.
WORKDIR /colorifix

RUN ls .

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

VOLUME /colorifix

EXPOSE 8080

CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000
# CMD ["%%CMD%%"]