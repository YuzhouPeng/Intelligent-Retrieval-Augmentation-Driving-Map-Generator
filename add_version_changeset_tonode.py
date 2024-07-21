
import xml.etree.ElementTree as ET

def add_version_to_nodes(filename, default_version="1",default_changeset="1",default_timestamp="2022-11-20T17:08:59Z"):
    """
    Add a version attribute to nodes that do not have it.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        for node in root.findall('.//node'):
            if 'version' not in node.attrib:
                print(1)
                node.set('version', default_version)
            if 'changeset' not in node.attrib:
                print(2)
                node.set('changeset', default_changeset)
            if 'timestamp' not in node.attrib:
                print(3)
                node.set('timestamp', default_timestamp)

        # Write data with version to a new file
        versioned_filename = f"versioned_{filename}"
        tree.write(versioned_filename, encoding='utf-8', xml_declaration=True)
        print(f"Version attribute added to nodes. Data saved to {versioned_filename}")
        
    except Exception as e:
        print(f"Error adding version attribute to nodes: {e}")

if __name__ == '__main__':
    add_version_to_nodes("osm_bbox_data_39.909187_116.397455_500.osm")
    