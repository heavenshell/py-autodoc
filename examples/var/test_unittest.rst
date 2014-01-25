POST /foo/bar
=============

Target Server
-------------

http://localhost:80

Request
-------
::

  POST /foo/bar

Parameters
----------

::

  {
  "id": 1, 
  "message": "foo"
}

Response
--------

::

  Status:       200
  Content-Type: application/json
  Response:
  {
  "response": "foo_bar"
}

GET /
=====

Target Server
-------------

http://localhost:80

Request
-------
::

  GET /

Parameters
----------

::

  

Response
--------

::

  Status:       200
  Content-Type: application/json
  Response:
  {
  "response": "index"
}

POST /
======

Target Server
-------------

http://localhost:80

Request
-------
::

  POST /

Parameters
----------

::

  {
  "id": 1, 
  "message": "foo"
}

Response
--------

::

  Status:       200
  Content-Type: application/json
  Response:
  {
  "response": "create"
}
