import pdfplumber
import pandas as pd

def extract_pdf_to_excel(pdf_path, output_excel):
    data = []

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                for line in text.split("\n"):
                    data.append([line])

    df = pd.DataFrame(data, columns=["Extracted Text"])
    df.to_excel(output_excel, index=False)

if __name__ == "__main__":
    extract_pdf_to_excel("sample.pdf", "sample_output.xlsx")
