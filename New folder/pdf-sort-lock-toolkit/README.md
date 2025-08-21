# PDF Sort and Lock Toolkit

This project provides functionalities to sort and lock PDF files. It includes two main features: sorting PDF files based on specified criteria and applying password protection to PDF files.

## Features

### Sorting
- The sorting feature allows users to sort a list of PDF files based on various criteria. The implementation is found in `src/sorting/sort_pdf.py`.

### Locking
- The locking feature enables users to secure PDF files with a password. This functionality is implemented in `src/locking/lock_pdf.py`.

## Installation

To set up the project, follow these steps:

1. Clone the repository:
   ```
   git clone <repository-url>
   cd pdf-sort-lock-toolkit
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

### Sorting PDFs
To sort PDF files, you can use the `sort_pdf` function from the `src/sorting/sort_pdf.py` file. This function takes a list of PDF file paths and sorts them based on the specified criteria.

### Locking PDFs
To lock a PDF file, use the `lock_pdf` function from the `src/locking/lock_pdf.py` file. This function requires the path to the PDF file and a password to apply the protection.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.