# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'locationsaver_dialog_base.ui'
#
# Created: Wed Nov 26 15:22:24 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_locationsaverDialogBase(object):
    def setupUi(self, locationsaverDialogBase):
        locationsaverDialogBase.setObjectName(_fromUtf8("locationsaverDialogBase"))
        locationsaverDialogBase.resize(400, 300)
        self.button_box = QtGui.QDialogButtonBox(locationsaverDialogBase)
        self.button_box.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.button_box.setObjectName(_fromUtf8("button_box"))

        self.retranslateUi(locationsaverDialogBase)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("accepted()")), locationsaverDialogBase.accept)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("rejected()")), locationsaverDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(locationsaverDialogBase)

    def retranslateUi(self, locationsaverDialogBase):
        locationsaverDialogBase.setWindowTitle(_translate("locationsaverDialogBase", "locationsaver", None))

