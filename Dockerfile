
FROM python:3.10


ENV PYTHONUNBUFFERED=1


WORKDIR /AuthenticationServices


COPY . /AuthenticationServices/

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose the port Django runs on
EXPOSE 8000

# Command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
