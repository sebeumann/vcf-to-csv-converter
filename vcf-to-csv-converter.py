import pandas as pd
import vobject
from pathlib import Path
import logging
from typing import List, Dict, Any

def vcf_to_csv(input_file: str, output_file: str) -> None:
    """
    Convert a contact VCF (vCard) file to CSV format.
    
    Args:
        input_file (str): Path to input VCF file
        output_file (str): Path to output CSV file
    
    Raises:
        FileNotFoundError: If input file doesn't exist
        ValueError: If VCF file is empty or malformed
    """
    # Set up logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    
    # Validate input file
    input_path = Path(input_file)
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_file}")
    
    try:
        # Read VCF file
        logger.info(f"Reading VCF file: {input_file}")
        with open(input_file, 'r', encoding='utf-8') as f:
            vcf_content = f.read()
        
        # Extract records
        records: List[Dict[str, Any]] = []
        for vcard in vobject.readComponents(vcf_content):
            record_dict = {}
            
            # Extract common fields
            if hasattr(vcard, 'fn'): # Full Name
                record_dict['Full Name'] = vcard.fn.value
            
            if hasattr(vcard, 'n'): # Name components
                n = vcard.n.value
                record_dict['Last Name'] = n.family
                record_dict['First Name'] = n.given
                
            # Handle multiple email addresses
            emails = []
            if hasattr(vcard, 'email'):
                for email in vcard.email_list:
                    emails.append(email.value)
            record_dict['Email'] = ';'.join(emails) if emails else ''
            
            # Handle multiple phone numbers
            phones = []
            if hasattr(vcard, 'tel'):
                for tel in vcard.tel_list:
                    phones.append(tel.value)
            record_dict['Phone'] = ';'.join(phones) if phones else ''
            
            # Handle organization
            if hasattr(vcard, 'org'):
                record_dict['Organization'] = vcard.org.value[0] if vcard.org.value else ''
            
            # Handle address - fixed version
            if hasattr(vcard, 'adr'):
                addresses = []
                for adr in vcard.adr_list:
                    # Address components: PO Box, Extended Address, Street, City, Region, Postal Code, Country
                    addr_parts = [
                        adr.value.street,
                        adr.value.city,
                        adr.value.region,
                        adr.value.code,
                        adr.value.country
                    ]
                    # Filter out empty parts and join
                    addr_str = ', '.join(part for part in addr_parts if part)
                    if addr_str:
                        addresses.append(addr_str)
                record_dict['Address'] = ';'.join(addresses) if addresses else ''
            
            records.append(record_dict)
        
        if not records:
            raise ValueError("No contacts found in VCF file")
            
        # Convert to DataFrame and save
        logger.info("Converting to DataFrame")
        df = pd.DataFrame(records)
        
        # Save to CSV
        logger.info(f"Saving to CSV: {output_file}")
        df.to_csv(output_file, index=False)
        logger.info("Conversion completed successfully")
        
    except Exception as e:
        logger.error(f"Error during conversion: {str(e)}")
        raise

if __name__ == "__main__":
    # Example usage
    vcf_to_csv('your_input.vcf', 'your_outout.csv')