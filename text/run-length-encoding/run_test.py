import RLE

def main() -> None:
    file_path = "test.txt"

    with open(file_path, "r") as f:
        original_text = f.read()
        f.close()
    
    compressed = RLE.encode_string(original_text)

    print("Test Complete!")
    print("-" * 20)
    print("Original Text:", original_text)
    print("Size", original_text.__sizeof__())
    print("-" * 20)
    print("Compressed Text:", compressed)
    print("Size", compressed.__sizeof__())
    print("-" * 20)

if __name__ == "__main__":
    main()