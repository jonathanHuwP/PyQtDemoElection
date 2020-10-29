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
import csv

def read_file(file_name):
    """
    read the csv file of election results

        Args:
            file_name (string) the file_name, including relative path

        Returns:
            dictionary of rows, first entry => rest of row

        Throws:
            IOError if file cannot be opened
    """
    results = dict()

    with open(file_name, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            results[row[0]] = row[1:]

    return results

def write_file(results, file_name):
    """
    write  the csv file of election results

        Args:
            results (dict) the dictionary of results
            file_name (string) the file_name, including relative path

        Throws:
            IOError if file cannot be opened
    """
    with open(file_name, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)

        for item in results.items():
            row = [item[0]] + item[1]
            csv_writer.writerow(row)

if __name__ == "__main__":
    tmp_results = read_file(".\\resources\\sample_data.csv")

    for tmp in tmp_results.items():
        print("{} => {}".format(tmp[0], tmp[1]))

    test = {}

    # comment on use of csv to fix test etc
    test["North\" Winging"] = [12, 17, 4]
    write_file(test, "test_output.csv")
