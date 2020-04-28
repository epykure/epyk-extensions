
from epyk.core.js import JsUtils
from epyk.core.js.packages import JsPackage
from epyk.core.js.primitives import JsObjects


class JsDatepicker(JsPackage):

  def navigate(self, date):
    """
    Description:
    ------------
    Programmatically navigates the calendar to the date you provide.
    This doesn't select a date, it's literally just for navigation. You can optionally trigger the onMonthChange callback with the 2nd argument.

    Related Pages:

      https://www.npmjs.com/package/js-datepicker/v/5.11.0#navigate

    Attributes:
    ----------
    :param date:
    """
    date = JsUtils.jsConvertData(date, None)
    return JsObjects.JsObjects.get('%s.navigate(%s)' % (self.varName, date))

  def remove(self):
    """
    Description:
    ------------
    Performs cleanup. This will remove the current instance from the DOM, leaving all others in tact.
    If this is the only instance left, it will also remove the event listeners that Datepicker previously set up.

    Related Pages:

      https://www.npmjs.com/package/js-datepicker/v/5.11.0#remove
    """
    return JsObjects.JsObjects.get('%s.remove()' % self.varName)

  def setDate(self, date, update=True):
    """
    Description:
    ------------
    Allows you to programmatically select or unselect a date on the calendar.
    To select a date on the calendar, pass in a JS date object for the 1st argument.
    If you set a date on a month other than what's currently displaying and you want the calendar to automatically change to it, pass in true as the 2nd argument.

    Related Pages:

      https://www.npmjs.com/package/js-datepicker/v/5.11.0#setDate

    Attributes:
    ----------
    :param date:
    :param update:
    """
    date = JsUtils.jsConvertData(date, None)
    update = JsUtils.jsConvertData(update, None)
    return JsObjects.JsObjects.get('%s.setDate(%s, %s)' % (self.varName, date, update))

  def setMin(self, date):
    """
    Description:
    ------------
    Allows you to programmatically set the minimum selectable date or unset it.
    If this instance is part of a daterange instance (see the id option) then the other instance will be changed as well.
    To unset a minimum date, simply run the function with no arguments.

    Related Pages:

      https://www.npmjs.com/package/js-datepicker/v/5.11.0#setMin

    Attributes:
    ----------
    :param date:
    """
    date = JsUtils.jsConvertData(date, None)
    return JsObjects.JsObjects.get('%s.setMin(%s)' % (self.varName, date))

  def setMax(self, date):
    """
    Description:
    ------------
    Allows you to programmatically set the maximum selectable date or unset it.
    If this instance is part of a daterange instance (see the id option) then the other instance will be changed as well.
    To unset a maximum date, simply run the function with no arguments.

    Related Pages:

      https://www.npmjs.com/package/js-datepicker/v/5.11.0#setMax

    Attributes:
    ----------
    :param date:
    """
    date = JsUtils.jsConvertData(date, None)
    return JsObjects.JsObjects.get('%s.setMax(%s)' % (self.varName, date))

  def show(self):
    """
    Description:
    ------------
    Allows you to programmatically show the calendar. Using this method will trigger the onShow callback if your instance has one.

    :return:
    """
    return JsObjects.JsObjects.get('%s.show()' % self.varName)

  def hide(self):
    """
    Description:
    ------------
    Allows you to programmatically hide the calendar.
    If the alwaysShow property was set on the instance then this method will have no effect.
    Using this method will trigger the onHide callback if your instance has one.

    """
    return JsObjects.JsObjects.get('%s.hide()' % self.varName)

  def getRange(self):
    """
    Description:
    ------------
    This method is only available on daterange pickers.
    It will return an object with start and end properties whose values are JavaScript date objects representing what the user selected on both calendars.

    """
    return JsObjects.JsObjects.get('%s.getRange()' % self.getRange)
