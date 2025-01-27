FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN black . && isort .
# RUN flake8 . && black . --check && isort . --check-only
# CMD ["pytest", "&&", "python", "bot/main.py"]
CMD ["python", "bot/main.py"]
