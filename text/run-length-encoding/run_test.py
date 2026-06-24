import RLE

import time

def main() -> None:
    file_path = "test.txt"

    with open(file_path, "r") as f:
        original_text = f.read()
        f.close()
    
    encode_start_time = time.perf_counter()
    compressed = RLE.encode_string(original_text)
    encode_end_time = time.perf_counter()

    encode_time = (encode_end_time - encode_start_time) * 1000

    with open("compressed.txt", "w") as f:
        f.write(compressed)
        f.close()

    with open("results.txt", "w") as f:
        f.write(f"Original Size {len(original_text.encode())}\n")
        f.write(("-" * 20) + "\n")
        f.write(f"Compressed Size {len(compressed.encode())}\n")
        f.write(f"Encoding Time {encode_time:.6f} ms\n")
        f.write(("-" * 20) + "\n")
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