=====
Usage
=====

To use DRF Service Token Authenticator in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'service_token_authenticator.apps.ServiceTokenAuthenticatorConfig',
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
