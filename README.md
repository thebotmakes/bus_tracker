## bus_tracker
# Tracks the buses outside my house!

![alt text](https://github.com/thebotmakes/bus_tracker/blob/master/IMG_1109.jpg "tracker_image")

This project has been cooking for some time - ever since I found out I could get the bus times for the next two buses leaving from outside my house as JSON data via a link.  Uses a Raspberry Pi Zero with a Display-o-Tron from Pimoroni - I'm a sucker for an LCD display, and this has the nice feature of being able to adjust the background colour, which is ideal for this.  What it does:

* Gets the bus data for the stop outside my house (departure time, route no and destination - although I don't display destination - Display-o-Tron didn't have enough characters!)
* Gets the current date and time (although I didn't end up using date - see character issue above!)
* Calculate the number of minutes between the current time and the two departure times
* Converts this into a message (time, next bus route and minutes to next bus, then same details for the next bus after)
* Uses the minutes to next bus to derive a background colour (roughly 6 minutes (with a child in tow :-) ) to the bus stop, so colour = panic level!):
  * No bus data available - Blue
  * Over 10 minutes to next bus - Green
  * Over 6 minutes - Yellow
  * Under 6 minutes - Red
  
* Display the message on the LCD and change the backlight to the selected colour
