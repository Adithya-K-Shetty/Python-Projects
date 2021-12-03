import PyPDF2
wannaContinue = True
pdfWriter = PyPDF2.PdfFileWriter()
while wannaContinue:
    pdf_Name = input("Enter The Pdf Name : ")  #Input Pdf Should be residing in the same directory in order for the program to open the pdf
    inFile = open(pdf_Name+'.pdf'   ,'rb')
    pdfReader = PyPDF2.PdfFileReader(inFile)
    pageMode = input("type 's' to get the random sequence of page,'r' to specific range of page : ").lower()
    if pageMode == 's':
        pageNumberList = []
        numberOfPage = int(input("Enter the number of pages : "))
        for count in range(numberOfPage):
            pageNum = int(input("Enter the page number : "))
            pageNumberList.append(pageNum-1)
        for page in pageNumberList:
            newPage = pdfReader.getPage(page)
            pdfWriter.addPage(newPage)
        
    elif pageMode == 'r':
        startPageNum = int(input("Enter the starting Page Number :  "))
        endPageNum = int(input("Enter the ending page NUmber : "))
        for page in range(startPageNum-1,endPageNum):
            newPage = pdfReader.getPage(page)
            pdfWriter.addPage(newPage)
        
    else:
        print("Enter A Valid Input")

    wannaReapeat = input("Wanna Continue (y/n) : ").lower()
    if wannaReapeat == 'y':
        wannaContinue = True
    elif wannaReapeat == 'n':
        wannaContinue = False

output_pdf_name = input("Enter the name of the output pdf : ")
outFile = open(output_pdf_name+'.pdf','wb')
pdfWriter.write(outFile)

inFile.close()
outFile.close()
    
            
