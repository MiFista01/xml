# from bs4 import BeautifulSoup
# with open('money.xml','r') as q:
#     data = q.read()
# file_data = BeautifulSoup(data, "xml")
# countries = file_data.find_all('Country')
# print()
# print("========================================")
# print(countries)



import xml.etree.ElementTree as ET

tree = ET.parse("my_folder/ivkhk.xml")
root = tree.getroot()

mass = []
for q in root.findall('./branch'): #name branch
    branch = {}
    professions = []

    branch['Branch name'] = q.attrib['name']
    for w in q:
        profession = {}
        groups = []
        
        profession['Profession name'] = w.attrib['name']
        professions.append(profession)
        for e in w:
            group = {}
            students = []
            
            group['Group name'] = e.attrib['name']
            groups.append(group)
            for r in e:
                student = {}
                for t in r:
                    if t.tag == 'name':
                        student['name'] = t.text
                    if t.tag == 'surname':
                        student['surname'] = t.text
                    if t.tag == 'birthday':
                        student['birthday'] = t.text
                students.append(student)
                group['Students'] = students
        profession['Groups'] = groups
    branch['Professions'] = professions
    
    mass.append(branch)
    

for q in mass:
    for w in q:
        if w == 'Branch name':
            print("Brunch:",q[w])
        if w == 'Professions':
            print(w+":")
            for e in q[w]:
                for r in e:
                    if r == 'Profession name':
                        print(e[r])
                    if r == 'Groups':
                        print(r+":")
                        for t in e[r]:
                            for y in t:
                                if y == 'Group name':
                                    print(t[y])
                                if y == 'Students':
                                    print(y+":")
                                    for u in t[y]:
                                        name = ""
                                        surname = ""
                                        birthday = ""
                                        for i in u:
                                            if i == "name":
                                                name = u[i]
                                            if i == "surname":
                                                surname = u[i]
                                            if i == "birthday":
                                                birthday = u[i]
                                        print("Name:",name,"Surname:",surname,"Birthday:",birthday)
