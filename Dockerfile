FROM python:3.10

WORKDIR /app

COPY . /app

RUN pip install streamlit pandas matplotlib openpyxl

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0"]