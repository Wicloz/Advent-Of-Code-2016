def count_decompressed(compressed):
    length = 0
    skip = 0
    for i in range(len(compressed)):
        if i < skip:
            continue
        if compressed[i] is '(':
            close = compressed.find(')', i)
            chars, repeats = [int(x) for x in compressed[i+1:close].split('x')]
            skip = close + chars + 1
            block = compressed[close+1:skip]
            length += repeats*count_decompressed(block)
        elif compressed[i] is not '\n':
            length += 1
    return length

input = open('input.txt', 'r')
compressed = input.read()
input.close()

length = count_decompressed(compressed)
print(length)
