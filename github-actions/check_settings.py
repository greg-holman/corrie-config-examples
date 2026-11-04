"""Check that the settings a deploy needs are there before it runs (standard library only).

The workflow starts this through the Corrie Config launcher, so the variables come from
config.corrie.io. It prints the names it found, never the values, and exits 1 if any are missing.
"""
import os
import sys

REQUIRED = ["API_URL", "DB_HOST", "DB_POOL"]

missing = [name for name in REQUIRED if not os.environ.get(name)]
if missing:
    print("Missing settings: " + ", ".join(missing))
    sys.exit(1)

if not os.environ["API_URL"].startswith("https://"):
    print("API_URL should start with https://")
    sys.exit(1)

print("All %d required settings are present: %s" % (len(REQUIRED), ", ".join(REQUIRED)))
print("New checkout is %s." % ("on" if os.environ.get("FEATURE_NEW_CHECKOUT") == "true" else "off"))
