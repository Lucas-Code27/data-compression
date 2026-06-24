def encode_file(file_path: str) -> str:
    with open(file_path, "r") as f:
        text = f.read()
        f.close()
    
    return _encode(text)


def encode_string(input_string: str) -> str:
    return _encode(input_string)


def _encode(input: str) -> str:
    if not input:
        return ""

    compressed_data = ""

    current_char = input[0]
    count = 1

    for char in input[1:]:
        if char == current_char:
            count += 1
        elif char == " ":
            if count == 1:
                compressed_data += current_char
                current_char = " "
            else:
                compressed_data += f"{count}{current_char}"
                current_char = " "

            count = 1
        else:
            if count == 1:
                compressed_data += current_char
                current_char = char
            else:
                compressed_data += f"{count}{current_char}"
                count = 1
                current_char = char
    
    if count == 1:
        compressed_data += current_char
    else:
        compressed_data += f"{count}{current_char}"
    
    return compressed_data