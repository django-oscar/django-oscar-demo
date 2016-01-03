from oscar.apps.checkout import app

from oscar_demo.apps.checkout import views


class CheckoutApplication(app.CheckoutApplication):
    # Replace the payment details view with our own
    payment_details_view = views.PaymentDetailsView


application = CheckoutApplication()
