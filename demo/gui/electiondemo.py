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

import os

import PyQt5.QtWidgets as qw
import PyQt5.QtGui as qg
import PyQt5.QtCore as qc

from demo.io.csvio import read_file, write_file

from demo.gui.Ui_electiondemo import Ui_ElectionDemo
from demo.gui.tablemodels import ConstituancyTableModel, VoteShareTableModel

class ElectionDemo(qw.QMainWindow, Ui_ElectionDemo):
    """
    The main window for an election results demonstration program.
    In this program the names, and ordering of the parties is hard coded
    thus avoiding the problem of handeling meta-data. This allows the
    raw data to be a dictionary mapping constituancy names to a list
    of the votes.
    """

    def __init__(self, parent=None):
        """
        the object initalization function

            Args:
                parent (QObject): the parent QObject for this window

            Returns:
                None
        """
        super().__init__(parent)
        self.setupUi(self)

        ## handle for the results
        self._data = None

        ## handle for the constituancy table data model
        self._constituency_model = None

        ## handle for the national vote share data model
        self._vote_share_model = None
        
    @qc.pyqtSlot()
    def data_changed(self):
        print(">>>> something has changed in the data redisplay all")
        self._partyTableView.viewport().update()

    @qc.pyqtSlot()
    def load_data(self):
        """
        callback for reading in the raw data
        """
        file_name, _ = qw.QFileDialog.getOpenFileName(
            self,
            "Read Results File",
            os.path.expanduser('~'),
            "CSV (*.csv)")

        if file_name is not None and file_name != '':
            self._data = read_file(file_name)
            self.fill_tables()

    @qc.pyqtSlot()
    def save_data(self):
        """
        callback for saving the data
        """
        file_name, _ = qw.QFileDialog.getSaveFileName(
            self,
            "Save Results File",
            os.path.expanduser('~'),
            "CSV (*.csv)")

        if file_name is not None and file_name != '':
            write_file(self._data, file_name)

    def fill_tables(self):
        """
        create the models and fill the tables
        """

        # constituancy table
        self._constituency_model = ConstituancyTableModel(self._data)
        self._constituencyTableView.setModel(self._constituency_model)
        self._constituencyTableView.setStyleSheet("QHeaderView::section { background-color:red }")
        self._constituencyTableView.verticalHeader().hide()
        self._constituency_model.dataChanged.connect(self.data_changed)

        # party share of the vote
        self._vote_share_model = VoteShareTableModel(self._data)
        self._partyTableView.setModel(self._vote_share_model)
        self._partyTableView.setStyleSheet("QHeaderView::section { background-color:red }")
