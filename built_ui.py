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

@copyright 2020
@author: j.h.pickering@leeds.ac.uk and j.leng@leeds.ac.uk
"""

import os

# a list of the modules that the package requires
modules = ["electiondemo"]

# relative path to the Qt .ui file
UI_PATH = "./resources/designer_ui/"

# relative path to the python source files
PY_PATH = "./demo/gui/Ui_"

def build(module_name):
    """
    run pyuic5 on a single module

        Args:
            module_name (string) the module name with no decoration or postfix
    """
    ui_file = f"{UI_PATH}{module_name}.ui"
    py_file = f"{PY_PATH}{module_name}.py"

    command = "pyuic5 {} -o {}"

    # in the case of failure CPython will print its own error message
    if os.system(command.format(ui_file, py_file)) == 0:
        print(f"made Ui_{module_name}.py")

if __name__ == "__main__":
    for module in modules:
        build(module)
