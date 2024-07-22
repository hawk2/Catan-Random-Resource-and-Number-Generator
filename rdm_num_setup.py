import random

def rdm_rsc():
    n = int(input("Desert:"))
    semiput = []
    l_rsc = [2, 3, 3, 4, 4, 5, 5, 6, 6, 8, 8, 9, 9, 10, 10, 11, 11, 12]
    for i in range(18):  # number of numbers in l_rsc
        rdm_int = random.choice(l_rsc)  # random number from list
        l_rsc.remove(rdm_int)  # remove from l_rsc
        semiput.append(rdm_int)  # add to semiput
    semiput.insert(n, "r")
    return semiput

output = rdm_rsc()

def chunk_it(output):
    chunk_sizes = [3, 4, 5, 4, 3]
    chunks = []
    start = 0

    for chunk_size in chunk_sizes:
        chunk = output[start:start + chunk_size]
        chunks.append(chunk)
        start += chunk_size
        if start >= len(output):
            break

    return chunks

# Split the output into chunks
chunks = chunk_it(output)

# Calculate the maximum width of the chunk representation
max_width = max(len(str(chunk)) for chunk in chunks)

# Print each chunk with the appropriate indentation
for chunk in chunks:
    chunk_str = str(chunk)
    # Calculate the needed spaces to center the chunk
    spaces = (max_width - len(chunk_str)) // 2
    print(' ' * spaces + chunk_str)