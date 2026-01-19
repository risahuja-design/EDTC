#!/usr/bin/env python3
"""
Convert EDTC Portfolio HTML to PDF using WeasyPrint
"""

from weasyprint import HTML
import os

def convert_html_to_pdf():
    """Convert the EDTC portfolio HTML file to PDF"""

    # Define file paths
    html_file = '/home/user/EDTC/edtc_portfolio.html'
    output_dir = '/mnt/user-data/outputs'
    pdf_file = os.path.join(output_dir, 'EDTC_Portfolio.pdf')

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    print(f"Converting {html_file} to PDF...")
    print(f"Output location: {pdf_file}")

    # Convert HTML to PDF
    HTML(filename=html_file).write_pdf(pdf_file)

    print(f"✓ PDF successfully created at: {pdf_file}")

    # Get file size
    file_size = os.path.getsize(pdf_file)
    file_size_mb = file_size / (1024 * 1024)
    print(f"✓ File size: {file_size_mb:.2f} MB")

    return pdf_file

if __name__ == '__main__':
    try:
        pdf_path = convert_html_to_pdf()
        print(f"\n✓ Success! Your EDTC portfolio is ready at: {pdf_path}")
    except Exception as e:
        print(f"\n✗ Error: {str(e)}")
        raise
