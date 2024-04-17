"""
File Extensions

In a file called extensions.py, implement a program that prompts the user for
the name of a file and then outputs that file's media type if the file's name
ends, case-insensitively, in any of these suffixes:

.gif
.jpg
.jpeg
.png
.pdf
.txt
.zip

If the file's name ends with some other suffix or has no suffix at all, output
application/octet-stream instead, which is a common default.
"""

ext_MIME = {
    'gif': 'image/gif',
    'jpg': 'image/jpeg',
    'jpeg': 'image/jpeg',
    'png': 'image/png',
    'pdf': 'application/pdf',
    'txt': 'text/plain',
    'zip': 'application/zip'
}

if __name__ == "__main__":
    get_input = input().strip().lower()

    split_str = get_input.split('.')

    if split_str[-1] in ext_MIME:
        print(ext_MIME[split_str[-1]])

    else:
        print("application/octet-stream")