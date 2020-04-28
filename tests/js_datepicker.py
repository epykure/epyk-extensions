
import config

import epyk
from epyk.core.Page import Report

rptObj = Report()


rptObj.ui.extension('epyk_x_js_datepicker', 'dt')

dt = rptObj.ui.dt.datepicker("")


rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
