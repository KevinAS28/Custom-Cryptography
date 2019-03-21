from KEncrypt import XYZ
from cetak import cetak
import os

ojb = XYZ.new("modemode", b"\xff"*8)
cetak(ojb.encrypt(b"\x00"*8))

