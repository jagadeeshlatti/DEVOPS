FROM python:3.11

RUN apt-get update \
    && apt-get install -y \
        curl \
        libxrender1 \
        libfontconfig \
        libxtst6 \
        xz-utils \
        gcc \
        wget
RUN wget -P /downloads http://archive.ubuntu.com/ubuntu/pool/main/o/openssl/libssl1.1_1.1.1f-1ubuntu2_amd64.deb \
    && apt install -f /downloads/libssl1.1_1.1.1f-1ubuntu2_amd64.deb

RUN wget -P /downloads https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6.1-2/wkhtmltox_0.12.6.1-2.bullseye_amd64.deb \
    && apt install -f -y /downloads/wkhtmltox_0.12.6.1-2.bullseye_amd64.deb
    
# RUN apt-get install wkhtmltopdf

# RUN apk update && apk upgrade
# RUN apk add build-base
# RUN apk add --no-cache wkhtmltopdf

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

RUN python manage.py makemigrations
RUN python manage.py migrate

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]