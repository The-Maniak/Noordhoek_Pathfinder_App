import os
import fitz
import pandas as pd
import pyodbc

# Defining file directories:
app_directory = r'Y:\DeckDept\Bridge Resthours\Maniak\python_projects\Noordhoek_Pathfinder\NHP_apps\ntm_picker'
# Source directory and files:
current_ntm_directory = os.path.join(app_directory, 'current_ntm')
current_ntm_filename = os.listdir(current_ntm_directory)[0]
current_ntm_filepath = os.path.join(current_ntm_directory, current_ntm_filename)
# This part adds a value to be cleaned from the corrections, ie. Wk11/23 depending on the filename length
ntm_week_year = f'Wk{current_ntm_filename[:2]}/{current_ntm_filename[6:8]}'
# Output directory and files:
output_directory = os.path.join(app_directory, 'output')
# output_filepath_csv = os.path.join(output_directory, 'this_week_ntms.csv')
output_filepath_xslx = os.path.join(output_directory, 'this_week_ntms.xlsx')


def finding_notices(current_ntm_filepath, searched_phrase):
    ntm = fitz.open(current_ntm_filepath)
    pages_with_notices = []
    corrections = []
    for page in ntm:
        text = page.get_text()
        if searched_phrase in text:
            pages_with_notices.append(page.number)
            corrections.append(page.get_text())
    ntm.close()
    return corrections


def all_corrections_in_ntm(list_of_corrections):
    all_corrections = {}
    for n in range(len(list_of_corrections)):
        page = list_of_corrections[n]
        page_splitted = page.splitlines()
        page_cleaned = [x for x in page_splitted if x not in useless_elements]
        page_concatenated = []
        i = 0
        while i < len(page_cleaned):
            try:
                if not page_cleaned[i].rstrip('PT').isalpha():
                    page_concatenated.append(page_cleaned[i])
                    i += 1
                else:
                    page_concatenated.append(f'{page_cleaned[i]} {page_cleaned[i + 1]}')
                    i += 2
            except IndexError:
                print('There was an index error but never mind')
                break
        partial_dictionary = dict(zip(page_concatenated[::2], page_concatenated[1::2]))
        all_corrections.update(partial_dictionary)
    return all_corrections


# Specifying the phrase which will generate a list of charts and corrections they're affected by.
searched_phrase = 'INDEX OF CHARTS AFFECTED'

# Calling function to extract the text with corrections, which still needs to be processed.
list_of_corrections = finding_notices(current_ntm_filepath, searched_phrase)

# List of elements which need to be removed from extracted text so that only pure charts and their corections remain:
useless_elements = ['II', '2.3', '2.4', '2.5', 'INDEX OF CHARTS AFFECTED', 'Admiralty Chart No.', 'Notices',
                    'Admiralty Chart No.', 'German', 'Indian', 'International', 'Chart No.', 'Japanese',
                    'Australian', f'{ntm_week_year}', 'New Zealand']

# Extracting all chart corrections from the raw text from provided NTM:
all_corrections = all_corrections_in_ntm(list_of_corrections)

# Database part - collecting a list of charts in stock currently on board:
chart_db_directory = os.path.join(r'Y:\DeckDept\navigation\Nautical Charts', 'Small_corrections_database.accdb')
conn_str = (
    r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};'
    f'DBQ={chart_db_directory};'
)
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()
cursor.execute("SELECT CHARTNUMBER, NUMBERADDITION FROM ListOfCharts")

# Processing the extracted list of charts in stock into suitable format:
chart_suffixes = ['A', 'B', 'C', 'D']
chart_prefixes = ['DE', 'NO']
charts_on_board = []
for row in cursor.fetchall():
    try:
        chart = (list(row))
        if chart[1] in chart_suffixes:
            charts_on_board.append(f'{chart[0]:.0f}{chart[1]}')
        elif chart[1] in chart_prefixes:
            charts_on_board.append(f'{chart[1]} {chart[0]:.0f}')
        else:
            charts_on_board.append(f'{chart[0]:.0f}')
    except TypeError as e:
        pass

# Cross-referencing all corrections in the current NTM with the list of charts in stock onboard:
our_charts_with_corrections = {}
for chart in charts_on_board:
    if chart in all_corrections.keys():
        our_charts_with_corrections[chart] = all_corrections[chart]

# Saving the cross-referenced charts and corrections into a PD DF and then into a CSV file.
our_charts_series = pd.Series(data=our_charts_with_corrections.keys())
our_corrections_series = pd.Series(data=our_charts_with_corrections.values())
to_be_corrected = pd.concat([our_charts_series, our_corrections_series], axis=1)
to_be_corrected.sort_values(0, ascending=True, inplace=True)
to_be_corrected.columns = ['Chart_number', 'Correction_number']
to_be_corrected.to_excel(excel_writer=output_filepath_xslx, sheet_name='corrections', index=False)
# to_be_corrected.to_csv(output_filepath, index=False, header=True)
