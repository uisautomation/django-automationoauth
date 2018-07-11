#!/usr/bin/env python
import sys

import django

from django.conf import settings
from django.core.management import call_command

settings.configure(
    DEBUG=True,
    INSTALLED_APPS=(
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'automationoauth',
        'automationlookup',
    ),
)

django.setup()
call_command('makemigrations', *sys.argv[1:])
