import zipfile
import io
import PyPDF2 as pf

input_zip_path = "" #enter input path
output_zip_path = "" #enter output path 

in_memory = io.BytesIO()

with zipfile.ZipFile(input_zip_path, 'r') as input_zip, zipfile.ZipFile(in_memory, 'w', zipfile.ZIP_DEFLATED) as output_zip:
    for file_name in input_zip.namelist():
        if file_name.lower().endswith('.pdf'):
                with input_zip.open(file_name) as file:
                    reader = pf.PdfReader(io.BytesIO(file.read()))

                    if len(reader.pages) >= 3:
                        writer = pf.PdfWriter()
                        writer.add_page(reader.pages[2])  
                        pdf_bytes = io.BytesIO()
                        writer.write(pdf_bytes)
                        pdf_bytes.seek(0)

                        name = file_name.split('/')[-1].split('\\')[-1]
                        output_name = f"{name[:-4]}.pdf"

                        output_zip.writestr(output_name, pdf_bytes.read())

                        print(f" {output_name}")
                    else:
                        print(f" error: {file_name}")



with open(output_zip_path, "wb") as f:
    f.write(in_memory.getvalue())

print(f"Saved Files: {output_zip_path}")
