from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication,QMainWindow,QFileDialog,QMessageBox
from panel import Ui_Form
import sys,csv
import qdarkstyle

class MyMainWindow(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.files=[]
        self.file=''
        self.signal=0    #the flag to decide which operation to do
        self.button1.clicked.connect(self.single_file)
        self.button2.clicked.connect(self.multiple_file)
        self.button3.clicked.connect(self.extract)

    #Choose the single file
    def single_file(self):
        self.signal=1
        self.file, filetype = QFileDialog.getOpenFileName(self,
                      "选取文件",
                      "./",
                      "Exce(*.csv)")  #设置文件扩展名过滤,注意用双分号间隔
        self.textBrowser_3.append(self.file)
    #Choose the multiple files
    def multiple_file(self):
        self.signal=2
        self.files, files_type = QFileDialog.getOpenFileNames(self,
              "Choose multiple files",
              "./",
              "Exce(*.csv)")
        for i in self.files:
           self.textBrowser_3.append(i)


    #Execute the extraction operation
    def extract(self):
      if self.files==[] and self.file=='':
        QMessageBox.about(self, "Alert", "You should choose file firstly and then extract information from it !!!")
      else:
          #single file operation
          if self.signal==1:
              keyword=self.lineEdit_2.text()
              with open(self.file,'r') as f:
                 reader = csv.reader(f)
                 head_row=next(reader)

                 if (keyword not in head_row):
                    self.textBrowser_2.append(self.file+' doesn\'t have this keyword!!!')
                    QMessageBox.about(self, "Alert", "The file you selected doesn't have this keyword,please modify it and then extract !!!")
                    
                 else:
                    column_num=head_row.index(keyword)
                    rows=[row[column_num] for row in reader]
                    with open('extract.txt','a+') as txt:
                         for i in rows:
                            txt.write(i+"\n")
                    self.textBrowser_2.append("extract.txt is created successfully.")
                    QMessageBox.about(self, "Success", "Your operation is successfully executed,the extracted information is created.")


          #multiple files operation
          elif self.signal==2:
              keyword=self.lineEdit_2.text()
              self.file_count=0
              for selected_file in self.files:
                self.file_count+=1
                with open(selected_file,'r') as f:
                     reader = csv.reader(f)
                     head_row=next(reader)

                     if (keyword not in head_row):
                        self.textBrowser_2.append(selected_file+' doesn\'t have this keyword!!!')
                        QMessageBox.about(self, "Alert", "The file you selected doesn't have this keyword,please modify it and then extract !!!")
                        break
                     else:
                         column_num=head_row.index(keyword)
                         rows=[row[column_num] for row in reader]
                         file_name="extract_"+str(self.file_count)+".txt"
                         with open(file_name,'a+') as txt:
                             for i in rows:
                                txt.write(i+"\n")
                         self.textBrowser_2.append(file_name+" is created successfully.")
                QMessageBox.about(self, "Success", "Your operation is successfully executed,the extracted information is created.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./pic/extract.png"))
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())