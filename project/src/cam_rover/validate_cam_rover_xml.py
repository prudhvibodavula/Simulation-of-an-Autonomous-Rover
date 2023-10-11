import xml.etree.ElementTree as ET
import xmlschema

# Parse roverModel.sdf XML data from file to tree structure
tree_sdf = ET.parse('roverModel.sdf')
root_sdf = tree_sdf.getroot()
print(" roverModel.sdf-element tree ------ ", ET.tostring(root_sdf))

# Validate roverModel.sdf XML with comparison with XSD
xsd_sdf = xmlschema.XMLSchema('roverModel.xsd')
result = xsd_sdf.is_valid(tree_sdf)
print(' roverModel.sdf is valid - {}'.format(result))
