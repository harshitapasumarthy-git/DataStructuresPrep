from collections import Counter


def countConnections(matrix):
    m = len(matrix)
    n = len(matrix[0])
    count = 0

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 1:
                # Check top-left diagonal
                if i - 1 >= 0 and j - 1 >= 0 and matrix[i - 1][j - 1] == 1:
                    count += 1
                # Check top
                if i - 1 >= 0 and matrix[i - 1][j] == 1:
                    count += 1
                # Check top-right diagonal
                if i - 1 >= 0 and j + 1 < n and matrix[i - 1][j + 1] == 1:
                    count += 1
                # Check right
                if j + 1 < n and matrix[i][j + 1] == 1:
                    count += 1
    return count
def compress_and_sort(chars):
    write = 0
    anchor = 0
    compressed = []

    # Compress the input characters
    for read in range(len(chars)):
        if read + 1 == len(chars) or chars[read + 1] != chars[read]:
            compressed.append(chars[read])
            if read - anchor > 0:
                n = read - anchor + 1
                compressed.extend(list(str(n)))
            anchor = read + 1

    # Split compressed list into tuples of (character, count)
    i = 0
    result = []
    while i < len(compressed):
        char = compressed[i]
        count = ''
        i += 1
        while i < len(compressed) and compressed[i].isdigit():
            count += compressed[i]
            i += 1
        if count == '':
            count = '1'
        result.append((char, int(count)))

    # Sort the result based on the character
    # result.sort(key=lambda x: x[0])

    # Rebuild the sorted compressed list
    sorted_compressed = []
    for char, count in result:
        sorted_compressed.append(char)
        if count > 1:
            sorted_compressed.extend(list(str(count)))

    return sorted_compressed


def sort_alphabetically_linear(input_str):
    buckets = [[] for _ in range(26)]

    i = 0
    while i < len(input_str):
        char = input_str[i]
        if char.isalpha():
            index = ord(char.lower()) - ord('a')
            num = ''
            i += 1
            while i < len(input_str) and input_str[i].isdigit():
                num += input_str[i]
                i += 1
            buckets[index].append(char + num)
        else:
            i += 1

    sorted_str = ''.join([''.join(bucket) for bucket in buckets])
    return sorted_str


def betterCompression(compressed: str) -> str:
    char_count = {}
    i = 0
    n = len(compressed)

    while i < n:
        char = compressed[i]
        i += 1
        x = 0
        while i < n and compressed[i].isdigit():
            x = x * 10 + int(compressed[i])
            i += 1
        if char in char_count:
            char_count[char] += x
        else:
            char_count[char] = x

    result = ""
    for char in sorted(char_count):
        result += f"{char}{char_count[char]}"

    return result


if __name__ == "__main__":

    # Example usage
    input_str = "a12b56c1"
    sorted_str = betterCompression(input_str)
    print(sorted_str)  # Output will be "a3b2c1"
