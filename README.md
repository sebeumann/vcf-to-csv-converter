# VCF to CSV Contact Converter

A Python script to convert VCF (vCard) contact files to CSV format. This tool is particularly useful for migrating contacts between different systems, such as from ProtonMail to Google Contacts.

## Features

- Converts VCF contact files to CSV format
- Handles multiple email addresses and phone numbers per contact
- Preserves contact details including:
  - Full Name
  - First Name
  - Last Name
  - Email Addresses
  - Phone Numbers
  - Organization
  - Addresses

## Prerequisites

- Python 3.x
- pip (Python package installer)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/YOUR_USERNAME/vcf-to-csv-converter.git
cd vcf-to-csv-converter
```

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the virtual environment:
   - On Linux/macOS:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```

4. Install required packages:
```bash
pip install pandas vobject
```

## Usage

1. Place your VCF file in the project directory
2. Update the input and output filenames in the script (optional)
3. Run the script:
```bash
python vcf_to_csv_converter.py
```

By default, the script looks for `protonContacts.vcf` and outputs to `googleContacts.csv`. You can modify these filenames in the script by changing the last lines:

```python
if __name__ == "__main__":
    vcf_to_csv('your_input.vcf', 'your_output.csv')
```

## Running with Different File Names

You can also run the script with different file names without modifying the code by importing the function:

```python
from vcf_to_csv_converter import vcf_to_csv

vcf_to_csv('input.vcf', 'output.csv')
```

## Error Handling

The script includes error handling for common issues:
- Missing input file
- Empty VCF file
- Malformed VCF data

Error messages will be logged to help identify any issues during conversion.

## Contributing

Feel free to fork this repository and submit pull requests for any improvements you make.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- vobject library for VCF parsing
- pandas for CSV handling

## Support

If you encounter any issues or have questions, please open an issue on the GitHub repository.
