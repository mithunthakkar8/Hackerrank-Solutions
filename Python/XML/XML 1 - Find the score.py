# Import the sys module to read input from standard input
import sys

# Import the ElementTree module for parsing and handling XML data
import xml.etree.ElementTree as etree

# Define a function to calculate the total number of attributes in an XML tree
def get_attr_number(node):
    # Initialize a counter to store the total number of attributes
    score = 0

    # Iterate over all elements in the XML tree (including the root and its children)
    for element in node.iter():
        # Add the number of attributes in the current element to the score
        score += len(element.attrib)
    
    # Return the total number of attributes
    return score

# Main execution block
if __name__ == '__main__':
    # Read and ignore the first line (typically contains metadata or the number of lines)
    sys.stdin.readline()
    
    # Read the remaining XML data from standard input
    xml = sys.stdin.read()
    
    # Parse the XML data and create an ElementTree object
    tree = etree.ElementTree(etree.fromstring(xml))
    
    # Get the root element of the XML tree
    root = tree.getroot()
    
    # Calculate and print the total number of attributes in the XML tree
    print(get_attr_number(root))
