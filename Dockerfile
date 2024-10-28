FROM python:3.8.5-slim-buster
# Update and install locales
RUN apt-get update -y && apt-get install -y \
    awscli \
    locales \
    && locale-gen en_IN.UTF-8
# Create the locale definition file for en_IN.UTF-8
RUN echo 'en_IN.UTF-8 UTF-8' >> /etc/locale.gen && locale-gen
# Set environment variables for locale
ENV LANG=en_IN.UTF-8
ENV LANGUAGE=en_IN:en
ENV LC_ALL=en_IN.UTF-8
# Upgrade pip to the latest version and set a longer timeout
RUN pip install --upgrade pip && \
    pip config set global.timeout 1000
# Set the working directory
WORKDIR /app
# Copy the application code
COPY . /app
# Install Python dependencies
RUN pip install -r requirements.txt
# Command to run the application
CMD ["python3", "app.py"]