# https://www.npmjs.com/package/js-datepicker

from epyk.core.html import Html

import html_js
import html_options
import html_dom


class DatePicker(Html.Html):
  __reqCss, __reqJs = ['json-formatter'], ['json-formatter']

  def __init__(self, report, data, width, height, options, profile):
    super(DatePicker, self).__init__(report, data, profile=profile, css_attrs={"height": height, width: "width"})
    self.__options = html_options.OptsDatepicker(self, options)

  @property
  def dateId(self):
    """
    Description:
    ------------
    """
    return "%s_obj" % self.htmlId

  @property
  def _js__builder__(self):
    return '''
      window[ htmlObj.id + '_obj'] = new JSONFormatter(data, options.open, options.opts); htmlObj.innerHTML = '';
      htmlObj.appendChild(window[ htmlObj.id + '_obj'].render());
      '''

  @property
  def dom(self):
    """
    Description:
    -----------
    HTML Dom object

    :rtype: html_dom.DomDatePicker
    """
    if self._dom is None:
      self._dom = html_dom.DomDatePicker(self, report=self._report)
    return self._dom

  @property
  def options(self):
    """
    Description:
    ------------

    :rtype: html_options.OptsDatepicker
    """
    return self.__options

  @property
  def js(self):
    """
    Description:
    ------------
    Return the Javascript internal object

    :return: A Javascript object

    :rtype: html_js.JsDatepicker
    """
    if self._js is None:
      self._js = html_js.JsDatepicker(self._report, varName=self.jsonId, setVar=False, parent=self)
    return self._js

  def __str__(self):
    #
    self._report._props.setdefault('js', {}).setdefault("builders", []).append(self.refresh())
    #
    return '<div %s></div>' % (self.get_attrs(pyClassNames=self.style.get_classes()))
