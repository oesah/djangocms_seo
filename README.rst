=============================
DjangoCMS SEO
=============================

.. image:: https://badge.fury.io/py/djangocms-seo.svg
    :target: https://badge.fury.io/py/djangocms-seo

.. image:: https://travis-ci.org/oesah/djangocms-seo.svg?branch=master
    :target: https://travis-ci.org/oesah/djangocms-seo

.. image:: https://codecov.io/gh/oesah/djangocms_seo/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/oesah/djangocms_seo

The missing SEO App for DjangoCMS.

Developed by: oesahIT_.

.. _oesahIT: https://www.oesah.de/



Documentation
-------------

The full documentation is at https://djangocms-seo.readthedocs.io.

Quickstart
----------

Install DjangoCMS SEO::

    pip install djangocms-seo

Add it to your `INSTALLED_APPS`:

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

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage


Sponsorship
-----------

This project is maintained by `Mathison AG | Mobile & Web Development <https://mathison.ch>`_.
