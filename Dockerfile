# IMPORTANT: Building an image ONLY for scanning voulnerabilities with Trivy pacakge in CI pipline.
FROM python:3.12.11-slim

# Set work directory
WORKDIR /app

# Copy project files
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables if needed
ENV PYTHONUNBUFFERED=1

# Default command (adjust as needed)
CMD ["pytest"]
