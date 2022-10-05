"""
Created on Feb 12 2018

@author: MCC
"""


def enum_mask_to_list(enum_type, mask):
    enum_value_list = []
    for opt in enum_type:
        if opt & mask:
            enum_value_list.append(opt)
    return enum_value_list
