def calculate_pending(total_fee, paid):
    return total_fee - paid


def get_payment_status(pending):
    if pending <= 0:
        return "Fully Paid"
    else:
        return "Payment Pending"