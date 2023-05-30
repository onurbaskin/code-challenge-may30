# Docker Setup

- docker build -t colorifix .
- docker run -d -p 8080:8000  -v src:/colorifix --name colorifix_app colorifix
- if you need admin user. to create it, enter the container bash via
    - docker exec -it django_drf_app /bin/bash

- docker-compose up -d
