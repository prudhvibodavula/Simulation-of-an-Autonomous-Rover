import xml.etree.ElementTree as ET
import xmlschema

# Parse model.sdf XML data from file to tree structure
tree_sdf = ET.parse('model.sdf')
root_sdf = tree_sdf.getroot()
print(" model.sdf-element tree ------ ", ET.tostring(root_sdf))

# Parse model.config XML data from file to tree structure
tree_config = ET.parse('model.config')
root_config = tree_config.getroot()
print(" model.config-element tree -------- ", ET.tostring(root_config))

# Validate model.sdf XML with comparison with XSD
xsd_sdf = xmlschema.XMLSchema('model_sdf.xsd')
result = xsd_sdf.is_valid(tree_sdf)
print(' model.sdf is valid - {}'.format(result))

# Validate model.sdf XML with comparison with XSD
xsd_config = xmlschema.XMLSchema('model_config.xsd')
result = xsd_config.is_valid(tree_config)
print(' model.config is valid - {}'.format(result))

