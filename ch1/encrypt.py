from secrets import  token_bytes
from typing import Tuple
import base64

def random_key(length:int) -> int:
    
    tb: bytes =token_bytes(length)
    tbase64 : bytes =base64.b64encode(tb)
    
    return int.from_bytes(tbase64,"big")

def encrypt(original:str) -> Tuple[int,int]:
    second: str =original[::-1]
    sec_bytes: bytes= second.encode("utf-8")
    sec_base64: bytes = base64.b64encode(sec_bytes)
    dummy: int=random_key(len(sec_base64))
    sec_key: int=int.from_bytes(sec_base64,"big")
    encrypted : int = dummy^sec_key
    
    return dummy,encrypted

def decrypt(key1:int,key2:int) -> str:
    decrypted: int=key1^key2
    temp: bytes=decrypted.to_bytes((decrypted.bit_length()+7) //8,"big")
    temp2: bytes = base64.b64decode(temp)
    temp3: str= temp2.decode("utf8")
    return temp3[::-1]    

if __name__ =="__main__":
    k1,k2 = encrypt(input())
    result:str=decrypt(k1,k2)
    print(result)