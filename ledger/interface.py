import sys
import cmd

from ledger.loan import Loan
from ledger.logger import get_logger


class Interface(cmd.Cmd):
    logger = get_logger()

    intro = 'Welcome to Ledger Co. Type help to list commands.\n'
    prompt = '>'
    bankLedger = {}

    # ----- Ledger commands -----


    def do_LOAN(self, arg):
        # Command Format: LOAN Bankname Username Principal_amount No_of_years Rate_of_interst
        try:
            argList = parseArgs(arg)
            bankname, name, principal_amount, noOfYears, rate = argList
            principal_amount = int(principal_amount)
            noOfYears = int(noOfYears)
            rate = int(rate)
        except:
            self.logger.warning("Please check the input format")

        id = (bankname + "_" + name).upper()
        self.bankLedger[id] = Loan(bankname, name, principal_amount, noOfYears, rate)


    def do_BALANCE(self, arg):
        # Command Format: BALANCE Bankname Username EmiNumber
        try:
            agrList = parseArgs(arg)
            bankname, name, emiNumber = agrList
            emiNumber = int(emiNumber)
        except:
            self.logger.warning("Please check the input format")

        id = (bankname + "_" + name).upper()
        if id in self.bankLedger:
            response = self.bankLedger[id].balance(emiNumber)
            print(response['bankname']
                  + ' '+response['person']
                    + ' '+str(response['amount_paid'])
                    + ' '+str(response['no_Of_Emis_Left'])
                  )
        else:
            self.logger.warning("User Not Found")


    def do_PAYMENT(self, arg):
        # Command Format: PAYMENT Bankname Username LumpsumAmount EmiNumber
        try:
            agrList = parseArgs(arg)
            bankname, name, lump_sum, emiNumber = agrList
            lump_sum = int(lump_sum)
            emiNumber = int(emiNumber)
            id = (bankname + "_" + name).upper()
        except:
            self.logger.warning("Please check the input format")
        id = (bankname + "_" + name).upper()
        if id in self.bankLedger:
            self.bankLedger[id].payment(lump_sum, emiNumber)
        else:
            self.logger.warning("User Not Found")


    def do_exit(self, arg):
        'Exit from the Ledger Co'
        print('Bye.')
        return True


def parseArgs(arg):
    # Convert a series of zero or more numbers to an argument tuple
    return tuple(map(str, arg.split()))