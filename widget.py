import os
import shutil
from PySide6.QtCore import Qt, QProcess, QUrl
from PySide6.QtWidgets import QWidget, QFileDialog, QMessageBox
from PySide6.QtGui import QFont, QDesktopServices
from ui_widget_NHP import Ui_widget_NHP


class Widget_NHP(QWidget, Ui_widget_NHP):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Noordhoek Pathfinder - unofficial app')

        # Creating a dynamic filepath system in order to use the app on several pc's:
        self.main_directory = os.getcwd()

        # Creating an instance of QProcess class to trigger scripts:
        self.process = QProcess()

        # NL port docs associated buttons:
        self.nl_crewlist_directory = os.path.join(self.main_directory, r'NHP_apps\nl_ports_crewlist_project')
        self.nl_arrival = os.path.join(self.nl_crewlist_directory, r'vessel-format-crewlist\arrival')
        self.nl_departure = os.path.join(self.nl_crewlist_directory, r'vessel-format-crewlist\departure')
        self.pushButton_freshNL.clicked.connect(self.nl_clear_directories)
        self.pushButton_arrivalNL.clicked.connect(lambda: self.copy_file(self.nl_arrival))
        self.pushButton_departureNL.clicked.connect(lambda: self.copy_file(self.nl_departure))
        self.pushButton_createNL.clicked.connect(self.create_nl_crewlist)
        # self.pushButton_infoNL.clicked.connect(self.info_nl)
        self.pushButton_infoNL.clicked.connect(lambda: self.instruction(self.nl_crewlist_directory))

        # UK port docs associated buttons:
        self.uk_crewlist_directory = os.path.join(self.main_directory, r'NHP_apps\uk_ports_crewlist_project')
        self.pushButton_copyUKcrewlist.clicked.connect(
            lambda: self.copy_file(r"NHP_apps\uk_ports_crewlist_project\current-crewlist"))
        self.pushButton_createUKcrewlist.clicked.connect(self.create_uk_crewlist)
        # self.pushButton_infoUKcrewlist.clicked.connect(self.info_uk)
        self.pushButton_infoUKcrewlist.clicked.connect(lambda: self.instruction(self.uk_crewlist_directory))

        # Resthours associated buttons:
        self.resthours_directory = os.path.join(self.main_directory, r'NHP_apps\resthours')
        self.pushButton_generate_resthours.clicked.connect(self.generate_resthours)
        self.pushButton_info_resthours.clicked.connect(lambda: self.instruction(self.resthours_directory))

        # NTM picker associated buttons:
        self.ntm_picker_directory = os.path.join(self.main_directory, r'NHP_apps\ntm_picker')
        self.pushButton_selectNTM.clicked.connect(
            lambda: self.copy_file(os.path.join(self.ntm_picker_directory, 'current_ntm')))
        self.pushButton_extractNTM.clicked.connect(self.extractNTM)
        self.pushButton_infoNTM.clicked.connect(lambda: self.instruction(self.ntm_picker_directory))

        # Qinsy voyage planning associated buttons:
        self.qinsy_voyage_planning_directory = os.path.join(self.main_directory, r'NHP_apps\qinsy_voyage_planning')
        self.pushButton_selectVP.clicked.connect(
            lambda: self.copy_file(os.path.join(self.qinsy_voyage_planning_directory, 'source_voyage_plan')))
        self.pushButton_createCSV.clicked.connect(self.createQinsyVpCsv)
        self.pushButton_instructionQinsy.clicked.connect(lambda: self.instruction(self.qinsy_voyage_planning_directory))

    def copy_file(self, destination_folder):
        """Function used for selecting vessel format crew lists and moving them to source folders of applications.
        Works both with the NL and UK crew list apps."""
        destination_directory = os.path.join(os.getcwd(), destination_folder)
        shutil.rmtree(destination_directory, ignore_errors=True)
        os.makedirs(destination_directory, exist_ok=True)
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_url, _ = QFileDialog.getOpenFileUrl(self, "Select file to copy", QUrl(),
                                                 "All Files (*);;Excel Files (*.xlsx)", options=options)
        if not file_url.isValid():
            # User cancelled the file selection dialog and aborted the process
            return
        file_path = file_url.toLocalFile()
        shutil.copy(file_path, destination_directory)

    def nl_clear_directories(self):
        arrival_and_departure = [self.nl_arrival, self.nl_departure]
        for directory in arrival_and_departure:
            shutil.rmtree(directory, ignore_errors=True)
            os.makedirs(directory, exist_ok=True)

    def create_nl_crewlist(self):
        """Function triggering the process of creation xlsx file with NL format crewlist including
        both crew arriving and departing the port."""
        # self.process.execute("python", [os.path.join(self.nl_crewlist_directory, 'main.py')])
        self.process.setProperty('directory', os.path.join(self.nl_crewlist_directory, r'ready-document'))
        self.process.start("python", [os.path.join(self.nl_crewlist_directory, 'main.py')])
        self.process.finished.connect(self.when_finished)

    def create_uk_crewlist(self):
        """Function triggering the process of creation docx files with UK format FAL4 & FAL5 forms."""
        self.process.start("python", [os.path.join(self.uk_crewlist_directory, "main.py")])
        self.process.setProperty('directory', os.path.join(self.uk_crewlist_directory, r'ready-documents'))
        self.process.finished.connect(self.when_finished)

    def generate_resthours(self):
        """Function generating sheets with rest hours and agency time sheets for given crew data."""
        resthourst_script_filepath = os.path.join(self.resthours_directory, 'resthours_plus_timesheets.py')
        self.process.setProperty('directory', os.path.join(self.resthours_directory, r'output'))
        self.process.start("python", [resthourst_script_filepath])
        self.process.finished.connect(self.when_finished)

    def extractNTM(self):
        """Function triggering the process of extracting the corrections from provided NTM file and saving them
        into an xlsx file."""
        self.process.setProperty('directory', os.path.join(self.ntm_picker_directory, 'output'))
        self.process.start("python", [os.path.join(self.ntm_picker_directory, 'ntm_picker.py')])
        self.process.finished.connect(self.when_finished)

    def createQinsyVpCsv(self):
        """Function triggering the proces of conversion MS Excel format voyage plan into Qinsy accepted csv file"""
        self.process.setProperty('directory', os.path.join(self.qinsy_voyage_planning_directory, 'csv_voyage_plan'))
        self.process.start("python", [os.path.join(self.qinsy_voyage_planning_directory, 'qinsy_voyage_planning.py')])
        self.process.finished.connect(self.when_finished)

    def instruction(self, directory):
        """ Function displaying an instruction window for each functionality of the app"""
        instruction_filepath = os.path.join(directory, 'instruction.txt')
        with open(instruction_filepath, 'r') as instruction:
            first_line = instruction.readline().strip()
            message_body = instruction.read()
        message = QMessageBox()
        message.setWindowTitle(first_line)
        message.setText(message_body)
        message.setFont(QFont('Times New Roman', 12))
        message.setFixedSize(600, 400)
        message.setStandardButtons(QMessageBox.Ok)
        if 'Resthours' in first_line:
            open_directory_button = message.addButton("Crew data directory", QMessageBox.ActionRole)
            if message.clickedButton() == open_directory_button:
                # Open the directory
                directory = os.path.join(self.resthours_directory, 'crew-data')
                QDesktopServices.openUrl(QUrl.fromLocalFile(directory))
        message.exec_()

    def when_finished(self):
        """Function triggered by "process.finished" signal of each application, opening a Windows Explorer window
        with the directory containing the results generated by the app."""
        if self.process.exitCode() == 0:
            # Display the directory containing results of the app:
            directory = self.sender().property('directory')
            QDesktopServices.openUrl(QUrl.fromLocalFile(directory))
        else:
            # Show an error message
            QMessageBox.critical(self, "Error", f"The process failed. {self.process.exitStatus()},")
