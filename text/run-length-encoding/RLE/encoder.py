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

    lines = input.splitlines()

    compressed_data_list = []

    for line in lines:
        line = line.rstrip() # remove unneeded trailing spaces

        # Check if line is empty before doing anything with it
        if not line:
            compressed_data_list.append("")
            continue

        compressed_data = ""
        current_char = line[0]
        count = 1

        for char in line[1:]:
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
        
        compressed_data_list.append(compressed_data)
    
    return "\n".join(compressed_data_list)