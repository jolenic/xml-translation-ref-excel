import os
import xlrd
from collections import defaultdict
from xml.etree import ElementTree

#First, get excel file, read into program, and create a dictionary of key-value pairs
#that will be used to modify xml file

#get path for excel file
excel_file_name = 'nato-phonetic-alphabet.xls'
excel_full_file = os.path.abspath(os.path.join('data', excel_file_name))

#for excel reading: read column names into dictionary as key-value pairs
#when parsing xml, use dictionary lookups to change value

#open workbook
wb = xlrd.open_workbook(excel_full_file)
sheet = wb.sheet_by_index(0)

#set up dictionary with default value if no key is found
translations = defaultdict(lambda: 'no key found')

#read values from sheet and input into dictionary as key-value pairs
for i in range(sheet.nrows):
    translations[sheet.cell_value(i, 0)] = sheet.cell_value(i, 1)


###############################################

#Next, access the xml file and use the dictionary to change text

#get path for xml file
xml_file_name = 'books-sample.xml'
xml_full_file = os.path.abspath(os.path.join('data', xml_file_name))

#get element tree for xml file
dom = ElementTree.parse(xml_full_file)

#function for modifying xml text
def title_changes(og_title):
    new_title = translations[og_title]
    return new_title

#find each element in xml and replace text
for title in dom.iterfind("./book/title"):
    print('og title: ' + str(title.text))
    title.text = title_changes(str(title.text))
    print('new title: ' + str(title.text))

#write changes back to xml file
dom.write(xml_full_file)