import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text()
        doc.close()
        return text
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    text = extract_text_from_pdf("NALAMALAPU VASU REDDY_RESUME.pdf")
    if text:
        with open("resume_text.txt", "w", encoding="utf-8") as f:
            f.write(text)
        print("Text extracted successfully!")
    else:
        print("Failed to extract text") 