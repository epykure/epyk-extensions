
import os
import config

import sys
sys.path.append("../epyk-ui")

module = "epyk_x_json"


for py_file in os.listdir("tests"):
  if py_file.endswith(".py") and py_file != '__init__.py':
    script = py_file.replace(".py", "")
    if module is None:
      config.OUT_FILENAME ="%s.html" % script
      __import__("tests.%s" % script)

    elif module == script:
      config.OUT_FILENAME = "%s.html" % script
      __import__("tests.%s" % script)
