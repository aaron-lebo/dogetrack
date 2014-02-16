import datetime
from json import load
from urllib2 import urlopen

from PySide import QtGui

class Icon(QtGui.QSystemTrayIcon):
    def __init__(self):
        QtGui.QSystemTrayIcon.__init__(self, QtGui.QIcon('dogetrack.png'))
        self.activated.connect(self.activate)
        self.fetch()

    def activate(self, value):
        if self.time < datetime.datetime.now() - datetime.timedelta(minutes=5):
            self.fetch()

        menu = QtGui.QMenu()
        menu.addAction(self.time.strftime('%m/%d/%y %I:%M %p'))
        menu.addSeparator()
        menu.addAction(self.btc_usd)
        menu.addAction(self.doge_btc)
        menu.addAction(str(self.doge_usd))
        if self.doge_owned and self.usd is not None:
            menu.addAction('%.2f' % self.usd)
        if self.usd_invested and self.profit is not None:
            menu.addAction('%.2f' % self.profit)
        menu.addSeparator()
        exit = menu.addAction('Exit')
        exit.triggered.connect(QtGui.qApp.quit)
        menu.exec_(QtGui.QCursor.pos())

    def fetch(self):
        self.time = datetime.datetime.now()

        try:
            file = open('settings.json')
            settings = load(file)
            self.doge_owned = float(settings['doge_owned'])
            self.usd_invested = float(settings['usd_invested'])
            file.close()
        except:
            self.doge_owned = None
            self.usd_invested = None

        try:
            coinbase = load(urlopen('https://coinbase.com/api/v1/prices/buy'))
            self.btc_usd = coinbase['total']['amount']
        except:
            self.btc_ucd = 'N/A'

        try:
            cryptsy = load(urlopen('http://pubapi.cryptsy.com/api.php?method=singlemarketdata&marketid=132'))
            self.doge_btc = cryptsy['return']['markets']['DOGE']['recenttrades'][0]['price']
        except:
            self.doge_btc = 'N/A'

        try:
            self.doge_usd = float(self.btc_usd) * float(self.doge_btc)
        except:
            self.doge_usd = 'N/A'

        try:
            self.usd = float(self.doge_usd) * self.doge_owned
        except:
            self.usd = None

        try:
            self.profit = float(self.usd) - self.usd_invested
        except:
            self.profit = None

if __name__ == '__main__':
  app = QtGui.QApplication([])
  icon = Icon()
  icon.show()
  app.exec_()
