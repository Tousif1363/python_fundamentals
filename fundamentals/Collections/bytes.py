# immutable sequence of bytes
# prefixed with a lower case b

byte1 = b'Hello'
byte2 = b"World!"

print(byte1 + b" " + byte2)

norsk = 'Hello \345'
print(norsk)

byteRep = norsk.encode('utf-8')
print(byteRep)

norwegian = byteRep.decode('utf-8')
print(norwegian)
print(norwegian == norsk)

# Bytes are needed because Files, Network Resources and HTTP Responses are all byte streams
# and we need to decode them to strings to use them for our purpose
