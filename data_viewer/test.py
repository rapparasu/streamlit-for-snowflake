"""
the purpose of this file is to test the modules
"""

import modules.utils as utils

filepath = utils.getFullPath("data/employees.csv")

print(f"filepath:{filepath}")