import RLE

import time

def main() -> None:
    file_path = "test.txt"

    with open(file_path, "r") as f:
        original_text = f.read()
        f.close()
    
    original_lines = original_text.splitlines()
    clean_line_list = []

    for line in original_lines:
        line = line.rstrip()
        clean_line_list.append(line)

    clean_text = "\n".join(clean_line_list)
    
    encode_start_time = time.perf_counter()
    compressed = RLE.encode_string(clean_text)
    encode_end_time = time.perf_counter()

    encode_time = (encode_end_time - encode_start_time) * 1000

    with open("compressed.txt", "w") as f:
        f.write(compressed)
        f.close()

    decode_start_time = time.perf_counter()
    decoded = RLE.decode_string(compressed)
    decode_end_time = time.perf_counter()

    decode_time = (decode_end_time - decode_start_time) * 1000

    with open("decoded.txt", "w") as f:
        f.write(decoded)
        f.close()

    with open("results.txt", "w") as f:
        f.write(f"Original Size {len(original_text.encode())}\n")
        f.write(f"Original Size (Cleaned) {len(clean_text.encode())}\n")
        f.write(("-" * 20) + "\n")
        f.write(f"Compressed Size {len(compressed.encode())}\n")
        f.write(f"Encoding Time {encode_time:.6f} ms\n")
        f.write(("-" * 20) + "\n")
        f.write(f"Decoded Size {len(decoded.encode())}\n")
        f.write(f"Decoding Time {decode_time:.6f} ms\n")
        f.close()

    print("Test Complete!")
    print("-" * 20)
    print("Original Text:", original_text)
    print("Size", len(original_text.encode()))
    print("-" * 20)
    print("Compressed Text:", compressed)
    print("Size", len(compressed.encode()))
    print("Encoding Time", f"{encode_time:.6f} ms")
    print("-" * 20)

if __name__ == "__main__":
    main()