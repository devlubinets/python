# unicode.org/charts
# UTF-8 best and recommended for WEB dynamic 1-4 bytes
print(ord('H'))
print(ord('e'))
print(ord('\n'))

encoded_bytes = "GET fb.com".encode('utf-8')
print(fr"{encoded_bytes}")
print(type(encoded_bytes))

# Print the bytes
print("Encoded Bytes:", encoded_bytes)

# To see the bytes as integers, you can iterate over the bytes and print each byte's integer value
print("Bytes as Integers:", [byte for byte in encoded_bytes])