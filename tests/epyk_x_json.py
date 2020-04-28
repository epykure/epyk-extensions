
import config

import epyk
from epyk.core.Page import Report

rptObj = Report()


rptObj.ui.extension('epyk_x_json', 'js')

dt = rptObj.ui.js.json_formatter({"test": 185})


rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
