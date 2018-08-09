"""
Custom system checks for the :py:mod:`smsjwplatform` application.

.. seealso::

    The `Django System Check Framework <https://docs.djangoproject.com/en/2.0/ref/checks/>`_.

"""
from django.conf import settings
from django.core.checks import register, Error


@register
def required_settings_check(app_configs, **kwargs):
    """
    A system check ensuring that all required settings are specified.

    .. seealso:: https://docs.djangoproject.com/en/2.0/ref/checks/

    """
    # Check that all required settings are specified and non-None
    required_settings = [
        'OAUTH2_LOOKUP_SCOPES',
        'LOOKUP_OAUTH2_SCOPES',
        'LOOKUP_ROOT',
        'LOOKUP_PEOPLE_CACHE_LIFETIME'
    ]

    errors = []

    for idx, name in enumerate(required_settings):
        value = getattr(settings, name, None)
        if value is None or value == '':
            errors.append(Error(
                'Required setting {} not set'.format(name),
                id='assets.E{:03d}'.format(idx + 1),
                hint='Add {} to settings.'.format(name)))

    return errors
