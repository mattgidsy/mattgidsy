import xml.etree.ElementTree as ET

data = '''
<person>
  <name>Chuck</name>
  <phone type="intl">
    +1 734 303 4456
  </phone>
  <email hide="yes" />
</person>'''

tree = ET.fromstring(data) #can blow up if there is a mistake in the XML formatting
print('Name:', tree.find('name').text)#finds the text within the tag 'name'. text gets the text out of the tag
print('Attr:', tree.find('email').get('hide'))#finds the attribute within tag 'email'. get() gets the  attribute out of the tag
