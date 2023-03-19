import os
import xlrd
import pandas as pd

# Specifying filenames and directories
app_directory = r'Y:\DeckDept\Bridge Resthours\Maniak\python_projects\Noordhoek_Pathfinder\NHP_apps\qinsy_voyage_planning'
# Source NTM directory:
source_directory = os.path.join(app_directory, 'source_voyage_plan')
voyage_plan_name = os.listdir(source_directory)[0]
voyage_plan = os.path.join(source_directory, voyage_plan_name)
# Output directory
output_directory = os.path.join(app_directory, 'csv_voyage_plan')
csv_file_name = f'{voyage_plan_name[:-4]}.csv'
output_file_path = os.path.join(output_directory, csv_file_name)


# Defining a function for reading latitues and longitudes:
def extract_data_from_excel(voyage_plan):
    """Function which reads the waypoint coordinates from commonly used on board MS Excel xls sheet. It returns
    a list consisting of two lists, first with latitudes, second with longitudes."""
    # Reading vessel format voyage plan:
    book = xlrd.open_workbook(voyage_plan)
    sh = book.sheet_by_name('passageplan')
    latitudes = []
    longitudes = []
    for i in range(9, 101):
        value = sh.cell_value(rowx=i, colx=0)
        latitude = sh.cell_value(rowx=i, colx=3)
        longitude = sh.cell_value(rowx=i, colx=5)
        if value:
            latitudes.append(latitude)
            longitudes.append(longitude)
        else:
            break
    coordinates = [latitudes, longitudes]
    return coordinates


# Function reading the coordinates and adopting them to Qinsy readable format:
def reformatting_coordinates(list_of_values, plus_sign, minus_sign):
    """Function taking either latitudes or longitudes of values in the voyage plan and converting them into
    a format which Qinsy is accepting for passage plans."""
    for i in range(len(list_of_values)):
        value = str(list_of_values[i])
        decimal_index = value.index('.')
        decimal_from_end_position = len(value) - decimal_index
        if value[0] == '-':
            value = value.lstrip('-')
        if decimal_from_end_position == 2:
            value = f'{value}0'
        if list_of_values[i] >= 0:
            if decimal_index == 5:
                list_of_values[i] = f'{value[:3]}:{value[3:]}{plus_sign}'
            elif decimal_index == 4:
                list_of_values[i] = f'0{value[:2]}:{value[2:]}{plus_sign}'
            elif decimal_index == 3:
                list_of_values[i] = f'00{value[:1]}:{value[1:]}{plus_sign}'
            elif decimal_index == 2:
                list_of_values[i] = f'000:{value}{plus_sign}'
            else:
                list_of_values[i] = f'000:0{value}{plus_sign}'
        else:
            if decimal_index == 5:
                list_of_values[i] = f'{value[:3]}:{value[3:]}{minus_sign}'
            elif decimal_index == 4:
                list_of_values[i] = f'0{value[:2]}:{value[2:]}{minus_sign}'
            elif decimal_index == 3:
                list_of_values[i] = f'00{value[:1]}:{value[1:]}{minus_sign}'
            elif decimal_index == 2:
                list_of_values[i] = f'000:{value}{minus_sign}'
            else:
                list_of_values[i] = f'000:0{value}{minus_sign}'
    return list_of_values


def main():
    """Function executing all processes within this script."""
    # Separating latitudes and longitudes from each other for further processing:
    coordinates = extract_data_from_excel(voyage_plan)
    latitudes = coordinates[0]
    longitudes = coordinates[1]
    # Lists with Qinsy format coordinates:
    latitudes = reformatting_coordinates(latitudes, 'N', 'S')
    longitudes = reformatting_coordinates(longitudes, 'E', 'W')
    # Creating Pandas series and df for csv export:
    latitudes_series = pd.Series(data=latitudes)
    longitudes_series = pd.Series(data=longitudes)
    coordinates = pd.concat([latitudes_series, longitudes_series], axis=1)
    coordinates.to_csv(output_file_path, index=False, header=False)


if __name__ == '__main__':
    main()
