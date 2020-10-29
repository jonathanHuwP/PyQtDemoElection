## -*- coding: utf-8 -*-
"""
Created on Tue 27 Oct 2020

Licensed under the Apache License, Version 2.0 (the "License"); you may not use
this file except in compliance with the License. You may obtain a copy of the
License at
http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed
under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.

This work was funded by Joanna Leng's EPSRC funded RSE Fellowship (EP/R025819/1)

@copyright 2020
@author: j.h.pickering@leeds.ac.uk and j.leng@leeds.ac.uk
"""
# set up linting conditions
# pylint: disable = too-many-public-methods
# pylint: disable = c-extension-no-member

import PyQt5.QtGui as qg
import PyQt5.QtCore as qc

class ConstituancyTableModel(qc.QAbstractTableModel):
    """
    the data model for the constituancy results table
    
    Note: the function names and variable lists are fixed
    by the need to override the C++ originals and cannot be
    changed
    """

    def __init__(self, data):
        """
        store the data
        
            Args:
                data (dict) the data store to be displayed/edited
        """
        super().__init__()
        self._data = data

    def data(self, index, role):
        """
        getter for data and display features

            Args:
                index (QModelIndex) the location of the data row(), column()
                role (int) the Qt flag for the purpose of the get, raw data, background etc

            Returns:
                required (QVariant) data for the cell
        """
        # convert dictionary contents to a list
        rows = list(self._data.items())

        # get the row as a tuple (key, [data])
        row = rows[index.row()]

        # convert row to a list
        row = [row[0]] + row[1]

        if role == qc.Qt.DisplayRole:
            return qc.QVariant(row[index.column()])

        if role == qc.Qt.BackgroundRole:
            if index.row() % 2 == 0:
                return qg.QColor('yellow')

            return qg.QColor('purple')

        return qc.QVariant()

    def headerData(self, section, orientation, role):
        """
        getter for the table headers
        """
        headers = ["Constituancy", "Lab", "Con", "LD"]

        if role == qc.Qt.DisplayRole and orientation == qc.Qt.Horizontal:
            return qc.QVariant(headers[section])

        return qc.QVariant()


    def rowCount(self, index):
        """ the number of rows in table"""
        return len(self._data)

    def columnCount(self, index):
        """the number of columns in the table"""
        return 4
        
    def flags(self, index):
        """
        return that the numeric columns are editable
        """
        if index.column() == 0:
            return qc.Qt.ItemIsEnabled|qc.Qt.ItemIsSelectable
        else:
            return qc.Qt.ItemIsEnabled|qc.Qt.ItemIsSelectable|qc.Qt.ItemIsEditable
            
    def setData(self, index, value, role):
        """
        allow the new value to replace the old in the data source, this method will
        not work if the order of the data is different between the dictionary and 
        the table, Python 3.6 onward preserve insetion order by default
        """
        if role == qc.Qt.EditRole and value.isnumeric():
            # convert keys to a list so that they they can be indexed
            keys = [x for x in self._data.keys()]
            key = keys[index.row()]
            self._data[key][index.column()-1] = value
            
            self.dataChanged.emit(index, index)
            return True
            
        return False

class VoteShareTableModel(qc.QAbstractTableModel):
    """
    the data model for the party share of the votes
    
    Note: the function names and variable lists are fixed
    by the need to override the C++ originals and cannot be
    changed
    """

    def __init__(self, data):
        """
        store the data
        
            Args:
                data (dict) the data store to be displayed/edited
        """
        super().__init__()
        self._data = data

    def data(self, index, role):
        """
        getter for data and display features

            Args:
                index (QModelIndex) the location of the data row(), column()
                role (int) the Qt flag for the purpose of the get, raw data, background etc

            Returns:
                required (QVariant) data for the cell
        """
        if role == qc.Qt.DisplayRole:
            percentages = self._data.party_percentages()
            item = "{:.2f}".format(percentages[index.row()])
            return qc.QVariant(item)

        return qc.QVariant()

    def headerData(self, section, orientation, role):
        """
        getter for the table headers
        """
        headers = ["Lab", "Con", "LD"]

        if role == qc.Qt.DisplayRole:
            if orientation == qc.Qt.Vertical:
                return qc.QVariant(headers[section])
            elif orientation == qc.Qt.Horizontal:
                return qc.QVariant("Vote (%)")

        return qc.QVariant()

    def rowCount(self, index):
        """ the number of rows in table"""
        return 3

    def columnCount(self, index):
        """the number of columns in the table"""
        return 1
