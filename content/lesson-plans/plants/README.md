## Updates

This is an updated version of the Plants notebooks, for "Jupyterlite" and the "Anywidget" module.

Now (March 2024) all the notebooks use the anywidget module, which runs on Jupyterlite as well as the Jupyter Lab and classic notebooks. 

- PhidgetFour_auto.ipynb:  Connects the phidgets to Plotly gauges, updates automatically
- PhidgetFour_read.ipynb:   Connects the phidgets to Plotly gauges, updates on button click
- plants-data-google-anywidget.ipynb: Connects the phidgets to Plotly gauges, posts to online spreadsheet
- plants-watering-anywidget.ipynb: Connects the phidgets to Plotly gauges, waters on a button click
- plants-watering-auto-anywidget.ipynb: Connects the phidgets to Plotly gauges, waters automatically

We have to remove the following notebook, as we were not able to figure out how to POST requests to Ethercalc in Jupyterlite:
- plants-data-ethercalc-anywidget.ipynb: Connects the phidgets to Plotly gauges, posts to online spreadsheet


## Limitations 

Successfully tested on:
- Mac OS in Chrome and Opera browsers
- Windows OS in Chrome browser
- Raspberry Pi in Chromium browser (latest OS and udev rules installed)

Important notes on Raspberry Pi:
- does not work with the old "buster" operating system
- does work on the latest operating system "bookworm". I have not tested others.
- it is important to install a file on the Raspberry Pi to allow access to the USB port, as follows:
- "Setting UDev Rules" on the page [https://www.phidgets.com/docs/OS_-_Linux](https://www.phidgets.com/docs/OS_-_Linux),
- basically you create a text file "99-libphidget22.rules" with the content indicated, and store it in  "/etc/udev/rules.d"

