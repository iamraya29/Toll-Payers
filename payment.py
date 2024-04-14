import stripe
import os

# Set your Stripe API keys
stripe.api_key = os.environ.get('STRIPE_SECRET_KEY', 'your_stripe_secret_key')

def create_payment_intent(amount):
    try:
        intent = stripe.PaymentIntent.create(
            amount=amount,
            currency="usd",
            confirm=True,
            payment_method_types=["card"],
        )
        return intent.client_secret
    except stripe.error.StripeError as e:
        st.error(f"Error creating payment intent: {e}")
        return None
