import os

import xlrd
from collections import defaultdict
from xml.etree import ElementTree as ET
#
# # may need to run pip install xlrd in console?  Not 100% sure
#
# # First, get excel file, read into program, and create a dictionary of key-value pairs
# # that will be used to modify xml file
#
# # get path for excel file
# excel_file_name = 'nato-phonetic-alphabet.xls'
# excel_full_file = os.path.abspath(os.path.join('data', excel_file_name))
#
# # for excel reading: read column names into dictionary as key-value pairs
# # when parsing xml, use dictionary lookups to change value
#
# # open workbook
# wb = xlrd.open_workbook(excel_full_file)
# sheet = wb.sheet_by_index(0)
#
# # set up dictionary with default value if no key is found
# translations = defaultdict(lambda: 'no key found')
#
# # read values from sheet and input into dictionary as key-value pairs
# for i in range(sheet.nrows):
#     translations[sheet.cell_value(i, 0)] = sheet.cell_value(i, 1)

###############################################

# Next, access the xml file and use the dictionary to change text

# get path for xml file
xml_file_name = 'businessView.xml'
xml_full_file = os.path.abspath(os.path.join('data', xml_file_name))

# get element tree for xml file
tree = ET.parse(xml_full_file)
root = tree.getroot()

# #Uses a list comprehension and element tree's iterparse function to create a dictionary containing the namespace prefix and it's uri. The underscore is utilized to remove the "start-ns" output from the list.
# namespaces = {node[0]: node[1] for _, node in ET.iterparse(xml_full_file, events=['start-ns'])}
# #Iterates through the newly created namespace list registering each one.
# for key, value in namespaces.items():
#     ET.register_namespace(key, value)
#     print(key + ',' + value)
#
# #The curly brackets are needed around the uri when using Element Tree's find command with a manually passed namespace.
# default_ns = "{" + namespaces[""] + "}"
# # By inserting your namespace variable immediately before the search term your code will return the results you expect.
# # for elem in root.findall(".//" + default_ns + "/namespace/[name='Business view']"):
# # for namespace in root.findall(".//" + default_ns + "/namespace/namespace"):

# for name in tree.iterfind('./querySubject/queryItem/name'):
for name in tree.iterfind('.//name'):
    if name.attrib['locale'] == "en":
        print(name.text)

print('test')

# # function for modifying xml text
# def title_changes(og_title):
#     new_title = translations[og_title[0]]
#     return new_title


# # find each element in xml and replace text
# for title in tree.iterfind("./to_change/book/title"):
#     print('og title: ' + str(title.text))
#     # title.text = title_changes(str(title.text))
#     print('new title: ' + str(title.text))

# write changes back to xml file
tree.write(xml_full_file)
