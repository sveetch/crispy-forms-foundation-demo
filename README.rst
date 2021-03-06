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

* `crispy-forms-foundation`_ >= 0.5.0;

Install
=======

Edit your ``settings.py`` to add the following settings :

.. sourcecode:: python

    INSTALLED_APPS = (
        ...
        'crispy_forms',
        'crispy_forms_foundation',
        'crispy_forms_foundation_demo'
        ...
    )

    CRISPY_TEMPLATE_PACK = 'foundation-5'

Then mount it on your urls :

.. sourcecode:: python

    urlpatterns = patterns('',
        ...
        url(r'^crispies/', include('crispy_forms_foundation_demo.urls')),
        ...
    )

And finally, some templates attempt to inherit from a ``skeleton.html`` template where you should load your Foundation assets (CSS and JS), here is a sample of this template you should create into your templates directory:

.. sourcecode:: django

    <!DOCTYPE html>
    <!--[if IE 8]> <html class="no-js lt-ie9" lang="en"> <![endif]-->
    <!--[if gt IE 8]><!--> <html class="no-js" lang="en"> <!--<![endif]-->
    <head>
        <meta charset="utf-8">
        <title>{% block head_title %}Sample skeleton{% endblock %}</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        {% block header_content %}{% spaceless %}
            {% block head_base_links %}
                <link rel="stylesheet" href="{{ STATIC_URL }}css/foundation.min.css">
            {% endblock %}
            {% block head_base_js %}
                <script type="text/javascript" src="{{ STATIC_URL }}js/foundation.min.js"></script>
            {% endblock %}
            
        {% endspaceless %}{% endblock %}
    </head>

    <body>

        {% block content_container %}<div id="body_content"{% block content_container_attrs %}{% endblock %}>
            {% block base_content %}{% endblock %}
        </div>{% endblock %}

        {% block foot_more_js %}{% endblock %}
    </body>
    </html>

That's all, now you can access to the demo. 
