POST /foo/bar
=============

Target Server
-------------

http://localhost:5000/foo/bar

Request
-------
::

  POST /

Parameters
----------

::

  {
    "message": "foo",
    "id": "1"
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

GET /
=====

Target Server
-------------

http://localhost:5000/

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

http://localhost:5000/

Request
-------
::

  POST /

Parameters
----------

::

  {
    "message": "foo",
    "id": "1"
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
