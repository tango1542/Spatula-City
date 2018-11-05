#!/usr/bin/env python
import os
import sys

# Done with the help of the tutorial from
# https://github.com/muvatech/Shopping-Cart-Using-Django-2.0-and-Python-3.6

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'retailproject.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
