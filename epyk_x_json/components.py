

from epyk_x_json import html


class Components(object):

  alias = "js"

  def __init__(self, context):
    self.context = context

  def json_formatter(self, data, width=(None, "px"), height=(None, "px"), options=None, profile=False):
    """

    :param data:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    html_comp = html.HtmlPrettyJson(self.context.rptObj, data, width, height, options, profile)
    self.context.register(html_comp)
    return html_comp

