def getHashedURL(url, hash_string, k):
    # Write your code here

    output_hash_str = ''
    
    CHARACTER_MAPPING_DICT = {
        'a': 0,
        'b': 1,
        'c': 2,
        'd': 3,
        'e': 4,
        'f': 5,
        'g': 6,
        'h': 7,
        'i': 8,
        'j': 9,
        'k': 10,
        'l': 11,
        'm': 12,
        'n': 13,
        'o': 14,
        'p': 15,
        'q': 16,
        'r': 17,
        's': 18,
        't': 19,
        'u': 20,
        'v': 21,
        'w': 22,
        'x': 23,
        'y': 24,
        'z': 25,
        ':': 26, '/': 27, '.': 28
    }

    url_length = len(url)
    len_hash_str = len(hash_string)

    segments = url_length//k

    url_chunks = {}

    for i in range(0, url_length, k):
        hash_val = 0
        hash_str = url[i:i+k]

        for j in range(0, len(hash_str)):
            hash_val += CHARACTER_MAPPING_DICT[hash_str[j]]

        url_chunks[hash_str] = hash_val
        
        output_hash_str += hash_string[hash_val % len_hash_str]

        hash_val = 0
        hash_str = ''
    
    return output_hash_str
        

getHashedURL('https://xyz.com', 'pqrst', 4)
# https://xyz.com
# pqrst
# k = 4
