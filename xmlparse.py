import xml.etree.ElementTree as ET

tree = ET.parse('movies.xml')
root = tree.getroot()

films = []

for item in root.findall('./Movie'):
    film = {}
    film['rating'] = item.attrib['rating']
    for child in item:
        if child.tag == 'Title':
            film['title'] = child.text
            film['runtime'] = child.attrib['runtime']
    films.append(film)
print(films)        



# from bs4 import BeautifulSoup
# with open('movies.xml', 'r') as f:
#     data = f.read()

# Bs_data = BeautifulSoup(data, "xml")
# films = Bs_data.find_all('Movie')
# print(films)