# Define the python environement
FROM python:3.7.3-stretch


# Create a folder at the root of the container et make it the working directory
RUN mkdir /app
WORKDIR /app

ENV DOCKER_MODEL_VOLUME = "/model"
ENV DOCKER_OUTPUT_VOLUME = "/output"

# Copy the requirement txt in the working directory and install all the dependencies
# We make this first to throw error there if there is an error while installing dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt


# copy all the files in the repos
COPY . /app

# Launch the application
CMD python DL_model/train_def.py
