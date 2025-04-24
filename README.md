# Export Conflu PDF
Click Space setting and Export
![image](https://github.com/user-attachments/assets/ae8cdc0d-f489-405a-8ad6-85480443df0c)
Select PDF
![image](https://github.com/user-attachments/assets/f25aa688-c8c6-442b-b1e0-c44a6759fe89)
Select What to Export
![image](https://github.com/user-attachments/assets/c964167c-4c39-490d-b4e2-c6dc44905097)
![image](https://github.com/user-attachments/assets/168a6e51-2f6e-42fb-8745-6ef2907112d1)

If your ToC (Table of Content) like this, **you can use this tool**
![image](https://github.com/user-attachments/assets/16f92c7f-1b45-4799-8c6c-cfb77ec328a9)
 


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
python splitconflupdf.py input.pdf

# Specify output directory
python splitconflupdf.py input.pdf --output my_sections
