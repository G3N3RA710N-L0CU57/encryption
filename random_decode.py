""" Decodes the following:  

    bin2hex(strrev(base64_encode($secret)))

    that is encoded by a php script.

    Encode:
    string -> base64_encode() -> string base 64 rep -> strrev -> reversed base64 string -> 
    bin2hex() -> converted ascii chars to hexidecimal

    Decode:
    secret -> to ascii -> reverse -> base64_decode

"""
import base64
from codecs import ascii_decode


encoded_secret = '3d3d516343746d4d6d6c315669563362'

def hex_to_ascii(hex_string):

    """ Returns an ascii string from a string hexadecimal.
        Hexidecimal must be **2 string.
    """

    hex_length = len(hex_string)

    ascii_str = str()

    for i in range(0, hex_length):
        if i % 2:
            two_byte = hex_string[i-1] + hex_string[i]
            two_byte_int = int(two_byte, base=16)
            ascii_char = chr(two_byte_int)
            ascii_str += ascii_char           

    return ascii_str

# Convert hexidecimal string to ascii char string.
string64 = hex_to_ascii(encoded_secret)

# Reverse the string.
rev_string64 = string64[::-1]

# Encode the ascii string as bytes.
base64_bytes = rev_string64.encode('ascii')

# Decode the base64 bytes
secret_bytes = base64.b64decode(base64_bytes)

# Decode into ascii.
message = secret_bytes.decode('ascii')

print(message)