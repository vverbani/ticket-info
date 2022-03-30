# syntax=docker/dockerfile:1
FROM python:3.7-alpine

# Set the working directory
COPY . /src
WORKDIR /src

RUN apk add --no-cache gcc musl-dev linux-headers

# Copy the requirements over and then install all dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5000

COPY . .

CMD ["flask", "run"]