
from epyk.core.html import Html


class HtmlPrettyJson(Html.Html):
  __reqCss, __reqJs = ['json-pretty-formatter'], ['json-pretty-formatter']

  def __init__(self, report, data, width, height, options, profile):
    super(HtmlPrettyJson, self).__init__(report, data, profile=profile, css_attrs={"height": height, width: "width"})

  @property
  def jsonId(self):
    """
    Return the Javascript variable of the json object
    """
    return "%s_obj" % self.htmlId

  @property
  def _js__builder__(self):
    return '''
      window[ htmlObj.id + '_obj'] = new JSONFormatter(data, options.open, options.opts); htmlObj.innerHTML = '';
      htmlObj.appendChild(window[ htmlObj.id + '_obj'].render());
      '''

  def __str__(self):
    self._report._props.setdefault('js', {}).setdefault("builders", []).append(self.refresh())
    return '<div %s></div>' % (self.get_attrs(pyClassNames=self.style.get_classes()))
