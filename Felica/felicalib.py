from ctypes import *

flib = cdll.felicalib   # ライブラリを読む

flib.pasori_open.restype = c_void_p
pasori  = flib.pasori_open()    # PaSoRiと接続

flib.pasori_init(pasori)

flib.felica_polling.restype = c_void_p
felica = flib.felica_polling(pasori, 0xFFFF, 0 , 0) # FeliCaを読む

idm = c_uint64()
flib.felica_getidm(felica, byref(idm))  # IDm取得

print("%016X" % idm.value)
flib.pasori_close(pasori)   # PaSoRiを切断