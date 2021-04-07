# -*- coding: utf-8 -*-
import sys
import copy
import json
from SaveData import SaveData, GeneralInfo, ClientInfo, InvoiceInfo, InvoiceItem
from TexGenerator import LatexTemplateGenerator
from invoiceUI import Ui_Dialog
from PySide2.QtWidgets import (QApplication, QMessageBox, QTableWidgetItem,
                               QDialog, QHeaderView, QMenu, QAction)

from PySide2 import QtGui


class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.tableWidget_invoiceContent.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)

        self.saveData = SaveData('data/save.json')
        self.texGenerator = LatexTemplateGenerator()

        self.currentGeneralInfo = GeneralInfo()
        self.currentClientInfo = ClientInfo()
        self.currentInvoiceInfo = InvoiceInfo()

        self.ui.pushButton_saveQuickRecallInvoice.clicked.connect(self.save_invoice_info)
        self.ui.pushButton_saveQuickRecallClient.clicked.connect(self.save_client_info)
        self.ui.pushButton_saveQuickRecallGeneral.clicked.connect(self.save_general_info)

        self.ui.comboBox_quickRecallInvoice.activated.connect(self.on_combo_box_invoice_changed)
        self.ui.comboBox_quickRecallClient.activated.connect(self.on_combo_box_client_changed)
        self.ui.comboBox_quickRecallGeneral.activated.connect(self.on_combo_box_general_changed)

        self.ui.pushButton_generateInvoice.clicked.connect(self.generate_invoice)

        self.ui.toolButton_add.clicked.connect(self.add_row)
        self.ui.toolButton_delete.clicked.connect(self.delete_row)
        self.update_ui()

    def save_data(self):
        self.update_infos_from_UI()
        self.save_invoice_info()
        self.save_client_info()
        self.save_general_info()

        if self.saveData.save_client(self.currentClientInfo) and \
                self.saveData.save_invoice(self.currentInvoiceInfo) and \
                self.saveData.save_general(self.currentGeneralInfo):
            self.saveData.save_to_file()
        else:
            self.warning_message("Invalid invoice formatting\n Check for empty fields")

    def load_data(self):
        pass

    def list_client(self):
        self.ui.comboBox_quickRecallClient.clear()
        for client in self.saveData.clients:
            self.ui.comboBox_quickRecallClient.addItem(client.name)

    def list_general(self):
        self.ui.comboBox_quickRecallGeneral.clear()
        for general in self.saveData.generals:
            self.ui.comboBox_quickRecallGeneral.addItem(general.company_name)
        pass

    def list_invoice(self):
        self.ui.comboBox_quickRecallInvoice.clear()
        for invoice in self.saveData.invoices:
            self.ui.comboBox_quickRecallInvoice.addItem(invoice.invoice_number)

    def generate_invoice(self):
        print("generating invoice")
        self.save_data()
        self.texGenerator.render(SaveData.asflatdict(self.currentInvoiceInfo))
        self.update_ui()

    def recall_general_info(self, company_name):
        newGeneral = self.saveData.get_general(company_name)
        self.ui.lineEdit_companyName.setText(newGeneral.company_name)
        self.ui.lineEdit_firstName.setText(newGeneral.first_name)
        self.ui.lineEdit_lastName.setText(newGeneral.last_name)
        self.ui.lineEdit_fullAddress.setText(newGeneral.full_address)
        self.ui.lineEdit_companySIRET.setText(newGeneral.company_siret)
        self.ui.lineEdit_companySIREN.setText(newGeneral.company_siren)
        self.ui.lineEdit_companyEmail.setText(newGeneral.company_email)
        self.ui.lineEdit_companyTelephone.setText(newGeneral.company_phone)
        self.ui.lineEdit_bankIBAN.setText(newGeneral.bank_iban)
        self.ui.lineEdit_bankBIC.setText(newGeneral.bank_bic)

    def recall_client_info(self, name):
        newClient = self.saveData.get_client(name)
        self.ui.lineEdit_clientName.setText(newClient.name)
        self.ui.lineEdit_clientAddressFirst.setText(newClient.address_first_line)
        self.ui.lineEdit_clientAdressSecond.setText(newClient.address_second_line)
        self.update_infos_from_UI()

    def recall_invoice_info(self, invoice_number):
        newInvoice = self.saveData.get_invoice(invoice_number)

        self.ui.lineEdit_invoiceNumber.setText(newInvoice.invoice_number)
        self.ui.lineEdit_invoiceDate.setText(newInvoice.invoice_date)


        self.ui.tableWidget_invoiceContent.clearContents()
        for item in newInvoice.items:
            row_position = self.ui.tableWidget_invoiceContent.rowCount()
            self.ui.tableWidget_invoiceContent.insertRow(row_position)
            self.ui.tableWidget_invoiceContent.setItem(row_position, 0, QTableWidgetItem(str(item.product_name)))
            self.ui.tableWidget_invoiceContent.setItem(row_position, 1, QTableWidgetItem(str(item.quantity)))
            self.ui.tableWidget_invoiceContent.setItem(row_position, 2, QTableWidgetItem(str(item.price)))


        self.recall_client_info(newInvoice.client.name)
        self.recall_general_info(newInvoice.general.company_name)
        self.update_infos_from_UI()

    def on_combo_box_client_changed(self, index):
        self.recall_client_info(self.ui.comboBox_quickRecallClient.itemText(index))

    def on_combo_box_general_changed(self, index):
        self.recall_general_info(self.ui.comboBox_quickRecallGeneral.itemText(index))

    def on_combo_box_invoice_changed(self, index):
        self.recall_invoice_info(self.ui.comboBox_quickRecallInvoice.itemText(index))

    def save_invoice_info(self):
        self.update_infos_from_UI()
        if not self.saveData.save_invoice(self.currentInvoiceInfo):
            self.warning_message("Couldn't save new Invoice")
        self.update_ui()

    def save_general_info(self):
        self.update_infos_from_UI()
        if not self.saveData.save_general(self.currentGeneralInfo):
            self.warning_message("Couldn't save new General")
        self.update_ui()

    def save_client_info(self):
        self.update_infos_from_UI()
        if not self.saveData.save_client(self.currentClientInfo):
            self.warning_message("Couldn't save new Client")
        self.update_ui()

    def add_row(self):
        self.ui.tableWidget_invoiceContent.insertRow(self.ui.tableWidget_invoiceContent.rowCount())

    def delete_row(self):
        self.ui.tableWidget_invoiceContent.removeRow(self.ui.tableWidget_invoiceContent.currentRow())

    def ask_validation(self, text, informative_text, title="Validation Dialog"):
        msgBox = QMessageBox()
        msgBox.setWindowTitle("hey")
        msgBox.setText(text)
        msgBox.setInformativeText(informative_text)
        msgBox.setStandardButtons(QMessageBox.Apply | QMessageBox.Cancel)
        msgBox.setDefaultButton(QMessageBox.Cancel)
        ret = msgBox.exec_()
        return True if ret == QMessageBox.Apply else False

    def warning_message(self, text):
        ret = QMessageBox.warning(self, self.tr("Warning"),
                                  self.tr(text),
                                  QMessageBox.Ok,
                                  QMessageBox.Ok)

    def update_infos_from_UI(self):
        currentGeneralInfo = GeneralInfo()
        currentGeneralInfo.company_name = self.ui.lineEdit_companyName.text()
        currentGeneralInfo.first_name = self.ui.lineEdit_firstName.text()
        currentGeneralInfo.last_name = self.ui.lineEdit_lastName.text()
        currentGeneralInfo.full_address = self.ui.lineEdit_fullAddress.text()
        currentGeneralInfo.company_siret = self.ui.lineEdit_companySIRET.text()
        currentGeneralInfo.company_siren = self.ui.lineEdit_companySIREN.text()
        currentGeneralInfo.company_email = self.ui.lineEdit_companyEmail.text()
        currentGeneralInfo.company_phone = self.ui.lineEdit_companyTelephone.text()
        currentGeneralInfo.bank_iban = self.ui.lineEdit_bankIBAN.text()
        currentGeneralInfo.bank_bic = self.ui.lineEdit_bankBIC.text()

        currentClientInfo = ClientInfo()
        currentClientInfo.name = self.ui.lineEdit_clientName.text()
        currentClientInfo.address_first_line = self.ui.lineEdit_clientAddressFirst.text()
        currentClientInfo.address_second_line = self.ui.lineEdit_clientAdressSecond.text()

        currentInvoiceInfo = InvoiceInfo()
        currentInvoiceInfo.invoice_number = self.ui.lineEdit_invoiceNumber.text()
        currentInvoiceInfo.invoice_date = self.ui.lineEdit_invoiceDate.text()
        currentInvoiceInfo.general = self.currentGeneralInfo
        currentInvoiceInfo.client = self.currentClientInfo

        currentInvoiceInfo.items = []

        for row in range(self.ui.tableWidget_invoiceContent.rowCount()):
            newItem = InvoiceItem()
            newItem.product_name = self.ui.tableWidget_invoiceContent.item(row, 0).text() \
                if self.ui.tableWidget_invoiceContent.item(row, 0) is not None else ""
            newItem.quantity = int(self.ui.tableWidget_invoiceContent.item(row, 1).text()) \
                if self.ui.tableWidget_invoiceContent.item(row, 1) is not None else 0
            newItem.price = float(self.ui.tableWidget_invoiceContent.item(row, 2).text()) \
                if self.ui.tableWidget_invoiceContent.item(row, 2) is not None else 0
            currentInvoiceInfo.items.append(newItem)

        self.currentGeneralInfo = currentGeneralInfo
        self.currentClientInfo = currentClientInfo
        self.currentInvoiceInfo = currentInvoiceInfo

    def update_ui(self):
        self.list_invoice()
        self.list_client()
        self.list_general()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
