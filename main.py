# Принцип розділення інтерфейсів (Interface Segregation Principle)

from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print_document(self, document):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan_document(self):
        pass

class Fax(ABC):
    @abstractmethod
    def send_fax(self, document):
        pass

class BasicPrinter(Printer):
    def print_document(self, document):
        print(f"Друк документа: {document}")

class MultiFunctionDevice(Printer, Scanner, Fax):
    def print_document(self, document):
        print(f"Друк документа: {document}")

    def scan_document(self):
        print("Сканування документа")

    def send_fax(self, document):
        print(f"Надсилання факсу з документом: {document}")

if __name__ == "__main__":
    printer = BasicPrinter()
    printer.print_document("Тестовий документ")

    mfd = MultiFunctionDevice()
    mfd.print_document("Звіт")
    mfd.scan_document()
    mfd.send_fax("Контракт")
