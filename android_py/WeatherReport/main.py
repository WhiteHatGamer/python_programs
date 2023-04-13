"""Speak the weather."""

__author__ = 'T.V. Raman <raman@google.com>'
__copyright__ = 'Copyright (c) 2009, Google Inc.'
__license__ = 'Apache License, Version 2.0'

import androidhelper
import weather


def say_weather(droid):
  """Speak the weather at the current location."""
  
  msg = 'Failed to find location.'
  location = droid.getLastKnownLocation().result
  location = location.get('gps') or location.get('network')
  if location is not None:
    print('Finding ZIP code.')
    addresses = droid.geocode(location['latitude'], location['longitude'])
    zip = addresses.result[0]['postal_code']
    if zip is not None:
      print('Fetching weather report.')
      result = weather.fetch_weather(zip)
      # Format the result for speech.
      msg = '%(temperature)s degrees and %(conditions)s, in %(city)s.' % result
  droid.ttsSpeak(msg)


if __name__ == '__main__':
  droid = androidhelper.Android()
  say_weather(droid)
