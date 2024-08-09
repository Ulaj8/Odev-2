# Ulaş'ın E-ticaret Platformu

Bu proje, Pia Bootcamp için özel olarak geliştirilmiş bir e-ticaret platformu örneğidir. Flask, MySQL ve Nginx kullanılarak Docker-Compose ile konteynerize edilmiştir.

## Proje Yapısı

- **app/**: Flask uygulamasının bulunduğu dizin.
  - `app.py`: Flask uygulamasının ana dosyası.
  - `Dockerfile`: Flask uygulaması için Dockerfile.
  - `requirements.txt`: Flask uygulaması için gerekli Python paketlerini içeren dosya.
  
- **webserver/**: Nginx yapılandırma dosyalarının bulunduğu dizin.
  - `nginx.conf`: Nginx yapılandırma dosyası.
  - `Dockerfile`: Nginx için Dockerfile.

- **docker-compose.yml**: Tüm servisleri yönetmek için kullanılan Docker Compose dosyası.

## Gereksinimler

Bu projeyi çalıştırabilmek için aşağıdaki gereksinimlere sahip olmanız gerekir:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Kurulum ve Çalıştırma

Proje dizinine gidin ve aşağıdaki komutları çalıştırarak projeyi başlatın:

```bash
docker-compose up --build
