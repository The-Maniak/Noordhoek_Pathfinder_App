import os
import openpyxl
import docxtpl

# File with crewlist:  
current_folder = r"C:\Users\wojte\Desktop\python_projects\Noordhoek_Pathfinder\NHP_apps\uk_ports_crewlist_project"
crewlist_subfolder = os.path.join(current_folder, 'current-crewlist\\')
crewlist_file = os.path.join(crewlist_subfolder, os.listdir(crewlist_subfolder)[0])

# MS Word template folder:
template_subfolder = os.path.join(current_folder, 'ms-word-templates\\')
fal5_template_file = os.path.join(template_subfolder, 'c97 word.docx')
fal4_template_file = os.path.join(template_subfolder, 'c96 word.docx')

# output folder:
output_folder = os.path.join(current_folder, 'ready-documents\\')

# MS Word template files:
fal5_template = docxtpl.DocxTemplate(fal5_template_file)
fal4_template = docxtpl.DocxTemplate(fal4_template_file)

# Creating empty lists to store data to be inserted to MS Word files:
fal5_table_contents = []
fal4_table_contents = []


# Obtaining crew-members data from source file:
def create_uk_crewlist():
    wb = openpyxl.load_workbook(crewlist_file, data_only=True)
    crewlist_sheet = wb['Crewlist']
    number_of_pob = crewlist_sheet["E61"].value
    port_docs_sheet = wb['Port Doc Copy Sheet']
    cell = port_docs_sheet["B3":f"M{number_of_pob + 2}"]

    # Extracting data from vessels crew list document and preparing template contents:
    for number, surname, name, rank, nationality, date_of_birth, place_of_birth, gender, \
        document_type, document_number, document_state, document_expiration_date in cell:
        full_name = f'{surname.value}, {name.value}'
        date_and_place_of_birth = f"{date_of_birth.value}, {place_of_birth.value}".replace(" 00:00:00", '')
        fal5_table_contents.append({
            'no': number.value,
            'full_name': full_name,
            'rank': rank.value,
            'nat': nationality.value,
            'dp_of_b': date_and_place_of_birth,
            'doc_number': document_number.value
        })
        fal4_table_contents.append({
            'no': number.value,
            'full_name': full_name,
            'rank': rank.value
        })

    # Declare template variables:
    fal5_context = {
        'table_contents': fal5_table_contents
    }
    fal4_context = {
        'table_contents': fal4_table_contents
    }

    # Render automated reports:
    fal5_template.render(fal5_context)
    fal5_template.save(os.path.join(output_folder, "fal5.docx"))
    fal4_template.render(fal4_context)
    fal4_template.save(os.path.join(output_folder, "fal4.docx"))
    # debug statements
    # print(fal5_table_contents)
    # print(fal4_table_contents)


if __name__ == '__main__':
    create_uk_crewlist()
    # print("hey")
