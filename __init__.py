# -*- coding: utf-8 -*-
"""
/***************************************************************************
 locationsaver
                                 A QGIS plugin
 locationsaver
                             -------------------
        begin                : 2014-11-26
        copyright            : (C) 2014 by geodrinx
        email                : geodrinx@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load locationsaver class from file locationsaver.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .locationsaver import locationsaver
    return locationsaver(iface)
