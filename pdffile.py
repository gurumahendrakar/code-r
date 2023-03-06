import PyPDF2


page_read = open(r"C:\Users\mahen\Downloads\Atomic Habits James Clear.pdf",'rb')

reader = PyPDF2.PdfReader(page_read)
page = reader.pages[3]

count=0
for img in page.images:
    with open(str(count)+img.name,'wb') as fp:
        fp.write(img.data)
        count+=1

print(page.extract_text())