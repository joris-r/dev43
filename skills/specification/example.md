# shorten: create and follow short links

A small HTTP service that shortens URLs.

## Data model

- Link
  - code: 6 characters from `a-z` and `0-9`, unique
  - url: an absolute `http` or `https` URL
  - hits: number of times the link was followed, 0 when created

## POST /links

```http
POST /links
Content-Type: application/json

{"url": "https://example.org/a/long/path"}
```

```http
HTTP/1.1 201 Created
Content-Type: application/json

{"code": "k3x9qa", "url": "https://example.org/a/long/path", "hits": 0}
```

- R1: Shortening a URL that already has a link returns that link, with
  status 200.

## GET /{code}

```http
GET /k3x9qa
```

```http
HTTP/1.1 302 Found
Location: https://example.org/a/long/path
```

- Each redirect adds 1 to `hits`.

## Errors

- Error responses are JSON: `{"error": "<message>"}`.
- 400: the body is not JSON, or `url` is missing or not an `http` or
  `https` URL.
- 404: unknown code.

## Technical

- R2: Codes are random, never derived from the URL or from a counter.
