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

class ElectionResults(dict):
    """
    a dictionary for the elections results with a function
    to calculate the party percentages of the total vote
    """

    def party_percentages(self):
        """
        calculate the party percentages of the vote

            Returns:
                percentages of vote as a list
        """
        total = 0
        votes = [0, 0, 0]
        for key in self.keys():
            for i in range(0,3):
                vote = int(self[key][i])
                votes[i] += vote
                total += vote

        percentages = [(x / total)*100.0 for x in votes]

        return percentages
