dogetrack
=========

![dogetrack](screenshot.png?raw=true)

dogetrack is a Bitcoin and Dogecoin price tracker that lives in your system tray. When you click on the icon, it gives the following prices:

* BTC/USD (Coinbase)
* DOGE/BTC (Cryptsy)
* DOGE/USD

Additionally, if you edit the settings.json file in the dogetrack directory you can get extra information. If you set 'doge_owned' to your dogecoin balance, dogetrack will display:

* USD value of your dogecoin

If in addition to 'doge_owned', you set 'usd_invested' to the amount of USD you have spent on dogecoin, dogetrack will display:

* profit in USD

A Windows 32 binary is available on the [releases page](https://github.com/aaron-lebo/dogetrack/releases).

dogetrack uses Python 2.7 and Qt 4.8.5 (PySide 1.2.1). Binaries are compiled using PyInstaller and dogetrack.spec for compilation on other architectures is included.

Icon from [Ionicons](http://ionicons.com/).

Based on:

http://stackoverflow.com/questions/893984/pyqt-show-menu-in-a-system-tray-application
http://rowinggolfer.blogspot.com/2011/06/pyqt-qsystrayicon-example.html

Suggestions and pull requests welcome.

Tips appreciated:

DQrzSAHX1XSYCJc4VK736tYqsLxV2hGtan
