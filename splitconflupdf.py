import os
import sys
import pdfplumber
from PyPDF2 import PdfReader, PdfWriter
import re

def find_and_split_sections(pdf_path, output_folder="output_sections"):
    # Create output folder
    os.makedirs(output_folder, exist_ok=True)
    print(f"\n📁 All PDFs will be saved in: {os.path.abspath(output_folder)}")

    # Verify input file exists
    if not os.path.exists(pdf_path):
        print(f"\n❌ Error: Input file '{pdf_path}' not found!")
        return None

    # Step 1: Extract TOC
    print("\n🔍 Extracting table of contents...")
    try:
        with pdfplumber.open(pdf_path) as pdf:
            first_page_text = pdf.pages[0].extract_text()
    except Exception as e:
        print(f"\n❌ Error reading PDF: {str(e)}")
        return None
    
    toc_entries = [line.strip() for line in first_page_text.split('\n') if line.strip()]
    print("\n📑 Detected Sections:")
    for i, entry in enumerate(toc_entries, 1):
        print(f"{i}. {entry}")

    # Step 2: Extract page numbers
    toc_with_pages = []
    for entry in toc_entries:
        match = re.search(r'(\d+)$', entry)
        if match:
            toc_with_pages.append((entry, int(match.group(1))))
        else:
            print(f"⚠️ Warning: No page number found in '{entry}' - skipping")

    # Step 3: Calculate ranges
    sections = {}
    reader = PdfReader(pdf_path)
    total_pages = len(reader.pages)
    
    for i in range(len(toc_with_pages)):
        entry, start = toc_with_pages[i]
        end = (toc_with_pages[i+1][1] - 1) if i < len(toc_with_pages) - 1 else total_pages
        sections[entry] = (start, end)
        print(f"🔹 {entry}: pages {start}-{end} (of {total_pages})")

    # Step 4: Split PDF
    print("\n✂️ Creating section PDFs...")
    for section, (start, end) in sections.items():
        writer = PdfWriter()
        try:
            for page_num in range(start - 1, end):
                writer.add_page(reader.pages[page_num])
            
            # Generate safe filename
            filename = (
                re.sub(r'[\[\]]', '', section)    # Remove brackets
                .replace(' ', '_')                # Spaces to underscores
                .replace('.', '_')               # Dots to underscores
                [:50] + '.pdf'                   # Limit length
            )
            output_path = os.path.join(output_folder, filename)
            
            with open(output_path, "wb") as f:
                writer.write(f)
            print(f"✅ Created: {filename} ({end-start+1} pages)")
        except Exception as e:
            print(f"❌ Failed to create {section}: {str(e)}")

    print(f"\n✔️ Processed {len(sections)} sections!")
    return sections

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python split_pdf.py <input.pdf> [output_folder]")
        print("Example: python split_pdf.py input.pdf my_sections")
        sys.exit(1)
    
    pdf_path = sys.argv[1]
    output_folder = sys.argv[2] if len(sys.argv) > 2 else "output_sections"
    
    result = find_and_split_sections(pdf_path, output_folder)
    
    if result:
        print("\n📊 Final Section Ranges:")
        for sec, (start, end) in result.items():
            print(f"{sec}: {start}-{end}")