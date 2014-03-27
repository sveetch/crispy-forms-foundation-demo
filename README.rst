.. _docutils: http://docutils.sourceforge.net/
.. _Django: https://www.djangoproject.com/
.. _django-crispy-forms: https://github.com/maraujop/django-crispy-forms
.. _Foundation: http://github.com/zurb/foundation
.. _Foundation Grid: http://foundation.zurb.com/docs/grid.php
.. _crispy-forms-foundation: https://github.com/sveetch/crispy-forms-foundation

Introduction
============

This is a Django application to demonstrate crispy-forms-foundation.

Requires
========

* `crispy-forms-foundation`_ >= 0.2.4;

Install
=======

Edit your ``settings.py`` to add the following settings : ::

    INSTALLED_APPS = (
        ...
        'crispy_forms',
        'crispy_forms_foundation',
        'crispy_forms_foundation_demo'
        ...
    )

    CRISPY_TEMPLATE_PACK = 'foundation'

Then mount it on your urls : ::

    urlpatterns = patterns('',
        ...
        url(r'^crispies/', include('crispy_forms_foundation_demo.urls')),
        ...
    )

That's all, now you can access to the demo. Take care that some templates attempt to inherit from a ``skeleton.html`` template which use `Foundation`_ 5.
