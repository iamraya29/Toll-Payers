import streamlit as st
import stripe
import uuid  # For generating unique IDs
import os

# Set your Stripe API keys
stripe.api_key = os.environ.get('STRIPE_SECRET_KEY', 'sk_test_51P1ssxSGjphJxLwP8xzAYVhYhLJLmYAPMrGGkpurxrC5B4aOu5OE2SLLzgTPg9RvAlAn9dH83zQK5O7aD3gwThPS00IWDDNfe2')

def create_payment_intent(total_amount, session_id):
    """
    Creates a Payment Intent on Stripe.

    Args:
        total_amount (int): The total amount in paisa.
        session_id (str): A unique session ID for reference.

    Returns:
        stripe.PaymentIntent: The created Payment Intent object or None on error.
    """
    try:
        intent = stripe.PaymentIntent.create(
            amount=total_amount,
            currency="inr",
            confirm=False,
            metadata={"session_id": session_id},
        )
        return intent
    except stripe.error.StripeError as e:
        st.error(f"Error creating payment intent: {e}")
        return None

def generate_unique_session_id():
    """
    Generates a unique session ID.

    Returns:
        str: A unique session ID string.
    """
    return str(uuid.uuid4())

def payment_options_page():
    """
    Defines the content for the payment page.
    """
    st.title("Payment Page")
    st.write("Welcome to the payment page. Please enter the amount you wish to pay in INR.")

    # Prompt for exact amount to pay
    total_amount = st.number_input("Enter Amount to Pay (INR)", min_value=0.01, format="%.2f")  # Allow minimum of ₹0.01

    # Convert to integer amount in paisa
    total_amount_in_paisa = int(total_amount)

    session_id = generate_unique_session_id()

    # Payment processing section
    if st.button("Pay Now"):
        intent = create_payment_intent(total_amount_in_paisa, session_id)

        if intent:
            # Placeholder for Stripe.js integration (see instructions below)
            st.write(
                """<script>
                // Replace with your Stripe.js code to collect payment method details
                // and send them to your backend server to confirm the Payment Intent.
                </script>""",
                unsafe_allow_html=True,
            )

def main():
    """
    The main function that runs the application.
    """
    st.title("Be Responsible And Kindly Pay Toll Tax")

    # Call the payment_options_page function
    payment_options_page()

if __name__ == "__main__":
    main()
