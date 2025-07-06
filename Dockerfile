# Use official docker image for Python
FROM python:3.9-slim

# set working directory
WORKDIR /app

# copy files to container
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# expose port 5000
EXPOSE 5000

# run the app
CMD ["python", "app.py"]

