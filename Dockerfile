FROM python:3.10-slim


# Set working directory
WORKDIR /app

# Copy files
COPY . .

# Install Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 8080

# Start Flask app
CMD ["python", "app.py"]
