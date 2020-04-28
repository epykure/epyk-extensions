
from epyk_x_js_datepicker import html


class Components(object):

  alias = "dt"

  def __init__(self, context):
    self.context = context

  def datepicker(self, data, width=(None, "px"), height=(None, "px"), options=None, profile=False):
    """

    :param data:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    html_date = html.DatePicker(self.context.rptObj, data, width, height, options, profile)
    self.context.register(html_date)
    return html_date

