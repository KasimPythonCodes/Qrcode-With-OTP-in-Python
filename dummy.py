import random

import qrcode

x=random.randint(100000 , 999999)
im=qrcode.make("OTP IS"+str(x))

im.show()