# Run Length Encoding
### Category: Lossless


## How it works
When encoding text data it looks for repeat characters and replace the row of them with a number for the amount and then the character which the decoder uses to know the amount of the character to reconstruct the old message


## Personal Assessment
This is a great first compression algorithm when learning how to create your own systems to compress data but this system hardly does anything about files size but at least with my version it should never become larger than the original file size.


## EXAMPLE
```
Original: AAABBBBCC
Compressed: 3A4B2C
```


## Flaws
- If the text doesn't include a lot of repeat characters the file could increase in size
    ```
    Example

    Original: ABC
    "Compressed": 1A1B1C

    I'm sure you can see the issue here
    ```

## Solutions to Flaws
- In order to avoid issues where the file size increases when there is only 1 unique character at a time then the 1 will not be added
    ```
    Example

    Original: AAABCCC
    Compressed: 3AB3C

    Singular characters can just be read as singular characters without needing a count
    ```