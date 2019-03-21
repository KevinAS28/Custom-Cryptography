#CUSTOM ECRYPTION
#by kevin A.S

#ada 2 enkripsi
#XYZcrypt
#CRYpstal

#rules
#string akan jadi utf-8
#data dan password % 4 = 0
#bytes
#mode KDC (kevin design crypt)
#mode ...


#tambahkan byte pembingung, (ditentukan dari password)

import string
import os
import re
import sys
import copy

args = sys.argv
#for debug mode(nanti buat file baru dan hapus tiga pagar (###))

huruf = {}
aslow = list(string.ascii_lowercase)
for i in aslow:
    huruf[r"%s" %(i)] = aslow.index(i)

def decor(*pesan, dec="#"):
    print(dec * 10)
    for i in pesan:
        print(i)
    print(dec * 10)

if True:#class KevinCipher:
    #biar kayak aes, kalo object sudah dibuat, selanjutnya hanya perlu aes.encrypt
        
    class XYZ:
        @staticmethod
        def KDC():
            return [0, 0, 1, 1, 1, 0, 1]
        
        class new:
            def __init__(self, M, P):
                try:
                    try:
                      __P = P.encode("utf-8")
                    except:
                        __P = P
                    del P
                    PP = []
                    for i in __P:
                        PP.append(i)
                    __P = copy.copy(PP)
                    del PP
                    
                except:
                    pass
                if ((len(__P) % 8)  != 0):
                    while True:
                        if (len(__P) % 8 != 0):
                            break
                        __P += b"\0"
                
                self.__P = bytes(__P)
                self.M = M
                
            
            def encrypt(self, D):
                if type(D) != bytes:
                    D = D.encode("utf-8")
                if len(D) % 8 != 0:
                    raise ValueError("the input lenght must be 0 after % 8")
                
                jabar = []
                for i in D:
                    jabar.append(i)
                ###print(D)
                
                #reverse
                jabar = jabar[::-1]            
                __to_enc = []
                ###decor(len(D))
                #reverse block 2(belakang)
                #[0] 
                for i in range(int(len(D)/2)): #because it will be float
                    
                    __to_enc.append(jabar[-2])
                    __to_enc.append(jabar[-1])
                    del(jabar[-2])
                    del(jabar[-1])
                
                __to_enc = __to_enc[::-1]    
                for i in range(int(len(D)/2)):#reverse block 2(depan)
                    try:
                     __to_enc.append(jabar[1])
                     __to_enc.append(jabar[0])
                     del(jabar[1])
                     del(jabar[0])
                    except:
                        pass
                
                __to_enc0 = []
                slaing = True

                #enc0                
                for i in __to_enc:
                    if slaing:
                        if (int(i + (len(self.__P)/2)) > 255):
                            __to_enc0.append(int(i - (len(self.__P)/2)))
                        else:
                            __to_enc0.append(int(i + (len(self.__P)/2)))
                    if not slaing:
                        if (int(i - (len(self.__P)*2)) < 0):
                            __to_enc0.append(int(i + (len(self.__P)*2)))
                        else:
                            __to_enc0.append(int(i - (len(self.__P)*2)))
                    if slaing:
                        slaing = False
                    if not slaing:
                        slaing = True
                    
                    
                del __to_enc
                Pass_list = []
                for i in self.__P:
                    Pass_list.append(i)
                kebrp = 0
                slaing = True
                for i in range(len(__to_enc0)):
                    if kebrp == len(Pass_list):
                        kebrp = 0
                    if slaing:
                        if ((__to_enc0[i] - Pass_list[kebrp]) < 0):
                            __to_enc0[i] = __to_enc0[i] + Pass_list[kebrp]
                        else:
                            __to_enc0[i] = __to_enc0[i] - Pass_list[kebrp]
                    if not slaing:
                        if ((__to_enc0[i] + Pass_list[kebrp]) > 255):
                            __to_enc0[i] = __to_enc0[i] - Pass_list[kebrp]
                        else:
                            __to_enc0[i] = __to_enc0[i] + Pass_list[kebrp]
                    kebrp += 1
                    if slaing:
                        slaing = False
                    if not slaing:
                        slaing = True
                """                                       
                slaing = True
                kbrp = -1
                for i in range(len(__to_enc0)):
                    if (kebrp == len(Pass_list)):
                        kbrp = -1
                    if slaing:
                        __to_enc0[i] = __to_enc0[i] - Pass_list[kebrp]
                    if not slaing:
                        __to_enc0[i] = __to_enc0[i] - Pass_list[kebrp]
                    if slaing:
                        slaing = False
                    if not slaing:
                        slaing = True
                    kebrp -= 1
                    #__to_enc = list(map(enc1, __to_enc0))"""
                """
                kebrp0 = -1
                kebrp1 = 0
                for i in __to_enc0:
                    if kebrp0 == -(len(Pass_list)):
                        kebrp = -1
                    if (i + Pass_list[-1]) > 255: 
                        __to_enc0[kebrp1] -= Pass_list[kebrp0]
                    if (i - Pass_list[-1]) < 0: 
                        __to_enc0[kebrp1] -= Pass_list[kebrp0]                    
                    kebrp0 -= 1
                    kebrp1 += 1"""
                return bytes(__to_enc0)#utf-8
        
    
        
        



            
            
        


            
            
            
            
            
                
                
            
xyz = XYZ().new()
print(xyz.encrypt("kevinags"))
