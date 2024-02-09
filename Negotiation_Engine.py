class NegotiationEngine:
    def __init__(self, start_price, round_limit=5, convergence_limit=0.05):
        self.start_price = start_price  # Initialize the starting price for negotiation
        self.round_limit = round_limit  # Set the maximum number of negotiation rounds
        self.convergence_limit = convergence_limit  # Define the threshold for convergence
        self.rounds_done = 0  # Initialize the count of completed negotiation rounds
        self.previous_offer = start_price  # Track the last offer made
        self.negotiation_state = "In Progress"  # Set the initial state of negotiation
        self.offer_history = []  # Initialize a list to record all offers made

    def propose(self, new_offer):
        if self.rounds_done >= self.round_limit:  # Check if maximum rounds have been reached
            self.negotiation_state = "Terminated: Max rounds reached"  # Update the negotiation state
            return self.negotiation_state  # Return the negotiation state

        self.offer_history.append(new_offer)  # Record the new offer in the history
        # Calculate the relative change between the new offer and the previous one
        offer_change = abs(new_offer - self.previous_offer) / self.previous_offer

        # Determine if the negotiation is converging based on the change
        if offer_change <= self.convergence_limit:
            self.negotiation_state = "Converging"  # Update the state to converging
        else:
            self.negotiation_state = "Diverging"  # Update the state to diverging

        self.previous_offer = new_offer  # Update the last offer to the new offer
        self.rounds_done += 1  # Increment the count of completed rounds

        return self.negotiation_state  # Return the current negotiation state

    def accept_offer(self):
        self.negotiation_state = "Agreement Reached"  # Set the state to indicate an agreement
        return self.negotiation_state  # Return the current negotiation state

    def terminate_negotiation(self):
        self.negotiation_state = "Terminated by User"  # Allow manual termination of the negotiation
        return self.negotiation_state  # Return the current negotiation state

    def get_negotiation_status(self):
        return self.negotiation_state  # Return the current state of the negotiation


# Example Usage

negotiation = NegotiationEngine(start_price=100)  # Initialize the negotiation engine with a starting price

# Seller proposes initial price
print(negotiation.get_negotiation_status())  # Print the initial negotiation state

# Buyer counters with a new offer
negotiation.propose(90)  # Propose a new offer
print(negotiation.get_negotiation_status())  # Print the updated negotiation state

# Seller counters with another offer
negotiation.propose(95)  # Propose another new offer
print(negotiation.get_negotiation_status())  # Print the negotiation state again

# Buyer accepts the last offer
negotiation.accept_offer()  # Accept the current offer to reach an agreement
print(negotiation.get_negotiation_status())  # Print the final negotiation state
