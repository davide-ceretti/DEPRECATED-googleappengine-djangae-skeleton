#!/usr/bin/env python
import os
import sys
import site
import os.path

# add `lib` subdirectory as a site packages directory,
# so our `main` module can load  third-party libraries.
site.addsitedir(os.path.join(os.path.dirname(__file__), '../lib'))

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "application.settings")

    from djangae.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
