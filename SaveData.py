import json


class GeneralInfo:
    def __init__(self, company_name=None, first_name=None, last_name=None, full_address=None, company_email=None,
                 company_siret=None, company_siren=None, company_phone=None, bank_iban=None, bank_bic=None):
        self.company_name = company_name
        self.first_name = first_name
        self.last_name = last_name
        self.full_address = full_address
        self.company_email = company_email
        self.company_siret = company_siret
        self.company_siren = company_siren
        self.company_phone = company_phone
        self.bank_iban = bank_iban
        self.bank_bic = bank_bic

    def asdict(self):
        return {'company_name': self.company_name,
                'first_name': self.first_name,
                'last_name': self.last_name,
                'full_address': self.full_address,
                'company_email': self.company_email,
                'company_siret': self.company_siret,
                'company_siren': self.company_siren,
                'company_phone': self.company_phone,
                'bank_iban': self.bank_iban,
                'bank_bic': self.bank_bic}

    @classmethod
    def fromdict(cls, dict_from):
        newgeneral = cls()
        newgeneral.company_name = dict_from['company_name']
        newgeneral.first_name = dict_from['first_name']
        newgeneral.last_name = dict_from['last_name']
        newgeneral.full_address = dict_from['full_address']
        newgeneral.company_email = dict_from.get('company_email', "")
        newgeneral.company_siret = dict_from['company_siret']
        newgeneral.company_siren = dict_from['company_siren']
        newgeneral.company_phone = dict_from['company_phone']
        newgeneral.bank_iban = dict_from['bank_iban']
        newgeneral.bank_bic = dict_from['bank_bic']
        return newgeneral


class ClientInfo:
    def __init__(self, name=None, address_first_line=None, address_second_line=None):
        self.name = name
        self.address_first_line = address_first_line
        self.address_second_line = address_second_line

    def asdict(self):
        return {'name': self.name,
                'address_first_line': self.address_first_line,
                'address_second_line': self.address_second_line}

    @classmethod
    def fromdict(cls, dict_from):
        newclient = cls()
        newclient.name = dict_from['name']
        newclient.address_first_line = dict_from['address_first_line']
        newclient.address_second_line = dict_from['address_second_line']
        return newclient


class InvoiceInfo:
    def __init__(self, invoice_number=None, invoice_date=None, invoice_name=None, general=None, client=None, items=[]):
        self.general = general
        self.client = client
        self.invoice_number = invoice_number
        self.invoice_date = invoice_date
        self.invoice_name = invoice_name
        self.items = items

    def asdict(self):
        newItemList = []
        for item in self.items:
            if item is not None:
                newItemList.append(item.asdict())
        return {'general': self.general.asdict(),
                'client': self.client.asdict(),
                'invoice_number': self.invoice_number,
                'invoice_date': self.invoice_date,
                'invoice_name': self.invoice_name,
                'items': newItemList}

    @classmethod
    def fromdict(cls, dict_from):
        newinvoice = cls()

        newItemList = []
        for item in dict_from['items']:
            if item is not None:
                newItemList.append(InvoiceItem.fromdict(item))

        newinvoice.general = GeneralInfo.fromdict(dict_from['general'])
        newinvoice.client = ClientInfo.fromdict(dict_from['client'])
        newinvoice.invoice_number = dict_from['invoice_number']
        newinvoice.invoice_date = dict_from['invoice_date']
        newinvoice.invoice_name = dict_from.get('invoice_name', '')
        newinvoice.items = newItemList
        return newinvoice


class InvoiceItem:
    def __init__(self, product_name=None, quantity=0, price=0):
        self.product_name = product_name
        self.quantity = quantity
        self.price = price

    def asdict(self):
        return {'product_name': self.product_name,
                'quantity': self.quantity,
                'price': self.price
                }

    @classmethod
    def fromdict(cls, dict_from):
        newinvoiceitem = cls()
        newinvoiceitem.product_name = dict_from['product_name']
        newinvoiceitem.price = dict_from['price']
        newinvoiceitem.quantity = dict_from['quantity']
        return newinvoiceitem


