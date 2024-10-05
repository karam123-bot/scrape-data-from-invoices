import fitz  # PyMuPDF
import re

# Path to the PDF file
pdf_path = r'D:\django_employee_qr\DEMO\OPEN RPA\pdf_files\sample-invoice.pdf'

# Define the regular expression pattern to find invoice numbers
invoice_number_pattern = re.compile(r'(?i)INVOICE:\s*[:\s-]+([A-Za-z\d]+(?:[-\s][A-Za-z\d]+)*)')

# Define the regular expression pattern to find dates
invoice_date_pattern = re.compile(r'DATE\s*[:\s\/]+(?:\d{1,2}/\d{1,2}/\d{4}|\d{1,2}\s+(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{4})', re.IGNORECASE)

try:
    # Open the PDF file
    with fitz.open(pdf_path) as pdf_document:
        # Extract text from each page and concatenate
        text = '\n'.join([page.get_text() for page in pdf_document])
        
        # Search for invoice numbers in the text
        invoice_number_matches = invoice_number_pattern.findall(text)
        # Search for dates in the text
        invoice_date_matches = invoice_date_pattern.findall(text)
        # Print invoice numbers
        if invoice_number_matches:
            print("Invoice numbers found:")
            for invoice_number_match in invoice_number_matches:
                print(invoice_number_match.strip())
        else:
            print("No invoice numbers found in the PDF.")

        # Print dates
        if invoice_date_matches:
            print("\nDates found:")
            for invoice_date_match in invoice_date_matches:
                print(invoice_date_match.strip())
        else:
            print("No dates found in the PDF.")
except Exception as e:
    print(f"An error occurred while processing the PDF: {e}")


