

from epyk.core.js import Imports


Imports.extend("json-pretty-formatter", [
  ('json-formatter.umd.min.js', "json-formatter-js@%(version)s/dist/"),
  ('json-formatter.css', "json-formatter-js@%(version)s/dist/"),
  ], version="2.3.4", cdnjs_url="https://cdn.jsdelivr.net/npm")
