# https://www.npmjs.com/package/js-datepicker

from epyk.core.html import Html
from epyk.core.js import JsUtils

from epyk_x_js_datepicker import html_js
from epyk_x_js_datepicker import html_options
from epyk_x_js_datepicker import html_dom


class DatePicker(Html.Html):
  __reqCss, __reqJs = ['js-datepicker'], ['js-datepicker']

  def __init__(self, report, data, width, height, options, profile):
    super(DatePicker, self).__init__(report, data, profile=profile, css_attrs={"height": height, width: "width"})
    self.__options = html_options.OptsDatepicker(self, options)

  @property
  def _js__builder__(self):
    return '''new datepicker(htmlObj, options)'''

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

  def onSelect(self, jsFncs, profile=False):
    """
    Description:
    ------------
    Callback function after a date has been selected.
    The 2nd argument is the selected date when a date is being selected and undefined when a date is being unselected.
    You unselect a date by clicking it again.

    Related Pages:

			https://www.npmjs.com/package/js-datepicker/v/5.11.0#onselect

    Attributes:
    ----------
    :param jsFncs: A Javascript Python function
    :param profile: A Boolean. Set to true to get the profile for the function on the Javascript console
    """
    self._jsStyles['onShow'] = "(instance, date) => {%s}" % JsUtils.jsConvertFncs(jsFncs, toStr=True)
    return self

  def onShow(self, jsFncs, profile=False):
    """
    Description:
    ------------
    Callback function when the calendar is shown.

    Related Pages:

			https://www.npmjs.com/package/js-datepicker/v/5.11.0#onShow

    Attributes:
    ----------
    :param jsFncs: A Javascript Python function
    :param profile: A Boolean. Set to true to get the profile for the function on the Javascript console
    """
    self._jsStyles['onShow'] = "instance => {%s}" % JsUtils.jsConvertFncs(jsFncs, toStr=True)
    return self

  def onHide(self, jsFncs, profile=False):
    """
    Description:
    ------------
    Callback function when the calendar is hidden.

    Related Pages:

			https://www.npmjs.com/package/js-datepicker/v/5.11.0#onHide

    Attributes:
    ----------
    :param jsFncs: A Javascript Python function
    :param profile: A Boolean. Set to true to get the profile for the function on the Javascript console
    """
    self._jsStyles['onHide'] = "instance => {%s}" % JsUtils.jsConvertFncs(jsFncs, toStr=True)
    return self

  def onMonthChange(self, jsFncs, profile=False):
    """
    Description:
    ------------
    Callback function when the month has changed.

    Related Pages:

			https://www.npmjs.com/package/js-datepicker/v/5.11.0#onMonthChange

    Attributes:
    ----------
    :param jsFncs: A Javascript Python function
    :param profile: A Boolean. Set to true to get the profile for the function on the Javascript console
    """
    self._jsStyles['onMonthChange'] = "instance => {%s}" % JsUtils.jsConvertFncs(jsFncs, toStr=True)
    return self

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
      self._js = html_js.JsDatepicker(self._report, varName="datepicker('#%s')" % self.htmlId, setVar=False, parent=self)
    return self._js

  def __str__(self):
    #
    self._report._props.setdefault('js', {}).setdefault("builders", []).append(self.refresh())
    #
    return '<div %s></div>' % (self.get_attrs(pyClassNames=self.style.get_classes()))
