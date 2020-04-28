
from epyk.core.html.options import Options


class OptsDatepicker(Options):

  @property
  def position(self):
    """
    Description:
    ------------
    This option positions the calendar relative to the <input> field it's associated with.
    This can be 1 of 5 values: 'tr', 'tl', 'br', 'bl', 'c' representing top-right, top-left, bottom-right, bottom-left, and centered respectively

    Related Pages:

      https://www.npmjs.com/package/js-datepicker/v/5.11.0#position
    """
    return self._config_get('bl')

  @position.setter
  def position(self, value):
    self._config(value)

  @property
  def startDay(self):
    """
    Description:
    ------------
    Specify the day of the week your calendar starts on. 0 = Sunday, 1 = Monday, etc.
    Plays nice with the customDays option.

    Related Pages:

      https://www.npmjs.com/package/js-datepicker/v/5.11.0#startDay
    """
    return self._config_get(0)

  @startDay.setter
  def startDay(self, num):
    self._config(num)

  @property
  def customDays(self):
    """
    Description:
    ------------
    You can customize the display of days on the calendar by providing an array of 7 values.
    This can be used with the startDay option if your week starts on a day other than Sunday.

    Related Pages:

      https://www.npmjs.com/package/js-datepicker/v/5.11.0#customDays

    :params names: list.
    """
    return self._config_get(['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'])

  @customDays.setter
  def customDays(self, names):
    self._config(names)

  @property
  def customMonths(self):
    """
    Description:
    ------------
    You can customize the display of the month name at the top of the calendar by providing an array of 12 strings.

    Related Pages:

      https://www.npmjs.com/package/js-datepicker/v/5.11.0#customDays
    """
    return self._config_get(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])

  @customMonths.setter
  def customMonths(self, names):
    self._config(names)

  @property
  def customOverlayMonths(self):
    """
    Description:
    ------------
    You can customize the display of the month names in the overlay view by providing an array of 12 strings.
    Keep in mind that if the values are too long, it could produce undesired results in the UI.

    Related Pages:

      https://www.npmjs.com/package/js-datepicker/v/5.11.0#customOverlayMonths
    """
    return self._config_get(True)

  @customOverlayMonths.setter
  def customOverlayMonths(self, value):
    self._config(value)

  @property
  def overlayButton(self):
    """
    Description:
    ------------
    Custom text for the year overlay submit button.

    Related Pages:

      https://www.npmjs.com/package/js-datepicker/v/5.11.0#overlayButton
    """
    return self._config_get(None)

  @overlayButton.setter
  def overlayButton(self, value):
    self._config(value)

  @property
  def overlayPlaceholder(self):
    """
    Description:
    ------------
    Custom placeholder text for the year overlay.

    Related Pages:

      https://www.npmjs.com/package/js-datepicker/v/5.11.0#overlayPlaceholder
    """
    return self._config_get(None)

  @overlayPlaceholder.setter
  def overlayPlaceholder(self, value):
    self._config(value)

  @property
  def events(self):
    """
    Description:
    ------------
    An array of dates which indicate something is happening - a meeting, birthday, etc. I.e. an event.

    Related Pages:

      https://www.npmjs.com/package/js-datepicker/v/5.11.0#events
    """
    return self._config_get(None)

  @events.setter
  def events(self, values):
    self._config(values)

  @property
  def dateSelected(self):
    """
    Description:
    ------------
    This will start the calendar with a date already selected.
    If Datepicker is used with an <input> element, that field will be populated with this date as well.

    Related Pages:

      https://www.npmjs.com/package/js-datepicker/v/5.11.0#dateSelected
    """
    return self._config_get(None)

  @dateSelected.setter
  def dateSelected(self, dt):
    self._config(dt)

  @property
  def showAllDates(self):
    """
    Description:
    ------------
    By default, the datepicker will not put date numbers on calendar days that fall outside the current month.

    Related Pages:

      https://www.npmjs.com/package/js-datepicker/v/5.11.0#showAllDates
    """
    return self._config_get(True)

  @showAllDates.setter
  def showAllDates(self, bool):
    self._config(bool)

  @property
  def respectDisabledReadOnly(self):
    """
    Description:
    ------------
    <input />'s can have a disabled or readonly attribute applied to them.
    In those cases, you might want to prevent Datepicker from selecting a date and changing the input's value.

    Related Pages:

      https://www.npmjs.com/package/js-datepicker/v/5.11.0#respectDisabledReadOnly
    """
    return self._config_get(True)

  @respectDisabledReadOnly.setter
  def respectDisabledReadOnly(self, bool):
    self._config(bool)

  @property
  def noWeekends(self):
    """
    Description:
    ------------
    Provide true to disable selecting weekends. Weekends are Saturday & Sunday.
    If your weekends are a set of different days or you need more control over disabled dates, check out the disabler option.

    Related Pages:

      https://www.npmjs.com/package/js-datepicker/v/5.11.0#noWeekends
    """
    return self._config_get(True)

  @noWeekends.setter
  def noWeekends(self, bool):
    self._config(bool)

  @property
  def disabler(self):
    """
    Description:
    ------------
    Sometimes you need more control over which dates to disable.
    The disabledDates option is limited to an explicit array of dates and the noWeekends option is limited to Saturdays & Sundays.

    Related Pages:

      https://www.npmjs.com/package/js-datepicker/v/5.11.0#disabler
    """
    return self._config_get(True)

  @disabler.setter
  def disabler(self, bool):
    self._config(bool)

  @property
  def disabledDates(self):
    """
    Description:
    ------------
    Provide an array of JS date objects that will be disabled on the calendar.
    This array cannot include the same date as dateSelected.
    If you need more control over which dates are disabled, see the disabler option.

    Related Pages:

      https://www.npmjs.com/package/js-datepicker/v/5.11.0#disabledDates
    """
    return self._config_get(None)

  @disabledDates.setter
  def disabledDates(self, dts):
    self._config(dts)

  @property
  def startDate(self):
    """
    Description:
    ------------
    The date you provide will determine the month that the calendar starts off at.

    Related Pages:

      https://www.npmjs.com/package/js-datepicker/v/5.11.0#startDate
    """
    return self._config_get(None)

  @startDate.setter
  def startDate(self, dt):
    self._config(dt)

  @property
  def minDate(self):
    """
    Description:
    ------------
    This will be the minumum threshold of selectable dates. Anything prior will be unselectable.

    Related Pages:

      https://www.npmjs.com/package/js-datepicker/v/5.11.0#minDate
    """
    return self._config_get(None)

  @minDate.setter
  def minDate(self, dt):
    self._config(dt)

  @property
  def maxDate(self):
    """
    Description:
    ------------
    This will be the maximum threshold of selectable dates. Anything after it will be unselectable.

    Related Pages:

      https://www.npmjs.com/package/js-datepicker/v/5.11.0#maxDate
    """
    return self._config_get(None)

  @maxDate.setter
  def maxDate(self, dt):
    self._config(dt)

  @property
  def alwaysShow(self):
    """
    Description:
    ------------
    By default, the datepicker will hide & show itself automatically depending on where you click or focus on the page.
    If you want the calendar to always be on the screen, use this option.

    Related Pages:

      https://www.npmjs.com/package/js-datepicker/v/5.11.0#alwaysShow
    """
    return self._config_get(False)

  @alwaysShow.setter
  def alwaysShow(self, bool):
    self._config(bool)

  @property
  def disableYearOverlay(self):
    """
    Description:
    ------------
    Clicking the year or month name on the calendar triggers an overlay to show, allowing you to enter a year manually.
    If you want to disable this feature, set this option to true.

    Related Pages:

      https://www.npmjs.com/package/js-datepicker/v/5.11.0#disableYearOverlay
    """
    return self._config_get(True)

  @disableYearOverlay.setter
  def disableYearOverlay(self, bool):
    self._config(bool)

