FROM rasa/rasa-sdk:latest 

#define the working directory of Docker container
WORKDIR /app 
#copy the requirements txt file with your dependencies in actions directory
COPY ./requirements-actions.txt ./ 
#copy everything in ./actions directory (your custom actions code) to /app/actions in container
# COPY ./ /app/actions
COPY actions.py /app
COPY config.py /app
COPY gpt.py /app
COPY connector/MyIO.py /app
COPY auction.py /app
COPY data.json /app
COPY read_excel.py /app
COPY booking.py /app
#install dependencies inside Docker container
USER root 
RUN pip install -U pip
RUN pip install -r requirements-actions.txt 
USER 1001 