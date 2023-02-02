# Broken http
Repository demonstrates unconventional http-usage

## Setup
- Clone repo
- Create environment
- Install `flask`
- Run `main.py`

## Usage
### Call with netcat (or telnet)
- Execute: `nc localhost 5000`
- Request with custom `ABRAKADABRA` method:
  ```http
  ABRAKADABRA /abra HTTP/1.1
  ```
- GET-request with body:
  ```http
  GET /getb HTTP/1.1
  Content-Type: application/x-www-form-urlencoded
  Content-Length: 21

  title=Anime one love!
  ```
- POST-request with query-parameters:
  ```http
  POST /postq?q=QueryExample&p=999 HTTP/1.1
  ```
- Equivalent requests with different methods:
  ```http
  GET /?q=Query-Anime HTTP/1.1
  Content-Type: application/x-www-form-urlencoded
  Content-Length: 16

  title=Body-Anime
  ```
  ```http
  POST /?q=Query-Anime HTTP/1.1
  Content-Type: application/x-www-form-urlencoded
  Content-Length: 16

  title=Body-Anime
  ```


### Call with curl
- Request with custom `ABRAKADABRA` method:
  ```bash
  curl -X ABRAKADABRA localhost:5000/abra
  ```
- GET-Request with body:
  ```bash
  curl -X GET localhost:5000/getb -d "title=Anime one love\!"
  ```
- POST-Request with query-parameters:
  ```bash
  curl -X POST "localhost:5000/postq?q=QueryExample&p=999"
  ```
- Equivalent requests with different methods:
  ```bash
  curl -X GET 'localhost:5000?q=Query-Anime' -d 'title=Body-Anime'
  ```
  ```bash
  curl -X POST 'localhost:5000?q=Query-Anime' -d 'title=Body-Anime'
  ```
