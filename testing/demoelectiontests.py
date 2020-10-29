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

import sys
import pathlib
import unittest

sys.path.insert(0, str(pathlib.Path.cwd()))
from demo.datastructs.electionresults import ElectionResults

## class for unit tests of the ImagePoints
class TestElectionResults(unittest.TestCase):
    """test haness for the results class"""

    def setUp(self):
        """make test case"""
        self._results = ElectionResults()
        self._results["Somewhere"] = [10, 5, 0]
        self._results["Somewhere Else"] = [0, 10, 5]
        self._results["Elsewhare"] = [5, 0, 10]

    def tearDown(self):
        """delete test case"""
        self._results = None

    def test_results(self):
        """
        test the percentage of the vote function
        """
        percentages = self._results.party_percentages()

        self.assertAlmostEqual(percentages[0],
                               33.3333,
                               msg="percentage of first party failed",
                               delta=0.0001)

        self.assertAlmostEqual(percentages[1],
                               33.3333,
                               msg="percentage of second party failed",
                               delta=0.0001)

        self.assertAlmostEqual(percentages[2],
                               33.3333,
                               msg="percentage of third party failed",
                               delta=0.0001)

if __name__ == "__main__":
    print("Unit Tests for DemoElection")
    unittest.main()
