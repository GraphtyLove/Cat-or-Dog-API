# Define the python environement
FROM python:3.7.3-stretch


# Create a folder at the root of the container et make it the working directory
RUN mkdir /test-21-08
WORKDIR /test-21-08


# Copy the requirement txt in the working directory and install all the dependencies
# We make this first to throw error there if there is an error while installing dependencies
COPY requirements.txt /test-21-08/
RUN pip install -r requirements.txt


# copy all the files in the repos
COPY . /test-21-08/

# Specify the port
EXPOSE $PORT

# Launch the application
CMD python app.py
