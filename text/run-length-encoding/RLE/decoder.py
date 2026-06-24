number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

CHAR_ESCAPE_CODE = "\x1b"

def decode_file(file_path: str) -> str:
    with open(file_path, "r") as f:
        text = f.read()
        f.close()
    
    return _decode(text)


def decode_string(input_string: str) -> str:
    return _decode(input_string)


def _decode(input: str) -> str:
    if not input:
        return ""

    lines = input.splitlines()

    decoded_lines_list = []

    for line in lines:
        decoded_line = ""
        count = 1
        write_number = False

        for char in line:
            if (char in number) and not write_number:
                if count > 1:
                    count = (count * 10) + int(char)
                else:
                    count = int(char)
            elif char == CHAR_ESCAPE_CODE:
                write_number = True
            else:
                write_number = False
                if count > 1:
                    decoded_line += (char * count)
                    count = 1
                else:
                    decoded_line += char
        
        decoded_lines_list.append(decoded_line)


    return "\n".join(decoded_lines_list)