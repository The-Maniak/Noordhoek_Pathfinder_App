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
        self.pushButton_arrivalNL.clicked.connect(lambda: self.copy_crewlist(self.nl_arrival))
        self.pushButton_departureNL.clicked.connect(lambda: self.copy_crewlist(self.nl_departure))
        self.pushButton_createNL.clicked.connect(self.create_nl_crewlist)
        self.pushButton_infoNL.clicked.connect(self.info_nl)

        # UK port docs associated buttons:
        self.uk_crewlist_directory = os.path.join(self.main_directory, r'NHP_apps\uk_ports_crewlist_project')
        self.pushButton_copyUKcrewlist.clicked.connect(
            lambda: self.copy_crewlist(r"NHP_apps\uk_ports_crewlist_project\current-crewlist"))
        self.pushButton_createUKcrewlist.clicked.connect(self.create_uk_crewlist)
        self.pushButton_infoUKcrewlist.clicked.connect(self.info_uk)

        # Resthours associated buttons:
        self.resthours_directory = os.path.join(self.main_directory, r'NHP_apps\resthours')
        self.pushButton_generate_resthours.clicked.connect(self.generate_resthours)
        self.pushButton_info_resthours.clicked.connect(self.info_resthours)

    def copy_crewlist(self, destination_folder):
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
            print(f'removing {directory}')
            shutil.rmtree(directory, ignore_errors=True)
            print(f'creating {directory}')
            os.makedirs(directory, exist_ok=True)

    def create_nl_crewlist(self):
        """Function triggering the process of creation xlsx file with NL format crewlist including
        both crew arriving and departing the port."""
        # self.process.execute("python", [os.path.join(self.nl_crewlist_directory, 'main.py')])
        self.process.setProperty('directory', os.path.join(self.nl_crewlist_directory, r'ready-document'))
        self.process.start("python", [os.path.join(self.nl_crewlist_directory, 'main.py')])
        self.process.finished.connect(self.when_finished)

    def info_nl(self):
        """ Function displaying an instruction window for NL crew list"""
        instruction_filepath = os.path.join(self.nl_crewlist_directory, 'instruction_nl.txt')
        with open(instruction_filepath, 'r') as instruction_file:
            instruction_nl = instruction_file.read()
        message = QMessageBox()
        message.setWindowTitle("NL format crewlist - manual")
        message.setText(instruction_nl)
        message.setFont(QFont('Times New Roman', 12))
        message.setFixedSize(600, 400)
        message.exec_()

    def create_uk_crewlist(self):
        """Function triggering the process of creation docx files with UK format FAL4 & FAL5 forms."""
        self.process.start("python", [os.path.join(self.uk_crewlist_directory, "main.py")])
        self.process.setProperty('directory', os.path.join(self.uk_crewlist_directory, r'ready-documents'))
        self.process.finished.connect(self.when_finished)

    def info_uk(self):
        """ Function displaying an instruction window for UK crew list"""
        instruction_filepath = os.path.join(self.uk_crewlist_directory, 'instruction_uk.txt')
        with open(instruction_filepath, 'r') as instruction_uk:
            instruction_uk = instruction_uk.read()
        message = QMessageBox()
        message.setWindowTitle("UK format crewlist - manual")
        message.setText(instruction_uk)
        message.setFont(QFont('Times New Roman', 12))
        message.setFixedSize(600, 400)
        message.exec_()

    def generate_resthours(self):
        """Function generating sheets with rest hours and agency time sheets for given crew data."""
        resthourst_script_filepath = os.path.join(self.resthours_directory, 'resthours_plus_timesheets.py')
        self.process.setProperty('directory', os.path.join(self.resthours_directory, r'output'))
        self.process.start("python", [resthourst_script_filepath])
        self.process.finished.connect(self.when_finished)

    def info_resthours(self):
        """ Function displaying an instruction window for generating rest hours and agency time sheets"""
        instruction_filepath = os.path.join(self.resthours_directory, 'instruction_resthours.txt')
        with open(instruction_filepath, 'r') as file:
            instruction_resthours = file.read()
        message = QMessageBox()
        message.setWindowTitle("Resthours and timesheets - manual")
        message.setText(instruction_resthours)
        message.setFont(QFont('Times New Roman', 12))
        message.setFixedSize(600, 400)
        message.setStandardButtons(QMessageBox.Ok)
        open_directory_button = message.addButton("Crew data directory", QMessageBox.ActionRole)
        message.exec_()

        if message.clickedButton() == open_directory_button:
            # Open the directory
            directory = os.path.join(self.resthours_directory, 'crew-data')
            QDesktopServices.openUrl(QUrl.fromLocalFile(directory))

    def when_finished(self):
        """Function triggered by "process.finished" signal of each application, opening a Windows Explorer window
        with the directory containing the results generated by the app."""
        if self.process.exitCode() == 0:
            # Display the directory containing results of the app:
            directory = self.sender().property('directory')
            QDesktopServices.openUrl(QUrl.fromLocalFile(directory))
        else:
            # Show an error message
            QMessageBox.critical(self, "Error", "The process failed.")
