# Log Parsing

This project involves parsing log files to extract useful information. The goal is to read a log file line by line and compute metrics.

## Requirements

- Python 3.x
- Basic understanding of file handling in Python

## Usage

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/alx-interview.git
    ```

2. Navigate to the project directory:
    ```sh
    cd alx-interview/0x03-log_parsing
    ```

3. Run the log parsing script:
    ```sh
    python3 log_parser.py
    ```

## Example

Given a log file `log.txt`:
```
127.0.0.1 - [2023-10-01 10:00:00] "GET /index.html HTTP/1.1" 200 1024
127.0.0.1 - [2023-10-01 10:01:00] "POST /submit HTTP/1.1" 404 512
```

The script will output:
```
Total file size: 1536
Status codes:
200: 1
404: 1
```

## Author

- Joe404
- GitHub: [yourusername](https://github.com/yourusername)
