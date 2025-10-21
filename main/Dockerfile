# -------------------------------
# Flask Dockerfile
# -------------------------------

# 1. Use a lightweight Python image
FROM python:3.12-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy all files from your local main/ folder into the container
COPY . .

# 4. Install Flask (and any other dependencies)
RUN pip install flask

# 5. Expose the port Flask runs on
EXPOSE 5000

# 6. Set the default command to run the app
CMD ["python", "app.py"]
