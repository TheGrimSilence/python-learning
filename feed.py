import xml.etree.ElementTree as etree
from typing import Dict

from util.printf import printf

tree = etree.parse('feed.xml')
root = tree.getroot()

printf('tree', tree)
printf('root', root)
printf('tag', root.tag)

for child in root:
	printf('child', child)

printf('root.attrib', root.attrib)
printf('root[4].attrib', root[4].attrib)
printf('root.findall', root.findall('{http://www.w3.org/2005/Atom}entry'))
