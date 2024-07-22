import random

def rdm_rsc():
    semiput = []
    l_rsc = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6]
    for i in range(19): # number of numbers in l_rsc
        rdm_int = random.choice(l_rsc) # random number from list
        l_rsc.remove(rdm_int) # remove from l_rsc
        semiput.append(rdm_int) # add to semiput
    
    # Define a mapping from numbers to letters
    num_to_letter = {
        1: 'wh',
        2: 'w',
        3: 'sh',
        4: 'ore',
        5: 'br',
        6: 'd'
    }
    output = [num_to_letter[num] for num in semiput]
    return output

# Generate the random pattern
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

# Define the indentation for each line to center the resources
indentation = ["       ", "   ", "", "   ", "       "]

# Print each chunk with the appropriate indentation
for i, chunk in enumerate(chunks):
    print(indentation[i] + str(chunk))