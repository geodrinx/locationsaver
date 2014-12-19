# -*- coding: utf-8 -*-
"""
/***************************************************************************
 locationsaver
                                 A QGIS plugin
 locationsaver
                              -------------------
        begin                : 2014-11-26
        git sha              : $Format:%H$
        copyright            : (C) 2014 by geodrinx
        email                : geodrinx@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from PyQt4.QtCore import QSettings, QTranslator, qVersion, QCoreApplication
from PyQt4.QtGui import QAction, QIcon
# Initialize Qt resources from file resources.py
import resources_rc
# Import the code for the dialog
from locationsaver_dialog import locationsaverDialog
import os.path

import datetime
import time

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from qgis.gui import QgsMessageBar

import qgis
from qgis.core import *

class locationsaver:
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'locationsaver_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Create the dialog (after translation) and keep reference
        self.dlg = locationsaverDialog()

        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&locationsaver')
        # TODO: We are going to let the user set this up in a future iteration
        self.toolbar = self.iface.addToolBar(u'locationsaver')
        self.toolbar.setObjectName(u'locationsaver')

    # noinspection PyMethodMayBeStatic
    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('locationsaver', message)


    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None):
        """Add a toolbar icon to the toolbar.

        :param icon_path: Path to the icon for this action. Can be a resource
            path (e.g. ':/plugins/foo/bar.png') or a normal file system path.
        :type icon_path: str

        :param text: Text that should be shown in menu items for this action.
        :type text: str

        :param callback: Function to be called when the action is triggered.
        :type callback: function

        :param enabled_flag: A flag indicating if the action should be enabled
            by default. Defaults to True.
        :type enabled_flag: bool

        :param add_to_menu: Flag indicating whether the action should also
            be added to the menu. Defaults to True.
        :type add_to_menu: bool

        :param add_to_toolbar: Flag indicating whether the action should also
            be added to the toolbar. Defaults to True.
        :type add_to_toolbar: bool

        :param status_tip: Optional text to show in a popup when mouse pointer
            hovers over the action.
        :type status_tip: str

        :param parent: Parent widget for the new action. Defaults None.
        :type parent: QWidget

        :param whats_this: Optional text to show in the status bar when the
            mouse pointer hovers over the action.

        :returns: The action that was created. Note that the action is also
            added to self.actions list.
        :rtype: QAction
        """

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            self.toolbar.addAction(action)

        if add_to_menu:
            self.iface.addPluginToMenu(
                self.menu,
                action)

        self.actions.append(action)

        return action

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        icon_path = ':/plugins/locationsaver/icon.png'
        self.add_action(
            icon_path,
            text=self.tr(u'locationsaver'),
            callback=self.run,
            parent=self.iface.mainWindow())


    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginMenu(
                self.tr(u'&locationsaver'),
                action)
            self.iface.removeToolBarIcon(action)


    def run(self):


 				mapCanvas = self.iface.mapCanvas()

 				mapRenderer = mapCanvas.mapRenderer()

 				srs = mapRenderer.destinationCrs()

				trovato = 0
				for iLayer in range(mapCanvas.layerCount()):
				   layer = mapCanvas.layer(iLayer)
				   if layer.name() == "Locations":
				      trovato = 1
				      memLay_Line = layer
				      memprovider_Line = memLay_Line.dataProvider()


				if (trovato == 0):

				   geomType = ("LineString" + '?crs=%s') %(srs.authid())
				   DronePlan = "Locations"             
				   memLay_Line = QgsVectorLayer(geomType, DronePlan, 'memory') 
				   memprovider_Line = memLay_Line.dataProvider()
				   memLay_Line.updateExtents()
				   memLay_Line.commitChanges()
				   QgsMapLayerRegistry.instance().addMapLayer(memLay_Line) 
				   res = memprovider_Line.addAttributes( [ QgsField("ID",  QVariant.String), QgsField("Note",  QVariant.String) ] )

				   styledir = QFileInfo(QgsApplication.qgisUserDbFilePath()).path() + "python/plugins/locationsaver/_QML_Styles"
				   memLay_Line.loadNamedStyle(styledir + '/locationsaver.qml')


				adesso = str(datetime.datetime.now())
				adesso = adesso.replace(" ","_")
				adesso = adesso.replace(":","_")
				adesso = adesso.replace(".","_") 


		
				mapRect = mapCanvas.extent()

				x1 = mapRect.xMinimum()
				y1 = mapRect.yMinimum()

				x3 = mapRect.xMaximum()
				y3 = mapRect.yMaximum()

				x2 = x1
				y2 = y3

				x4 = x3
				y4 = y1  

				gLine = QgsGeometry.fromPolyline( [ QgsPoint(x1,y1), QgsPoint(x2,y2) , QgsPoint(x3,y3), QgsPoint(x4,y4), QgsPoint(x1,y1) ] )

				fet = QgsFeature()
				fet.setGeometry( gLine )

				fet.initAttributes(1)

				IDLocation = ("Location_%s") % (adesso)

				Note = IDLocation
				values = [(IDLocation),(Note)]

				fet.setAttributes(values)

				memprovider_Line.addFeatures([fet]) 

				memLay_Line.updateFields()
				memLay_Line.updateExtents()
        
				self.iface.messageBar().pushMessage("Location saved: ",
                                                IDLocation,
                                                QgsMessageBar.INFO, 3)        
