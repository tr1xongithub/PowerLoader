import sys
def read_bytes(files):
    with open(files,"rb") as file:
        lines = file.read()
        data = bytearray(lines)
        return data
def write_bytes():
    bytes = read_bytes(sys.argv[1])
    #data = bytearray(data)
    with open("decode.raw","wb") as file:
        file.write(bytes)
    file.close()
write_bytes()