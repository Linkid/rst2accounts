ReST to accounts
================

.. image:: https://travis-ci.org/Linkid/rst2accounts.svg?branch=master
    :target: https://travis-ci.org/Linkid/rst2accounts
    :alt: Build Status


Calculate totals per operations in your accounts using a ReST table.


Example
-------

Your accounts look like that::

    Month
    -----

    +======+===============+========+========+=============+
    | Date |   Operation   | Debit  | Credit | Total month |
    +======+===============+========+========+=============+
    |  01  | A             |   1    |   /    |             |
    |  02  | B             |  11    |   /    |             |
    |  03  | C             | 111.1  |   /    |             |
    |  04  | D             |   /    | 1111.11|             |
    |  05  | E             |1111.01 |   /    |             |
    +------+---------------+--------+--------+-------------+
    |   /  | Total month   | 000.00 |  000.00|    000.00   |
    +------+---------------+--------+--------+-------------+


and you would like to complete the last column and the last line. So, put it in
a file and do::

    >>> rst2accounts my_accounts.rst

    Month
    -----

    +======+===============+========+========+=============+
    | Date |   Operation   | Debit  | Credit | Total month |
    +======+===============+========+========+=============+
    |  01  | A             |   1    |   /    |     -1.0    |
    |  02  | B             |  11    |   /    |    -12.0    |
    |  03  | C             | 111.1  |   /    |   -123.1    |
    |  04  | D             |   /    | 1111.11|    988.01   |
    |  05  | E             |1111.01 |   /    |   -123.0    |
    +------+---------------+--------+--------+-------------+
    |   /  | Total month   |1234.11 | 1111.11|   -123.0    |
    +------+---------------+--------+--------+-------------+

Easy, right?
