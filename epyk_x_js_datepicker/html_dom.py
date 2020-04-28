
from epyk.core.js.html import JsHtml

from epyk.core.js.primitives import JsNumber
from epyk.core.js.primitives import JsDate
from epyk.core.js.primitives import JsString


class DomDatePicker(JsHtml.JsHtmlRich):

  @property
  def content(self):
    """
    Description:
    ------------

    """
    return JsHtml.ContentFormatters(self._report, '%s.dateSelected' % self._src.js.varName)

  @property
  def currentMonth(self):
    """
    Description:
    ------------
    A 0-index number representing the current month. For example, 0 represents January.

    :return:
    """
    return JsNumber.JsNumber("%s.currentMonth" % self._src.js.varName, report=self._report)

  @property
  def currentMonthName(self):
    """
    Description:
    ------------
    Calendar month in plain english. E.x. January

    :return:
    """
    return JsString.JsString("%s.currentYear" % self._src.js.varName, report=self._report)

  @property
  def currentYear(self):
    """
    Description:
    ------------
    The current year. E.x. 2099

    :return:
    """
    return JsNumber.JsNumber("%s.currentYear" % self._src.js.varName, report=self._report)

  @property
  def dateSelected(self):
    """
    Description:
    ------------
    The value of the selected date. This will be undefined if no date has been selected yet.

    :return:
    """
    return JsDate.JsDate("%s.dateSelected" % self._src.js.varName, report=self._report)

  @property
  def minDate(self):
    """
    Description:
    ------------
    The minimum selectable date.

    :return:
    """
    return JsDate.JsDate("%s.minDate" % self._src.js.varName, report=self._report)

  @property
  def maxDate(self):
    """
    Description:
    ------------
    The maximum selectable date.

    :return:
    """
    return JsDate.JsDate("%s.maxDate" % self._src.js.varName, report=self._report)

  def empty(self):
    """
    Description:
    ------------

    :return:
    """
    return self._src.js.setDate()
