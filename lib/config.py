import sys
import os
import hashlib
import decimal
D = decimal.Decimal

# Units
UNIT = 100000000    # The same across currencies.

# Versions
VERSION = 1
DB_VERSION = 4

# Bitcoin protocol
DUST_SIZE = 5430
MIN_FEE = 10000 # Counterparty transactions are all under 1KB in size.
DATA_VALUE = 0

# Counterparty protocol
TXTYPE_FORMAT = '>I'

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
