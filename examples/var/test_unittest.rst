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
    "message": "foo",
    "id": 1
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
    "message": "foo",
    "id": 1
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
