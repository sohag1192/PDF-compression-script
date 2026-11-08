
# PDF Compression Script

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/sohag1192/PDF-compression-script?style=social)](https://github.com/sohag1192/PDF-compression-script)

A fast, lightweight Python tool designed to drastically reduce the file size of scanned PDF documents (such as legal land deeds/দলিল, khatian/খতিয়ান, receipts, and government forms) by **70% to 90%** while keeping text sharp and readable.

---

## ⚡ Features

- **Batch Processing:** Scans an entire directory and compresses all `.pdf` files in one run.
- **Scanned Document Optimization:** Re-renders high-DPI scans using adaptive JPEG/Grayscale stream compression.
- **Safe Execution:** Saves compressed outputs to a dedicated `compressed_files/` folder without touching or overwriting original files.
- **Detailed Size Logging:** Displays page-by-page progress, original vs. compressed file sizes (in MB), and the percentage of saved storage space.
- **Configurable Balance:** Easily adjust DPI, image quality, and color mode (Grayscale vs. Color).

---

## 📦 Requirements

- Python 3.8 or higher
- [PyMuPDF (`fitz`)](https://pymupdf.readthedocs.io/)
- [Pillow (PIL)](https://pillow.readthedocs.io/)

---

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone [https://github.com/sohag1192/PDF-compression-script.git](https://github.com/sohag1192/PDF-compression-script.git)
cd PDF-compression-script

```

### 2. Install Dependencies

```bash
pip install pymupdf pillow

```

### 3. Configure File Path

Open `compressor.py` in your code editor and set `FOLDER_PATH` to the directory containing your PDF files:

```python
FOLDER_PATH = r"C:\Users\sohag\Downloads\Telegram Desktop"

```

### 4. Run the Script

```bash
python compressor.py

```

All compressed documents will be saved inside:

```text
<FOLDER_PATH>/compressed_files/

```

---

## ⚙️ Configuration & Tuning

You can adjust compression parameters inside `compressor.py` to balance file size against visual clarity:

```python
process_all_pdfs_in_folder(
    FOLDER_PATH,
    dpi=120,          # Resolution (DPI)
    quality=50,       # Compression quality (1-100)
    grayscale=True    # Convert to black & white
)

```

| Parameter | Recommended Value | Description |
| --- | --- | --- |
| `dpi` | `120` | Output resolution. `100` for extreme compression; `150` for fine Bengali fonts. |
| `quality` | `50` | JPEG compression level (`1–100`). `40–60` is ideal for official records. |
| `grayscale` | `True` | Set to `False` if preserving colored signatures, official seals, or stamps is required. |

### Recommended Profiles

* **Maximum Compression (Targeting < 1 MB):**
```python
process_all_pdfs_in_folder(FOLDER_PATH, dpi=100, quality=40, grayscale=True)

```


* **Preserve Color & Seals (High Clarity):**
```python
process_all_pdfs_in_folder(FOLDER_PATH, dpi=150, quality=65, grayscale=False)

```



---

## 📁 Repository Structure

```text
PDF-compression-script/
├── compressor.py        # Main execution script
├── .gitignore           # Prevents uploading heavy PDF files to GitHub
├── LICENSE              # MIT License
└── README.md            # Documentation

```

---

## 🔒 Privacy & Safety Notice

To prevent confidential land records, financial documents, or personal PDFs from accidentally getting pushed to your public repository, ensure your `.gitignore` contains:

```text
*.pdf
compressed_files/
__pycache__/
*.pyc
.venv/

```

---

## 📄 License

This project is licensed under the [MIT License](https://www.google.com/search?q=LICENSE).

