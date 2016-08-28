#!/usr/bin/env python
# -*- coding: utf-8 -*-


# ReST constants
COL_SEPARATOR = '|'
LINE_SEP_SEP = '+'
CELL_NULL = '/'


def center_float(cell, val, offset=0):
    cell_size = len(cell)
    s_val = str(val)
    val_size = len(s_val)
    # -2 due to the point and one digit
    point_index = -2 if '.' not in s_val else s_val.index('.')
    rval = s_val.rjust(cell_size // 2 + val_size - point_index + offset)

    return rval.ljust(cell_size)
    #return s_val.center(cell_size)


def main(cpt_table):
    # init vars
    is_header = True
    header = []
    total = 0
    total_debit = 0
    total_credit = 0

    # init the final table
    cpt_final = []

    # go ahead
    for line in cpt_table.splitlines():
        if COL_SEPARATOR in line:
            line_split = line.split(COL_SEPARATOR)
            if is_header:
                # header
                header = line_split
                a = [len(k) for k in header]
                is_header = False
            else:
                if CELL_NULL in line_split[1]:
                    # last line
                    line_split[3] = center_float(header[3], total_debit)
                    line_split[4] = center_float(header[4], total_credit)
                    line_split[5] = center_float(header[5], total, 1)
                else:
                    # operations
                    debit_ = line_split[3].strip()
                    credit_ = line_split[4].strip()
                    debit = 0 if CELL_NULL in debit_ else float(debit_)
                    credit = 0 if CELL_NULL in credit_ else float(credit_)
                    # totals
                    total_debit = round(total_debit + debit, 2)
                    total_credit = round(total_credit + credit, 2)
                    #total = round(total + credit - debit, 2)
                    total = round(total_credit - total_debit, 2)
                    line_split[5] = center_float(header[5], total, 1)
            cpt_final.append(COL_SEPARATOR.join(line_split))
        else:
            line_split = line.split(LINE_SEP_SEP)
            cpt_final.append(line)

    return cpt_final
