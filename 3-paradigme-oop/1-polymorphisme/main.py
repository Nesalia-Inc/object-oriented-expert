

class PaymentProcessor:
    def process_payment(self, amount : float) -> str:
        raise NotImplementedError("Cette méthode doit être implémentée par les sous-classes")


class CreditCardPayment(PaymentProcessor):
    def process_payment(self, amount : float) -> str:
        return f"Traitement du paiement de {amount}€ via carte de crédit."


class PayPalPayment(PaymentProcessor):
    def process_payment(self, amount : float) -> str:
        return f"Traitement du paiement de {amount}€ via PayPal."


class BankTransferPayment(PaymentProcessor):
    def process_payment(self, amount : float) -> str:
        return f"Traitement du paiement de {amount}€ via virement bancaire."



def process_all_payments(payment_processors : list[PaymentProcessor], amount : float) -> None:
    for processor in payment_processors:
        print(processor.process_payment(amount))



if __name__ == '__main__':
    payment_processors = [CreditCardPayment(), PayPalPayment(), BankTransferPayment()]

    process_all_payments(payment_processors, 100)
