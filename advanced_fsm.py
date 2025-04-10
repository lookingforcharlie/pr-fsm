from typing import Dict, Set, Tuple, Any


class FSM:
    """Generic Finite State Machine class"""

    def __init__(
        self,
        states: Set[str],
        alphabet: Set[str],
        initial_state: str,
        final_states: Set[str],
        # Flat Dictionary with Tuple Keys: easier to validate (if (state, symbol) in transition_function)
        transition_function: Dict[Tuple[str, str], str],
    ):
        self.states = states
        self.alphabet = alphabet
        self.current_state = initial_state
        self.initial_state = initial_state
        self.final_states = final_states
        self.transition_function = transition_function

    def reset(self):
        """
        Reset the FSM to the initial state
        Allow you reuse the same FSM instance multiple times without having to re-create it
        """
        self.current_state = self.initial_state

    def process(self, input_str: str):
        """Process the input string one symbol at a time."""
        for symbol in input_str:
            if symbol not in self.alphabet:
                raise ValueError(
                    f"Invalid input symbol: '{symbol}' not in alphabet {self.alphabet}"
                )
            key = (self.current_state, symbol)
            if key not in self.transition_function:
                raise ValueError(
                    f"No transition from state '{self.current_state}' on input '{symbol}'"
                )
            self.current_state = self.transition_function[key]

    def get_current_state(self) -> str:
        """
        Return the FSM's current state after processing input
        """
        return self.current_state

    def is_accepting(self) -> bool:
        """
        Check if the FSM is in one of its accepting (final) states
        """
        return self.current_state in self.final_states


def mod_three_advanced(binary_str: str) -> int:
    # Define the FSM
    states = {"S0", "S1", "S2"}
    alphabet = {"0", "1"}
    initial_state = "S0"
    final_states = {"S0", "S1", "S2"}  # All are valid end states
    transition_function = {
        ("S0", "0"): "S0",
        ("S0", "1"): "S1",
        ("S1", "0"): "S2",
        ("S1", "1"): "S0",
        ("S2", "0"): "S1",
        ("S2", "1"): "S2",
    }

    fsm = FSM(states, alphabet, initial_state, final_states, transition_function)
    fsm.process(binary_str)

    output_mapping = {
        "S0": 0,
        "S1": 1,
        "S2": 2,
    }

    return output_mapping[fsm.get_current_state()]


print(mod_three_advanced("1101"))
print(mod_three_advanced("1110"))
print(mod_three_advanced("1111"))
