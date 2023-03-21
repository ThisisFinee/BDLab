import glob

from PyQt5 import QtCore, QtGui, QtWidgets
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 576)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 801, 221))
        self.frame.setStyleSheet("background-color: rgb(255, 60, 60)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 25, 501, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white")
        self.label.setObjectName("label")
        self.line_surname = QtWidgets.QLineEdit(self.frame)
        self.line_surname.setGeometry(QtCore.QRect(250, 80, 221, 31))
        self.line_surname.setStyleSheet("background-color: #22222e;\n"
                                        "border-top-left-radius: 10px;\n"
                                        "border-top-right-radius: 10px;\n"
                                        "border-bottom-left-radius: 10px;\n"
                                        "border-bottom-right-radius: 10px;\n"
                                        "color: white;")
        self.line_surname.setObjectName("line_surname")
        self.line_patronomyc = QtWidgets.QLineEdit(self.frame)
        self.line_patronomyc.setGeometry(QtCore.QRect(480, 80, 221, 31))
        self.line_patronomyc.setStyleSheet("background-color: #22222e;\n"
                                           "border-top-left-radius: 10px;\n"
                                           "border-top-right-radius: 10px;\n"
                                           "border-bottom-left-radius: 10px;\n"
                                           "border-bottom-right-radius: 10px;\n"
                                           "color: white;")
        self.line_patronomyc.setObjectName("line_patronomyc")
        self.line_name = QtWidgets.QLineEdit(self.frame)
        self.line_name.setGeometry(QtCore.QRect(20, 80, 221, 31))
        self.line_name.setStyleSheet("background-color: #22222e;\n"
                                     "border-top-left-radius: 10px;\n"
                                     "border-top-right-radius: 10px;\n"
                                     "border-bottom-left-radius: 10px;\n"
                                     "border-bottom-right-radius: 10px;\n"
                                     "color: white;")
        self.line_name.setObjectName("line_name")
        self.Button_add = QtWidgets.QPushButton(self.frame)
        self.Button_add.setGeometry(QtCore.QRect(710, 80, 71, 31))
        self.Button_add.setStyleSheet("color:white;\n"
                                      "border-top-left-radius: 15px;\n"
                                      "border-top-right-radius: 15px;\n"
                                      "border-bottom-left-radius: 15px;\n"
                                      "border-bottom-right-radius: 15px;\n"
                                      "background-color: green;")
        self.Button_add.setObjectName("Button_add")
        self.Select_button = QtWidgets.QPushButton(self.frame)
        self.Select_button.setGeometry(QtCore.QRect(350, 120, 131, 28))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Select_button.setFont(font)
        self.Select_button.setStyleSheet("color:white;\n"
                                         "border-top-left-radius: 14px;\n"
                                         "border-top-right-radius: 14px;\n"
                                         "border-bottom-left-radius: 14px;\n"
                                         "border-bottom-right-radius: 14px;\n"
                                         "background-color: rgb(255, 170, 0);")
        self.Select_button.setObjectName("Select_button")
        self.Create_file_button = QtWidgets.QPushButton(self.frame)
        self.Create_file_button.setGeometry(QtCore.QRect(600, 120, 181, 28))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Create_file_button.setFont(font)
        self.Create_file_button.setStyleSheet("color:white;\n"
                                              "border-top-left-radius: 14px;\n"
                                              "border-top-right-radius: 14px;\n"
                                              "border-bottom-left-radius: 14px;\n"
                                              "border-bottom-right-radius: 14px;\n"
                                              "background-color: rgb(255, 170, 0);")
        self.Create_file_button.setObjectName("Create_file_button")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(20, 130, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: white;")
        self.label_2.setObjectName("label_2")
        self.file_box = QtWidgets.QComboBox(self.frame)
        self.file_box.setGeometry(QtCore.QRect(160, 130, 181, 21))
        self.file_box.setStyleSheet("border-top-left-radius: 10px;\n"
                                    "border-bottom-left-radius: 10px;\n"
                                    "background-color: grey;\n"
                                    "color: white;")
        self.file_box.setObjectName("file_box")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(20, 170, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: white;")
        self.label_3.setObjectName("label_3")
        self.Id_Line = QtWidgets.QLineEdit(self.frame)
        self.Id_Line.setGeometry(QtCore.QRect(110, 170, 201, 31))
        self.Id_Line.setStyleSheet("background-color: #22222e;\n"
                                   "border-top-left-radius: 10px;\n"
                                   "border-top-right-radius: 10px;\n"
                                   "border-bottom-left-radius: 10px;\n"
                                   "border-bottom-right-radius: 10px;\n"
                                   "color: white;")
        self.Id_Line.setText("")
        self.Id_Line.setObjectName("Id_Line")
        self.Button_delete = QtWidgets.QPushButton(self.frame)
        self.Button_delete.setGeometry(QtCore.QRect(320, 170, 131, 28))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Button_delete.setFont(font)
        self.Button_delete.setStyleSheet("color:white;\n"
                                         "border-top-left-radius: 14px;\n"
                                         "border-top-right-radius: 14px;\n"
                                         "border-bottom-left-radius: 14px;\n"
                                         "border-bottom-right-radius: 14px;\n"
                                         "background-color:rgb(255, 85, 255);")
        self.Button_delete.setObjectName("Button_delete")
        self.Change_button = QtWidgets.QPushButton(self.frame)
        self.Change_button.setGeometry(QtCore.QRect(460, 170, 131, 28))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Change_button.setFont(font)
        self.Change_button.setStyleSheet("color:white;\n"
                                         "border-top-left-radius: 14px;\n"
                                         "border-top-right-radius: 14px;\n"
                                         "border-bottom-left-radius: 14px;\n"
                                         "border-bottom-right-radius: 14px;\n"
                                         "background-color:rgb(255, 85, 255);")
        self.Change_button.setObjectName("Change_button")
        self.label_id = QtWidgets.QLabel(self.frame)
        self.label_id.setGeometry(QtCore.QRect(520, 30, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_id.setFont(font)
        self.label_id.setStyleSheet("color: white")
        self.label_id.setText("")
        self.label_id.setObjectName("label_id")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 220, 801, 361))
        self.frame_2.setStyleSheet("background-color: rgb(255, 85, 127)")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.Student_id_list = QtWidgets.QListView(self.frame_2)
        self.Student_id_list.setGeometry(QtCore.QRect(10, 10, 581, 341))
        self.Student_id_list.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.Student_id_list.setObjectName("Student_id_list")
        self.Button_step_back = QtWidgets.QPushButton(self.frame_2)
        self.Button_step_back.setGeometry(QtCore.QRect(600, 7, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Button_step_back.setFont(font)
        self.Button_step_back.setStyleSheet("color:white;\n"
                                            "border-top-left-radius: 14px;\n"
                                            "border-top-right-radius: 14px;\n"
                                            "border-bottom-left-radius: 14px;\n"
                                            "border-bottom-right-radius: 14px;\n"
                                            "background-color:rgb(255, 170, 0);")
        self.Button_step_back.setObjectName("Button_step_back")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(610, 60, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: white;")
        self.label_4.setObjectName("label_4")
        self.spinBox = QtWidgets.QSpinBox(self.frame_2)
        self.spinBox.setGeometry(QtCore.QRect(610, 100, 51, 31))
        self.spinBox.setStyleSheet("background-color: grey;\n"
                                   "color:white;")
        self.spinBox.setObjectName("spinBox")
        self.Button_generate_table = QtWidgets.QPushButton(self.frame_2)
        self.Button_generate_table.setGeometry(QtCore.QRect(670, 100, 121, 31))
        self.Button_generate_table.setStyleSheet("color:white;\n"
                                                 "border-top-left-radius: 15px;\n"
                                                 "border-top-right-radius: 15px;\n"
                                                 "border-bottom-left-radius: 15px;\n"
                                                 "border-bottom-right-radius: 15px;\n"
                                                 "background-color: green;")
        self.Button_generate_table.setObjectName("Button_generate_table")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(600, 140, 191, 211))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("C:/Users/totoh/PycharmProjects/BdLaB/kot.jpg"))
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "This is the base"))
        self.line_name.setPlaceholderText("Name")
        self.line_surname.setPlaceholderText("Surname")
        self.line_patronomyc.setPlaceholderText("Patronymic")
        self.label.setText(_translate("MainWindow", "The added student will be assigned an id:"))
        self.Button_add.setText(_translate("MainWindow", "ADD"))
        self.Select_button.setText(_translate("MainWindow", "Select"))
        self.Create_file_button.setText(_translate("MainWindow", "Create new file"))
        self.label_2.setText(_translate("MainWindow", "Select a file:"))
        self.label_3.setText(_translate("MainWindow", "Enter id:"))
        self.Button_delete.setText(_translate("MainWindow", "Delete"))
        self.Change_button.setText(_translate("MainWindow", "Change"))
        self.Button_step_back.setText(_translate("MainWindow", "Step back"))
        self.label_4.setText(_translate("MainWindow", "Number of variants:"))
        self.Button_generate_table.setText(_translate("MainWindow", "Generate table"))


    def directoryexist(self, m1_path, string):
        m1_path += string
        if os.path.exists(m1_path):
            return True
        else:
            os.mkdir(m1_path)
            return True


    def MainDirectoryExists(self):
        main_path = os.getcwd()
        main_path += "/Students"
        if os.path.exists(main_path):
            direct = ["/students_table", "/Back", "/Generated1", "/Generated2", "/var"]
            for i in direct:
                self.directoryexist(main_path, i)
        else:
            os.mkdir(main_path)
            self.MainDirectoryExists()
        return main_path


    def FullFillFiles(self):
        self.file_box.clear()
        main_path = self.MainDirectoryExists()
        main1_path = main_path
        main1_path += "/students_table"
        os.chdir(main1_path)
        for file in glob.glob("*.txt"):
            name = f"/{file}"
            file_name = os.path.basename(main1_path+name)
            self.file_box.addItem(file_name)
            directory = ["/Generated2", "/Generated1", "/Back"]
            for i in directory:
                if os.path.isfile(main_path+i+name) is False:
                    f = open(main_path+i+name, "w")





