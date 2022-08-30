=============================
DRF Service Token Authenticator
=============================

.. image:: https://badge.fury.io/py/drf-service-token-authenticator.svg/?style=flat-square
    :target: https://badge.fury.io/py/drf-service-token-authenticator

.. image:: https://readthedocs.org/projects/pip/badge/?version=latest&style=flat-square
    :target: https://drf-service-token-authenticator.readthedocs.io/en/latest/

.. image:: https://img.shields.io/coveralls/github/frankhood/drf-service-token-authenticator/main?style=flat-square
    :target: https://coveralls.io/github/frankhood/drf-service-token-authenticator?branch=main
    :alt: Coverage Status

This package provides a drf authentication_class for your apis using a settings variable to define the service tokens

Documentation
-------------

The full documentation is at https://drf-service-token-authenticator.readthedocs.io.

Quickstart
----------

Install DRF Service Token Authenticator::

    pip install drf-service-token-authenticator

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'service_token_authenticator',
        ...
    )

Add DRF Service Token Authenticator's URL patterns:

.. code-block:: python

    from service_token_authenticator import urls as service_token_authenticator_urls


    urlpatterns = [
        ...
        url(r'^', include(service_token_authenticator_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox


Development commands
---------------------

::

    pip install -r requirements_dev.txt
    invoke -l


Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
