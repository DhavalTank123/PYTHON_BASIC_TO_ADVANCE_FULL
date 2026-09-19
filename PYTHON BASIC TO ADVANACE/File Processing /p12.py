# PDF Read & Write

    # PDF Read → PyPDF2
    # PDF Write/Create → reportlab

import PyPDF2

pdf_name = input("Enter PDF file name: ")

with open(pdf_name, "rb") as file:
    pdf_reader = PyPDF2.PdfReader(file)

    print("\nTotal Pages:", len(pdf_reader.pages))

    for page in pdf_reader.pages:
        text = page.extract_text()
        print("\nPDF Content: ")
        print(text)


        