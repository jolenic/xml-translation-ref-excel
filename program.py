import os
from xml.etree import ElementTree

#get path for xml file
xml_file_name = 'books-sample.xml'
xml_full_file = os.path.abspath(os.path.join('data', xml_file_name))

#get path for excel file
excel_file_name = 'nato-phonetic-alphabet.xlsx'
excel_full_file = os.path.abspath(os.path.join('data', excel_file_name))



#get element tree for xml file
dom = ElementTree.parse(xml_full_file)

#function for modifying xml text
def title_changes(og_title):
    new_title = og_title[0]
    return new_title

#find each element in xml and replace text
for title in dom.iterfind("./book/title"):
    print('og title: ' + str(title.text))
    title.text = title_changes(str(title.text))
    print('new title: ' + str(title.text))

#write changes back to xml file
dom.write(xml_full_file)

#for excel reading: read column names into dictionary as key-value pairs
#when parsing xml, use dictionary lookups to change value


# books = dom.findall('book')
#
# for b in books:
#     title = b.find('title').text
#     author = b.find('author').text
#     genre = b.find('genre').text
#
#     print(' * {}, by {} [{}] '.format(
#         title, author, genre
#     ))
