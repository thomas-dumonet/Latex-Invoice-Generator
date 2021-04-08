# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'InvoiceGenerator.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from DraggableTable import QTableWidgetDraggable


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(546, 895)
        Dialog.setMinimumSize(QSize(400, 400))
        self.verticalLayout_7 = QVBoxLayout(Dialog)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.scrollArea_main = QScrollArea(Dialog)
        self.scrollArea_main.setObjectName(u"scrollArea_main")
        self.scrollArea_main.setFrameShape(QFrame.NoFrame)
        self.scrollArea_main.setFrameShadow(QFrame.Plain)
        self.scrollArea_main.setLineWidth(0)
        self.scrollArea_main.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 528, 846))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.groupBox_quickRecall = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_quickRecall.setObjectName(u"groupBox_quickRecall")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_quickRecall)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_quickRecallInvoice = QHBoxLayout()
        self.horizontalLayout_quickRecallInvoice.setObjectName(u"horizontalLayout_quickRecallInvoice")
        self.label_quickRecallInvoice = QLabel(self.groupBox_quickRecall)
        self.label_quickRecallInvoice.setObjectName(u"label_quickRecallInvoice")
        self.label_quickRecallInvoice.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_quickRecallInvoice.addWidget(self.label_quickRecallInvoice)

        self.comboBox_quickRecallInvoice = QComboBox(self.groupBox_quickRecall)
        self.comboBox_quickRecallInvoice.setObjectName(u"comboBox_quickRecallInvoice")

        self.horizontalLayout_quickRecallInvoice.addWidget(self.comboBox_quickRecallInvoice)

        self.pushButton_saveQuickRecallInvoice = QPushButton(self.groupBox_quickRecall)
        self.pushButton_saveQuickRecallInvoice.setObjectName(u"pushButton_saveQuickRecallInvoice")

        self.horizontalLayout_quickRecallInvoice.addWidget(self.pushButton_saveQuickRecallInvoice)

        self.horizontalLayout_quickRecallInvoice.setStretch(1, 1)

        self.verticalLayout_6.addLayout(self.horizontalLayout_quickRecallInvoice)

        self.horizontalLayout_quickRecallGeneral = QHBoxLayout()
        self.horizontalLayout_quickRecallGeneral.setObjectName(u"horizontalLayout_quickRecallGeneral")
        self.label_quickRecallGeneral = QLabel(self.groupBox_quickRecall)
        self.label_quickRecallGeneral.setObjectName(u"label_quickRecallGeneral")
        self.label_quickRecallGeneral.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_quickRecallGeneral.addWidget(self.label_quickRecallGeneral)

        self.comboBox_quickRecallGeneral = QComboBox(self.groupBox_quickRecall)
        self.comboBox_quickRecallGeneral.setObjectName(u"comboBox_quickRecallGeneral")

        self.horizontalLayout_quickRecallGeneral.addWidget(self.comboBox_quickRecallGeneral)

        self.pushButton_saveQuickRecallGeneral = QPushButton(self.groupBox_quickRecall)
        self.pushButton_saveQuickRecallGeneral.setObjectName(u"pushButton_saveQuickRecallGeneral")

        self.horizontalLayout_quickRecallGeneral.addWidget(self.pushButton_saveQuickRecallGeneral)

        self.horizontalLayout_quickRecallGeneral.setStretch(1, 1)

        self.verticalLayout_6.addLayout(self.horizontalLayout_quickRecallGeneral)

        self.horizontalLayout_quickRecallClient = QHBoxLayout()
        self.horizontalLayout_quickRecallClient.setObjectName(u"horizontalLayout_quickRecallClient")
        self.label_quickRecallClient = QLabel(self.groupBox_quickRecall)
        self.label_quickRecallClient.setObjectName(u"label_quickRecallClient")
        self.label_quickRecallClient.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_quickRecallClient.addWidget(self.label_quickRecallClient)

        self.comboBox_quickRecallClient = QComboBox(self.groupBox_quickRecall)
        self.comboBox_quickRecallClient.setObjectName(u"comboBox_quickRecallClient")

        self.horizontalLayout_quickRecallClient.addWidget(self.comboBox_quickRecallClient)

        self.pushButton_saveQuickRecallClient = QPushButton(self.groupBox_quickRecall)
        self.pushButton_saveQuickRecallClient.setObjectName(u"pushButton_saveQuickRecallClient")

        self.horizontalLayout_quickRecallClient.addWidget(self.pushButton_saveQuickRecallClient)

        self.horizontalLayout_quickRecallClient.setStretch(1, 1)

        self.verticalLayout_6.addLayout(self.horizontalLayout_quickRecallClient)


        self.verticalLayout_4.addWidget(self.groupBox_quickRecall)

        self.groupBox_generalInfo = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_generalInfo.setObjectName(u"groupBox_generalInfo")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_generalInfo)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.formLayout_generalInfo = QFormLayout()
        self.formLayout_generalInfo.setObjectName(u"formLayout_generalInfo")
        self.formLayout_generalInfo.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)
        self.label_companyName = QLabel(self.groupBox_generalInfo)
        self.label_companyName.setObjectName(u"label_companyName")

        self.formLayout_generalInfo.setWidget(0, QFormLayout.LabelRole, self.label_companyName)

        self.label_firstName = QLabel(self.groupBox_generalInfo)
        self.label_firstName.setObjectName(u"label_firstName")

        self.formLayout_generalInfo.setWidget(1, QFormLayout.LabelRole, self.label_firstName)

        self.label_lastName = QLabel(self.groupBox_generalInfo)
        self.label_lastName.setObjectName(u"label_lastName")

        self.formLayout_generalInfo.setWidget(2, QFormLayout.LabelRole, self.label_lastName)

        self.lineEdit_companyName = QLineEdit(self.groupBox_generalInfo)
        self.lineEdit_companyName.setObjectName(u"lineEdit_companyName")

        self.formLayout_generalInfo.setWidget(0, QFormLayout.FieldRole, self.lineEdit_companyName)

        self.lineEdit_firstName = QLineEdit(self.groupBox_generalInfo)
        self.lineEdit_firstName.setObjectName(u"lineEdit_firstName")

        self.formLayout_generalInfo.setWidget(1, QFormLayout.FieldRole, self.lineEdit_firstName)

        self.lineEdit_lastName = QLineEdit(self.groupBox_generalInfo)
        self.lineEdit_lastName.setObjectName(u"lineEdit_lastName")

        self.formLayout_generalInfo.setWidget(2, QFormLayout.FieldRole, self.lineEdit_lastName)

        self.label_fullAdress = QLabel(self.groupBox_generalInfo)
        self.label_fullAdress.setObjectName(u"label_fullAdress")

        self.formLayout_generalInfo.setWidget(3, QFormLayout.LabelRole, self.label_fullAdress)

        self.label_companySIRET = QLabel(self.groupBox_generalInfo)
        self.label_companySIRET.setObjectName(u"label_companySIRET")

        self.formLayout_generalInfo.setWidget(4, QFormLayout.LabelRole, self.label_companySIRET)

        self.label_companySIREN = QLabel(self.groupBox_generalInfo)
        self.label_companySIREN.setObjectName(u"label_companySIREN")

        self.formLayout_generalInfo.setWidget(5, QFormLayout.LabelRole, self.label_companySIREN)

        self.label_companyTelephon = QLabel(self.groupBox_generalInfo)
        self.label_companyTelephon.setObjectName(u"label_companyTelephon")
        self.label_companyTelephon.setMinimumSize(QSize(0, 0))

        self.formLayout_generalInfo.setWidget(8, QFormLayout.LabelRole, self.label_companyTelephon)

        self.label_bankIBAN = QLabel(self.groupBox_generalInfo)
        self.label_bankIBAN.setObjectName(u"label_bankIBAN")

        self.formLayout_generalInfo.setWidget(9, QFormLayout.LabelRole, self.label_bankIBAN)

        self.label_bankBIC = QLabel(self.groupBox_generalInfo)
        self.label_bankBIC.setObjectName(u"label_bankBIC")
        self.label_bankBIC.setMinimumSize(QSize(100, 0))

        self.formLayout_generalInfo.setWidget(10, QFormLayout.LabelRole, self.label_bankBIC)

        self.lineEdit_fullAddress = QLineEdit(self.groupBox_generalInfo)
        self.lineEdit_fullAddress.setObjectName(u"lineEdit_fullAddress")

        self.formLayout_generalInfo.setWidget(3, QFormLayout.FieldRole, self.lineEdit_fullAddress)

        self.lineEdit_companySIRET = QLineEdit(self.groupBox_generalInfo)
        self.lineEdit_companySIRET.setObjectName(u"lineEdit_companySIRET")

        self.formLayout_generalInfo.setWidget(4, QFormLayout.FieldRole, self.lineEdit_companySIRET)

        self.lineEdit_companySIREN = QLineEdit(self.groupBox_generalInfo)
        self.lineEdit_companySIREN.setObjectName(u"lineEdit_companySIREN")

        self.formLayout_generalInfo.setWidget(5, QFormLayout.FieldRole, self.lineEdit_companySIREN)

        self.lineEdit_companyTelephone = QLineEdit(self.groupBox_generalInfo)
        self.lineEdit_companyTelephone.setObjectName(u"lineEdit_companyTelephone")

        self.formLayout_generalInfo.setWidget(8, QFormLayout.FieldRole, self.lineEdit_companyTelephone)

        self.lineEdit_bankIBAN = QLineEdit(self.groupBox_generalInfo)
        self.lineEdit_bankIBAN.setObjectName(u"lineEdit_bankIBAN")

        self.formLayout_generalInfo.setWidget(9, QFormLayout.FieldRole, self.lineEdit_bankIBAN)

        self.lineEdit_bankBIC = QLineEdit(self.groupBox_generalInfo)
        self.lineEdit_bankBIC.setObjectName(u"lineEdit_bankBIC")

        self.formLayout_generalInfo.setWidget(10, QFormLayout.FieldRole, self.lineEdit_bankBIC)

        self.label_companyEmail = QLabel(self.groupBox_generalInfo)
        self.label_companyEmail.setObjectName(u"label_companyEmail")

        self.formLayout_generalInfo.setWidget(7, QFormLayout.LabelRole, self.label_companyEmail)

        self.lineEdit_companyEmail = QLineEdit(self.groupBox_generalInfo)
        self.lineEdit_companyEmail.setObjectName(u"lineEdit_companyEmail")

        self.formLayout_generalInfo.setWidget(7, QFormLayout.FieldRole, self.lineEdit_companyEmail)

        self.label_companyAPE = QLabel(self.groupBox_generalInfo)
        self.label_companyAPE.setObjectName(u"label_companyAPE")

        self.formLayout_generalInfo.setWidget(6, QFormLayout.LabelRole, self.label_companyAPE)

        self.lineEdit_companyAPE = QLineEdit(self.groupBox_generalInfo)
        self.lineEdit_companyAPE.setObjectName(u"lineEdit_companyAPE")

        self.formLayout_generalInfo.setWidget(6, QFormLayout.FieldRole, self.lineEdit_companyAPE)


        self.verticalLayout_2.addLayout(self.formLayout_generalInfo)


        self.verticalLayout_4.addWidget(self.groupBox_generalInfo)

        self.groupBox_clientInfo = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_clientInfo.setObjectName(u"groupBox_clientInfo")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_clientInfo)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.formLayout_clientInfo = QFormLayout()
        self.formLayout_clientInfo.setObjectName(u"formLayout_clientInfo")
        self.label_clientName = QLabel(self.groupBox_clientInfo)
        self.label_clientName.setObjectName(u"label_clientName")

        self.formLayout_clientInfo.setWidget(0, QFormLayout.LabelRole, self.label_clientName)

        self.label_clientAddressfirst = QLabel(self.groupBox_clientInfo)
        self.label_clientAddressfirst.setObjectName(u"label_clientAddressfirst")
        self.label_clientAddressfirst.setMinimumSize(QSize(100, 0))

        self.formLayout_clientInfo.setWidget(1, QFormLayout.LabelRole, self.label_clientAddressfirst)

        self.label_clientAdressSecond = QLabel(self.groupBox_clientInfo)
        self.label_clientAdressSecond.setObjectName(u"label_clientAdressSecond")

        self.formLayout_clientInfo.setWidget(2, QFormLayout.LabelRole, self.label_clientAdressSecond)

        self.lineEdit_clientName = QLineEdit(self.groupBox_clientInfo)
        self.lineEdit_clientName.setObjectName(u"lineEdit_clientName")

        self.formLayout_clientInfo.setWidget(0, QFormLayout.FieldRole, self.lineEdit_clientName)

        self.lineEdit_clientAddressFirst = QLineEdit(self.groupBox_clientInfo)
        self.lineEdit_clientAddressFirst.setObjectName(u"lineEdit_clientAddressFirst")

        self.formLayout_clientInfo.setWidget(1, QFormLayout.FieldRole, self.lineEdit_clientAddressFirst)

        self.lineEdit_clientAdressSecond = QLineEdit(self.groupBox_clientInfo)
        self.lineEdit_clientAdressSecond.setObjectName(u"lineEdit_clientAdressSecond")

        self.formLayout_clientInfo.setWidget(2, QFormLayout.FieldRole, self.lineEdit_clientAdressSecond)


        self.verticalLayout_3.addLayout(self.formLayout_clientInfo)


        self.verticalLayout_4.addWidget(self.groupBox_clientInfo)

        self.groupBox_invoiceInfo = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_invoiceInfo.setObjectName(u"groupBox_invoiceInfo")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_invoiceInfo)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.formLayout_invoiceInfo = QFormLayout()
        self.formLayout_invoiceInfo.setObjectName(u"formLayout_invoiceInfo")
        self.label_invoiceNumber = QLabel(self.groupBox_invoiceInfo)
        self.label_invoiceNumber.setObjectName(u"label_invoiceNumber")

        self.formLayout_invoiceInfo.setWidget(0, QFormLayout.LabelRole, self.label_invoiceNumber)

        self.lineEdit_invoiceNumber = QLineEdit(self.groupBox_invoiceInfo)
        self.lineEdit_invoiceNumber.setObjectName(u"lineEdit_invoiceNumber")

        self.formLayout_invoiceInfo.setWidget(0, QFormLayout.FieldRole, self.lineEdit_invoiceNumber)

        self.label_invoiceDate = QLabel(self.groupBox_invoiceInfo)
        self.label_invoiceDate.setObjectName(u"label_invoiceDate")
        self.label_invoiceDate.setMinimumSize(QSize(100, 0))

        self.formLayout_invoiceInfo.setWidget(1, QFormLayout.LabelRole, self.label_invoiceDate)

        self.lineEdit_invoiceDate = QLineEdit(self.groupBox_invoiceInfo)
        self.lineEdit_invoiceDate.setObjectName(u"lineEdit_invoiceDate")

        self.formLayout_invoiceInfo.setWidget(1, QFormLayout.FieldRole, self.lineEdit_invoiceDate)

        self.label_invoiceName = QLabel(self.groupBox_invoiceInfo)
        self.label_invoiceName.setObjectName(u"label_invoiceName")

        self.formLayout_invoiceInfo.setWidget(2, QFormLayout.LabelRole, self.label_invoiceName)

        self.lineEdit_invoiceName = QLineEdit(self.groupBox_invoiceInfo)
        self.lineEdit_invoiceName.setObjectName(u"lineEdit_invoiceName")

        self.formLayout_invoiceInfo.setWidget(2, QFormLayout.FieldRole, self.lineEdit_invoiceName)


        self.verticalLayout_5.addLayout(self.formLayout_invoiceInfo)


        self.verticalLayout_4.addWidget(self.groupBox_invoiceInfo)

        self.groupBox_invoiceContent = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_invoiceContent.setObjectName(u"groupBox_invoiceContent")
        self.verticalLayout = QVBoxLayout(self.groupBox_invoiceContent)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tableWidget_invoiceContent = QTableWidgetDraggable(self.groupBox_invoiceContent)
        if (self.tableWidget_invoiceContent.columnCount() < 3):
            self.tableWidget_invoiceContent.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_invoiceContent.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_invoiceContent.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_invoiceContent.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget_invoiceContent.setObjectName(u"tableWidget_invoiceContent")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_invoiceContent.sizePolicy().hasHeightForWidth())
        self.tableWidget_invoiceContent.setSizePolicy(sizePolicy)
        self.tableWidget_invoiceContent.setAutoFillBackground(False)

        self.verticalLayout.addWidget(self.tableWidget_invoiceContent)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.toolButton_add = QToolButton(self.groupBox_invoiceContent)
        self.toolButton_add.setObjectName(u"toolButton_add")
        self.toolButton_add.setMinimumSize(QSize(42, 0))

        self.horizontalLayout.addWidget(self.toolButton_add)

        self.toolButton_delete = QToolButton(self.groupBox_invoiceContent)
        self.toolButton_delete.setObjectName(u"toolButton_delete")
        self.toolButton_delete.setMinimumSize(QSize(42, 0))

        self.horizontalLayout.addWidget(self.toolButton_delete)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_4.addWidget(self.groupBox_invoiceContent)

        self.scrollArea_main.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_7.addWidget(self.scrollArea_main)

        self.horizontalLayout_invoice = QHBoxLayout()
        self.horizontalLayout_invoice.setObjectName(u"horizontalLayout_invoice")
        self.horizontalLayout_invoice.setContentsMargins(9, -1, 9, -1)
        self.progressBar = QProgressBar(Dialog)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setEnabled(False)
        self.progressBar.setMaximum(1)
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setInvertedAppearance(False)

        self.horizontalLayout_invoice.addWidget(self.progressBar)

        self.pushButton_generateInvoice = QPushButton(Dialog)
        self.pushButton_generateInvoice.setObjectName(u"pushButton_generateInvoice")

        self.horizontalLayout_invoice.addWidget(self.pushButton_generateInvoice)


        self.verticalLayout_7.addLayout(self.horizontalLayout_invoice)

        QWidget.setTabOrder(self.scrollArea_main, self.comboBox_quickRecallInvoice)
        QWidget.setTabOrder(self.comboBox_quickRecallInvoice, self.pushButton_saveQuickRecallInvoice)
        QWidget.setTabOrder(self.pushButton_saveQuickRecallInvoice, self.comboBox_quickRecallGeneral)
        QWidget.setTabOrder(self.comboBox_quickRecallGeneral, self.pushButton_saveQuickRecallGeneral)
        QWidget.setTabOrder(self.pushButton_saveQuickRecallGeneral, self.comboBox_quickRecallClient)
        QWidget.setTabOrder(self.comboBox_quickRecallClient, self.pushButton_saveQuickRecallClient)
        QWidget.setTabOrder(self.pushButton_saveQuickRecallClient, self.lineEdit_companyName)
        QWidget.setTabOrder(self.lineEdit_companyName, self.lineEdit_firstName)
        QWidget.setTabOrder(self.lineEdit_firstName, self.lineEdit_lastName)
        QWidget.setTabOrder(self.lineEdit_lastName, self.lineEdit_fullAddress)
        QWidget.setTabOrder(self.lineEdit_fullAddress, self.lineEdit_companySIRET)
        QWidget.setTabOrder(self.lineEdit_companySIRET, self.lineEdit_companySIREN)
        QWidget.setTabOrder(self.lineEdit_companySIREN, self.lineEdit_companyAPE)
        QWidget.setTabOrder(self.lineEdit_companyAPE, self.lineEdit_companyEmail)
        QWidget.setTabOrder(self.lineEdit_companyEmail, self.lineEdit_companyTelephone)
        QWidget.setTabOrder(self.lineEdit_companyTelephone, self.lineEdit_bankIBAN)
        QWidget.setTabOrder(self.lineEdit_bankIBAN, self.lineEdit_bankBIC)
        QWidget.setTabOrder(self.lineEdit_bankBIC, self.lineEdit_clientName)
        QWidget.setTabOrder(self.lineEdit_clientName, self.lineEdit_clientAddressFirst)
        QWidget.setTabOrder(self.lineEdit_clientAddressFirst, self.lineEdit_clientAdressSecond)
        QWidget.setTabOrder(self.lineEdit_clientAdressSecond, self.lineEdit_invoiceNumber)
        QWidget.setTabOrder(self.lineEdit_invoiceNumber, self.lineEdit_invoiceDate)
        QWidget.setTabOrder(self.lineEdit_invoiceDate, self.lineEdit_invoiceName)
        QWidget.setTabOrder(self.lineEdit_invoiceName, self.tableWidget_invoiceContent)
        QWidget.setTabOrder(self.tableWidget_invoiceContent, self.toolButton_add)
        QWidget.setTabOrder(self.toolButton_add, self.toolButton_delete)
        QWidget.setTabOrder(self.toolButton_delete, self.pushButton_generateInvoice)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.groupBox_quickRecall.setTitle(QCoreApplication.translate("Dialog", u"Quick Recall", None))
        self.label_quickRecallInvoice.setText(QCoreApplication.translate("Dialog", u"Invoice", None))
        self.pushButton_saveQuickRecallInvoice.setText(QCoreApplication.translate("Dialog", u"Save Current", None))
        self.label_quickRecallGeneral.setText(QCoreApplication.translate("Dialog", u"General", None))
        self.pushButton_saveQuickRecallGeneral.setText(QCoreApplication.translate("Dialog", u"Save Current", None))
        self.label_quickRecallClient.setText(QCoreApplication.translate("Dialog", u"Client", None))
        self.pushButton_saveQuickRecallClient.setText(QCoreApplication.translate("Dialog", u"Save Current", None))
        self.groupBox_generalInfo.setTitle(QCoreApplication.translate("Dialog", u"General Info", None))
        self.label_companyName.setText(QCoreApplication.translate("Dialog", u"Company Name", None))
        self.label_firstName.setText(QCoreApplication.translate("Dialog", u"First Name", None))
        self.label_lastName.setText(QCoreApplication.translate("Dialog", u"Last Name", None))
        self.label_fullAdress.setText(QCoreApplication.translate("Dialog", u"Full Address", None))
        self.label_companySIRET.setText(QCoreApplication.translate("Dialog", u"Company SIRET", None))
        self.label_companySIREN.setText(QCoreApplication.translate("Dialog", u"Company SIREN", None))
        self.label_companyTelephon.setText(QCoreApplication.translate("Dialog", u"Company telephone", None))
        self.label_bankIBAN.setText(QCoreApplication.translate("Dialog", u"bank IBAN", None))
        self.label_bankBIC.setText(QCoreApplication.translate("Dialog", u"bank BIC", None))
        self.label_companyEmail.setText(QCoreApplication.translate("Dialog", u"Company Email", None))
        self.label_companyAPE.setText(QCoreApplication.translate("Dialog", u"Company APE", None))
        self.groupBox_clientInfo.setTitle(QCoreApplication.translate("Dialog", u"Client Info", None))
        self.label_clientName.setText(QCoreApplication.translate("Dialog", u"Name", None))
        self.label_clientAddressfirst.setText(QCoreApplication.translate("Dialog", u"Address First Line", None))
        self.label_clientAdressSecond.setText(QCoreApplication.translate("Dialog", u"Address Second Line", None))
        self.groupBox_invoiceInfo.setTitle(QCoreApplication.translate("Dialog", u"Invoice Info", None))
        self.label_invoiceNumber.setText(QCoreApplication.translate("Dialog", u"Invoice Number", None))
        self.label_invoiceDate.setText(QCoreApplication.translate("Dialog", u"Invoice Date", None))
        self.label_invoiceName.setText(QCoreApplication.translate("Dialog", u"Invoice Name", None))
        self.groupBox_invoiceContent.setTitle(QCoreApplication.translate("Dialog", u"Invoice Content", None))
        ___qtablewidgetitem = self.tableWidget_invoiceContent.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"Product", None));
        ___qtablewidgetitem1 = self.tableWidget_invoiceContent.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"Quantity", None));
        ___qtablewidgetitem2 = self.tableWidget_invoiceContent.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"Price", None));
        self.toolButton_add.setText(QCoreApplication.translate("Dialog", u"+", None))
        self.toolButton_delete.setText(QCoreApplication.translate("Dialog", u"-", None))
        self.pushButton_generateInvoice.setText(QCoreApplication.translate("Dialog", u"Generate Invoice", None))
    # retranslateUi