class SaveData:
    def __init__(self, saveFile):
        self.pathToFile = saveFile
        self.clients = []
        self.generals = []
        self.invoices = []
        try:
            self.load_from_file()
        except FileNotFoundError:
            print("No config found")
        except json.JSONDecodeError:
            print("Invalid json formatting")

    @staticmethod
    def asflatdict(invoice: InvoiceInfo):
        newitemslist = []
        for item in invoice.items:
            newitemslist.append(item.asdict())
        flatdict = {
            'invoice_number': invoice.invoice_number,
            'invoice_date': invoice.invoice_date,
            'invoice_name': invoice.invoice_name,
            'company_name': invoice.general.company_name,
            'first_name': invoice.general.first_name,
            'last_name': invoice.general.last_name,
            'full_address': invoice.general.full_address,
            'company_siret': invoice.general.company_siret,
            'company_siren': invoice.general.company_siren,
            'company_phone': invoice.general.company_phone,
            'company_email': invoice.general.company_email,
            'bank_iban': invoice.general.bank_iban,
            'bank_bic': invoice.general.bank_bic,
            'client_name': invoice.client.name,
            'client_address_first_line': invoice.client.address_first_line,
            'client_address_second_line': invoice.client.address_second_line,
            'items':newitemslist
        }
        return flatdict

    def save_to_file(self):
        with open(self.pathToFile, "w+") as write_file:
            print(self.__save_to_dict())
            json.dump(self.__save_to_dict(), write_file, sort_keys=True, indent=4)

    def load_from_file(self):
        with open(self.pathToFile, "r") as read_file:
            self.__load_from_dict(json.load(read_file))

    def __save_to_dict(self):
        general_dict_list = []
        for general in self.generals:
            general_dict_list.append(general.asdict())
        client_dict_list = []
        for client in self.clients:
            client_dict_list.append(client.asdict())
        invoices_dict_list = []
        for invoice in self.invoices:
            invoices_dict_list.append(invoice.asdict())
        toDict = {'generals': general_dict_list,
                  'clients': client_dict_list,
                  'invoices': invoices_dict_list}
        return toDict

    def __load_from_dict(self, fromDict):
        generals_list = []
        clients_list = []
        invoices_list = []

        for general in fromDict['generals']:
            generals_list.append(GeneralInfo.fromdict(general))
        for client in fromDict['clients']:
            clients_list.append(ClientInfo.fromdict(client))
        for invoice in fromDict['invoices']:
            invoices_list.append(InvoiceInfo.fromdict(invoice))
        self.generals = generals_list
        self.clients = clients_list
        self.invoices = invoices_list

    def save_general(self, general_info: GeneralInfo):
        if general_info.company_name == "":
            return False
        replaced = False
        for index, general in enumerate(self.generals):
            if self.generals[index].company_name == general_info.company_name:
                self.generals[index] = general_info
                replaced = True
        if not replaced:
            self.generals.append(general_info)
        return True

    def save_client(self, client_info: ClientInfo):
        if client_info.name == "":
            return False
        replaced = False
        for index, client in enumerate(self.clients):
            if self.clients[index].name == client_info.name:
                self.clients[index] = client_info
                replaced = True
        if replaced == False:
            self.clients.append(client_info)
        return True

    def save_invoice(self, invoice_info: InvoiceInfo):
        if (invoice_info.invoice_number == "") or (not invoice_info.items):
            return False
        replaced = False
        for index, invoice in enumerate(self.invoices):
            if self.invoices[index].invoice_number == invoice_info.invoice_number:
                self.invoices[index] = invoice_info
                replaced = True
        if not replaced:
            self.invoices.append(invoice_info)
        return True

    def get_invoice(self, invoice_number) -> InvoiceInfo:
        for invoice in self.invoices:
            if invoice.invoice_number == invoice_number:
                return invoice
        return None

    def get_client(self, name) -> ClientInfo:
        for client in self.clients:
            if client.name == name:
                return client
        return None

    def get_general(self, company_name) -> GeneralInfo:
        for general in self.generals:
            if general.company_name == company_name:
                return general
        return None
