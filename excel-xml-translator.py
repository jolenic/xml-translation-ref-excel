import os
import sys

import xlrd
from xml.etree import ElementTree as ET

# may need to run pip install xlrd in console?  Not 100% sure

# First, get excel file, read into program, and create a dictionary of key-value pairs
# that will be used to modify xml file

# get path for excel file - copy it in directly and add an r in front of the string so that '/'s won't mess it up
# file must be xls, not xlsx
excel_full_file = r"C:\Users\jenni\PycharmProjects\xml-translation-ref-excel\data\nato-phonetic-alphabet.xls"

# for excel reading: read column names into dictionary as key-value pairs
# when parsing xml, use dictionary lookups to change value

# open workbook and sheet, assuming your desired sheet is the first oen
wb = xlrd.open_workbook(excel_full_file)
sheet = wb.sheet_by_index(0)

# set up dictionary for value lookups
translations = dict()

# read values from sheet and input into dictionary as key-value pairs
# change the values to match the specific columns you're looking for on your sheet
for i in range(sheet.nrows):
    translations[sheet.cell_value(i, 0)] = sheet.cell_value(i, 1)

###############################################

# Next, access the xml file and use the dictionary to change text

# The workaround I have right now requires you to copy the entire namespace you want changes in and put it in its own
# xml file.  You can copy-paste it back into the original after it's been processed.  Not elegant but it should work


# get path for new xml file - copy it in directly and add an r in front of the string so that '/'s won't mess it up
xml_full_file = r"C:\Users\jenni\PycharmProjects\xml-translation-ref-excel\data\businessView.xml"

# get element tree for xml file
tree = ET.parse(xml_full_file)
root = tree.getroot()

#########################################################
# To make sure you're targeting the right elements, run this before you do anything else

# iterates through file looking for all name elements
print("Items to be run through translator:")
found_items = 0
for name in tree.findall('./querySubject/queryItem/name'):
    if name.attrib['locale'] == "en":
        print(name.text)
        found_items += 1
print("Total items found: " + str(found_items))
sys.exit()
#########################################################

# If that is targeting the correct items, comment it out and continue

found_items = 0
for name in tree.findall('./querySubject/queryItem/name'):
    if name.attrib['locale'] == "en":
        print(name.text)
        found_items += 1
print("Total items found: " + str(found_items))

# create counters to confirm changes made
changed = 0
ignored = 0


# function for modifying xml text
def name_changes(og_name):
    if og_name in translations:
        new_name = translations[og_name]
        global changed
        changed += 1
    else:
        new_name = og_name
        global ignored
        ignored += 1
    return new_name


# find each element in xml and replace text
for name in tree.findall('./querySubject/queryItem/name'):
    if name.attrib['locale'] == "en":
        print("Original text: " + str(name.text))
        name.text = name_changes(str(name.text))
        print("New text: " + str(name.text))

# write changes back to xml file
print('Changed: ' + str(changed) + ', Ignored: ' + str(ignored))
tree.write(xml_full_file)
