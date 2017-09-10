=====
Usage
=====

To use DjangoCMS SEO in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'djangocms_seo.apps.DjangocmsSeoConfig',
        ...
    )

Add DjangoCMS SEO's URL patterns:

.. code-block:: python

    from djangocms_seo import urls as djangocms_seo_urls


    urlpatterns = [
        ...
        url(r'^', include(djangocms_seo_urls)),
        ...
    ]
