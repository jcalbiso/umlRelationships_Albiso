class Printer:
    def print_message(self, message):
        print(message)

class Report:
    def generate(self, printer):
        printer.print_message("Report generated.")

printer = Printer()
report = Report()

report.generate(printer)