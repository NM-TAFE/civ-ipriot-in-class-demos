"""
class PaymentIntent {
    -string customer_id
    -long amount
    -string currency
    -datetime created_at
    -PaymentMethod[] payment_methods

    +debit_payment()
    +is_completed() bool
    +is_attempted() datetime
    +is_valid() bool
}

"""