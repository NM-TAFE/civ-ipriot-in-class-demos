# OOP Examples

Here are some OOP examples written in Python.

A lot of OOP examples are a little more whimsical, or 'toy-ish'.

It's quite common to see something like this, when you're starting out in OOP.

```mermaid
classDiagram
    Animal <|-- Dog
    Animal <|-- Cat
    Animal: +eat()
    Animal: +genus()
    Animal: +species()
    Animal: +move()
    Animal: -int age
    Animal: -string name
    Dog: +bark()
    Cat: +meow()
```

That's fine, and it gets the idea across, but maybe it's nice to see something a bit more grounded in the reality of what you might be programming.  After all, unless you're making a life simulator or a video game, there's probably not a lot of reason to design classes like these.


# Payments Processor
This project, in the subfolder `payments_processor`, is a self-contained Python CLI-based program.  It doesn't do much.  It brings up a toy payments processor.

The idea here is that we're looking at a small subset of the functions of a payments processor, encapsulated in an OOP way.

The only thing that this program is supposed to do is to capture *inbound* payments from customers (to "your business").

"Your business" doesn't really care how the payment is made to you, only that it is made.  For all you care, the customer may be sending you your payment by carrier pigeon.

> [!Important Note]
>
> You cannot actually just store payment details in reality without a lot of work! 
> We often rely on third party payment processors to handle this data storage for us, because it's very dangerous to store this kind of customer information.
> But this is a toy, so we can pretend.

```mermaid
classDiagram
    class PaymentMethod {
        <<Abstract>>
        -string billing_details_id
        -string customer_id
        -payment_implementation(amount)*
        +pay(amount)
        +is_valid()*
    }

    class CreditCard {
        -string cc_number
        -date expiry_date
        -string type
        -connect_to_cc_processor()
        -payment_implementation(amount)
        +is_valid()
    }


    class BECSDebit {
        -string bsb
        -string account_number
        -connect_to_becs_rails()
        -payment_implementation(amount)
        +is_valid()
    }

    class NPPDebit {
        -string bsb
        -string account_number
        -string pay_id
        -connect_to_npp_rails()
        -payment_implementation(amount)

        +is_valid()
    }

    class Paypal {
        -string paypal_id
        -string paypal_token
        -connect_to_paypal_api()
        -payment_implementation(amount)

        +is_valid()
    }

    class CarrierPigeon {
        <<Joke>>
        -string paypal_id
        -release_the_pigeon()
        -payment_implementation(amount)

        +is_valid()
    }

    CreditCard ..|> PaymentMethod : implements
    BECSDebit ..|> PaymentMethod : implements
    NPPDebit ..|> PaymentMethod : implements
    Paypal ..|> PaymentMethod : implements
    CarrierPigeon ..|> PaymentMethod : implements

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

    class Attempts {
        -string payment_intent_id
        -datetime created_at
        -enum outcome
        -string message

        +is_successful() bool
    }

    PaymentIntent "1" --> "+" PaymentMethod
    PaymentIntent "1" --> "*" Attempts
```
