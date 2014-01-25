## POST /foo/bar

### Target Server

http://localhost:80

### Parameters

{
  "id": 1, 
  "message": "foo"
}

### Request

POST /foo/bar

### Response

```
Status:       200
Content-Type: application/json
Response:
{
  "response": "foo_bar"
}
```

## GET /

### Target Server

http://localhost:80

### Parameters



### Request

GET /

### Response

```
Status:       200
Content-Type: application/json
Response:
{
  "response": "index"
}
```

## POST /

### Target Server

http://localhost:80

### Parameters

{
  "id": 1, 
  "message": "foo"
}

### Request

POST /

### Response

```
Status:       200
Content-Type: application/json
Response:
{
  "response": "create"
}
```
