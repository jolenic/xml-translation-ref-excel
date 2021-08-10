import os
from xml.etree import ElementTree

file_name = 'books-sample.xml'
full_file = os.path.abspath(os.path.join('data', file_name))

dom = ElementTree.parse(full_file)

def title_changes(og_title):
    new_title = og_title[0:3]
    return new_title

for title in dom.iterfind("./book/title"):
    print('og title: ' + str(title.text))
    title.text = title_changes(str(title.text))
    print('new title: ' + str(title.text))

dom.write(full_file)

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
