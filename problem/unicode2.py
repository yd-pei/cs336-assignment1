"""
Byte sequence that does not decode to any Unicode character(s).
"""

for i in range(256):
    for j in range(256):
        try:
            bytes([i, j]).decode('utf-8')
        except UnicodeDecodeError:
            print(f"Failed to decode: {[i, j]}")
            break
    break
