FROM python:3.10
EXPOSE 3000
WORKDIR /app
RUN pip install flask requests
COPY . .
CMD ["flask", "run", "--host", "0.0.0.0", "--debug", "--port", "3000"]