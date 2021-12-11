import csv,docx
inputFile = open("empData.csv","wt",newline='')
writer = csv.writer(inputFile)
writer.writerow(['FNAME','LNAME','STATE','COUNTRY','PINCODE'])
num_data = int(input("Enter the number of invites ?"))
for i in range(num_data):
    writer.writerow([input("Enter The Name : "),input("Enter The Last Name :"),input("Enter The State : "),input("Enter The Country : "),int(input("Enter The Pincode : "))])
    print("\n")
inputFile.close()


dataFile = open("empData.csv","rt")
reader = csv.reader(dataFile)
data = list(reader)
doc = docx.Document()

for item in range(1,len(data)):
    doc.add_paragraph("To,")
    for index in range(len(data[0])):
        if index == 0:
            doc.add_paragraph(data[item][0]+" "+data[item][1])
        elif index > 1:
            doc.add_paragraph(data[item][index])

counter = len(data[0]) - 1
while counter < len(doc.paragraphs)-1:
    doc.paragraphs[counter].runs[0].add_break(docx.text.run.WD_BREAK.PAGE)
    counter+=5


doc.save("Invitation8.docx")
dataFile.close()