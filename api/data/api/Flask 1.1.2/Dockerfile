FROM python:3-stretch
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN apt-get -y update
RUN apt-get -y install python-pyodbc

# Install Official Microsoft SQL Server Driver and ODBC
RUN apt-get update && \
    apt-get install -y apt-transport-https && \
    curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    curl https://packages.microsoft.com/config/debian/9/prod.list > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && \
    ACCEPT_EULA=Y apt-get install msodbcsql17 unixodbc-dev -y

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]