import io
import os
import fitz  # PyMuPDF
from PIL import Image

# যে ফোল্ডারের সব PDF সাইজ কমাতে চান তার পাথ দিন:
FOLDER_PATH = r"C:\Users\sohag\Downloads\Telegram Desktop"


def compress_single_pdf(
    input_path, output_path, dpi=120, quality=50, grayscale=True
):
    """একটি PDF ফাইলের সাইজ কমানোর ফাংশন"""
    src_doc = fitz.open(input_path)
    out_doc = fitz.open()

    for page_num in range(len(src_doc)):
        page = src_doc[page_num]
        pix = page.get_pixmap(dpi=dpi)
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

        # দলিল বা খতিয়ান সাদা-কালো (Grayscale) করলে সাইজ অনেক বেশি কমে
        if grayscale:
            img = img.convert("L")

        buffer = io.BytesIO()
        img.save(buffer, format="JPEG", quality=quality, optimize=True)
        buffer.seek(0)

        rect = page.rect
        new_page = out_doc.new_page(width=rect.width, height=rect.height)
        new_page.insert_image(rect, stream=buffer.read())

    out_doc.save(output_path, garbage=4, deflate=True)
    out_doc.close()
    src_doc.close()


def process_all_pdfs_in_folder(
    folder_path, dpi=120, quality=50, grayscale=True
):
    if not os.path.exists(folder_path):
        print(f"ভুল পাথ: '{folder_path}' ফোল্ডারটি খুঁজে পাওয়া যায়নি।")
        return

    # কম্প্রেস করা ফাইলগুলো রাখার জন্য আলাদা ফোল্ডার তৈরি
    output_dir = os.path.join(folder_path, "compressed_files")
    os.makedirs(output_dir, exist_ok=True)

    # ফোল্ডারের সব .pdf ফাইল খুঁজে বের করা
    pdf_files = [
        f
        for f in os.listdir(folder_path)
        if f.lower().endswith(".pdf")
        and not f.startswith("._")
        and os.path.isfile(os.path.join(folder_path, f))
    ]

    total_files = len(pdf_files)
    if total_files == 0:
        print("ফোল্ডারে কোনো PDF ফাইল পাওয়া যায়নি।")
        return

    print("=" * 60)
    print(f"মোট {total_files} টি PDF ফাইল পাওয়া গেছে। কাজ শুরু হচ্ছে...\n")

    total_original_mb = 0
    total_compressed_mb = 0

    for idx, filename in enumerate(pdf_files, start=1):
        input_file = os.path.join(folder_path, filename)
        output_file = os.path.join(output_dir, filename)

        orig_size = os.path.getsize(input_file) / (1024 * 1024)
        total_original_mb += orig_size

        print(f"[{idx}/{total_files}] কাজ চলছে: {filename}")
        print(f"    আসল সাইজ: {orig_size:.2f} MB")

        try:
            compress_single_pdf(
                input_file,
                output_file,
                dpi=dpi,
                quality=quality,
                grayscale=grayscale,
            )
            new_size = os.path.getsize(output_file) / (1024 * 1024)
            total_compressed_mb += new_size
            saved = ((orig_size - new_size) / orig_size) * 100
            print(f"    নতুন সাইজ: {new_size:.2f} MB (কমেছে {saved:.1f}%)")
        except Exception as e:
            print(f"    ত্রুটি: ফাইলটি প্রসেস করা যায়নি ({e})")

        print("-" * 40)

    total_saved_percent = (
        (total_original_mb - total_compressed_mb) / total_original_mb
    ) * 100
    print("=" * 60)
    print("সবগুলো ফাইলের কাজ সম্পন্ন হয়েছে!")
    print(f"আসল মোট সাইজ:   {total_original_mb:.2f} MB")
    print(f"নতুন মোট সাইজ:   {total_compressed_mb:.2f} MB")
    print(f"মোট জায়গা বেঁচেছে: {total_saved_percent:.1f}%")
    print(f"ফাইলগুলো রয়েছে:   {output_dir}")
    print("=" * 60)


if __name__ == "__main__":
    # দলিলের জন্য dpi=120 এবং quality=50 যথেষ্ট
    # রঙিন রাখতে চাইলে grayscale=False করে দিন
    process_all_pdfs_in_folder(
        FOLDER_PATH, dpi=120, quality=50, grayscale=True
    )