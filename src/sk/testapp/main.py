# encoding: utf-8

from PyQt4 import QtGui
import sys


def main():
    app = QtGui.QApplication(sys.argv)
    w = QtGui.QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle(u'Test App')
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
