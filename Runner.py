
import os
import config


module = "epyk_x_js_datepicker"


for py_file in os.listdir("tests"):
  if py_file.endswith(".py") and py_file != '__init__.py':
    config.OUT_FILENAME = module.replace(".py", ".html")
    __import__("tests.%s" % py_file[:-3])
