import hashlib

key = 0

while key != 10**5:
    keys = str(key)
    keys = keys + 'fHzxcGBiIWIcVceO2awq'
    keys = hashlib.md5(keys.encode())
    keys = keys.hexdigest()
    if keys == '1f04ba160affffbced5f6f631f5f60db':
        print(key)
    key +=1 
