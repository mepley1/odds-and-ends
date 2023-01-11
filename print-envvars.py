# Print environment variables

import os

for param in os.environ.keys():
    print("%s:\n%s\n" % (param, os.environ[param]))
