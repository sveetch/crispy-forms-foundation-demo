.. _docutils: http://docutils.sourceforge.net/
.. _Django: https://www.djangoproject.com/
.. _django-crispy-forms: https://github.com/maraujop/django-crispy-forms
.. _Foundation: http://github.com/zurb/foundation
.. _Foundation Grid: http://foundation.zurb.com/docs/grid.php
.. _crispy-forms-foundation: https://github.com/sveetch/crispy-forms-foundation

Introduction
============

This is a Django application to demonstrate `crispy-forms-foundation`_ using `django-crispy-forms`_ with `Foundation`_.

Links
*****

* Download his `PyPi package <http://pypi.python.org/pypi/crispy-forms-foundation-demo>`_;
* Clone it on his `Github repository <https://github.com/sveetch/crispy-forms-foundation-demo>`_;

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

    CRISPY_TEMPLATE_PACK = 'foundation-5'

You can also use the template pack name ``foundation-3``.

Then mount it on your urls : ::

    urlpatterns = patterns('',
        ...
        url(r'^crispies/', include('crispy_forms_foundation_demo.urls')),
        ...
    )

That's all, now you can access to the demo. Take care that some templates attempt to inherit from a ``skeleton.html`` template which use `Foundation`_.
