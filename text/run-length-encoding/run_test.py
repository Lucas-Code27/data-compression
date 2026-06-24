import RLE

import time

from pathlib import Path

current_file = Path(__file__).resolve()

TESTING_FOLDER = "testing"
CASES_FOLDER = "cases"
COMPRESSED_FOLDER = "compressed"
DECODED_FOLDER = "decoded"

def main() -> None:
    cases_folder = Path(f"{current_file.parent.parent}/{TESTING_FOLDER}/{CASES_FOLDER}")
    cases = [f for f in cases_folder.rglob("*.txt") if f.is_file()]

    with open(f"{current_file.parent.parent}/{TESTING_FOLDER}/results.txt", "w") as f:
        f.close()

    for file_path in cases:
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

        with open(f"{current_file.parent.parent}/{TESTING_FOLDER}/{COMPRESSED_FOLDER}/{file_path.name.removesuffix(".txt") + "-COMPRESSED.txt"}", "w") as f:
            f.write(compressed)
            f.close()

        decode_start_time = time.perf_counter()
        decoded = RLE.decode_string(compressed)
        decode_end_time = time.perf_counter()

        decode_time = (decode_end_time - decode_start_time) * 1000

        with open(f"{current_file.parent.parent}/{TESTING_FOLDER}/{DECODED_FOLDER}/{file_path.name.removesuffix(".txt") + "-DECODED.txt"}", "w") as f:
            f.write(decoded)
            f.close()

        with open(f"{current_file.parent.parent}/{TESTING_FOLDER}/results.txt", "a") as f:
            f.write(f"---{file_path.name}---\n")
            f.write(f"Original Size {len(original_text.encode())}\n")
            f.write(f"Original Size (Cleaned) {len(clean_text.encode())}\n")
            f.write(("-" * 20) + "\n")
            f.write(f"Compressed Size {len(compressed.encode())}\n")
            f.write(f"Encoding Time {encode_time:.6f} ms\n")
            f.write(("-" * 20) + "\n")
            f.write(f"Decoded Size {len(decoded.encode())}\n")
            f.write(f"Decoding Time {decode_time:.6f} ms\n\n\n")
            f.close()

        print(f"{file_path.name} Complete!")

    print("Test Complete!")


if __name__ == "__main__":
    main()