# PDF Splitter for Confluence Documents

🔧 **A Python tool to automatically split PDFs into sections based on Table of Contents (TOC)**

## 📌 Features
- Extracts sections from Confluence-generated PDFs
- Creates individual PDFs for each TOC entry
- Preserves original formatting
- Handles complex TOC structures (nested/numbered sections)
- Generates clean filenames automatically

## 🚀 Quick Start
### Prerequisites
- Python 3.8+

### Installation
```bash
# Clone repository
git clone git@github.com:rahmatsayfuddin/splitconflupdf.git
cd splitconflupdf
pip install -r requirements.txt

### Usage

# Basic usage
python split_pdf.py input.pdf

# Specify output directory
python split_pdf.py input.pdf --output my_sections

# Process specific pages (e.g., 5-20)
python split_pdf.py input.pdf --start 5 --end 20