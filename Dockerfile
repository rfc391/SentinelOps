FROM python:3.9-slim
WORKDIR /app

# Copy only required files to avoid context-related errors
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app

EXPOSE 5000
CMD ["python", "app.py"]

# Install gRPC tools
RUN pip install grpcio grpcio-tools
