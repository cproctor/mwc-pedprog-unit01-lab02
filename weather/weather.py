from weather.weather_apis import (
    geocode_location,
    geocode_ip_address,
    get_weather_office,
    get_forecast
)

def print_weather(location=None, metric=False, verbose=False):
    """Prints out a weather report using the provided location, or using
    the user's current location if no location was provided. 
    When metric is True, prints out the weather in metric units.
    When verbose is True, prints out a more detailed report. 
    """
    print("Not finished...") # YOUR CODE HERE!

# This is a clunky way to check whether this module was called directly with `python weather.py`,
# or whether it's being imported by another module. If the module is being called, then we
# should actually run `print_weather`. But if this module is just being imported, we probably don't
# want this module to call any functions. We'll leave that up whoever is doing the importing.
if __name__ == "__main__":
    print_weather()
