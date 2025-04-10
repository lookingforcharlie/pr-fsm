# Create Finite State Machine to simulate mod 3
def mod_three_standard(binary_str: str) -> int:
    """
    Computes the remainder when a binary number is divided by 3

    Args:
        binary_string: A string of '0's and '1's representing a binary number

    Returns:
        The remainder when the binary number is divided by 3 (0, 1, or 2)
    """
    # State transition table
    # (value = value * 2 + bit_we_are_seeing) is how we convert the binary to decimal
    # Nested Dictionary: more readable and intuitive and easy to access by transition[state][bit]
    transition = {
        "S0": {"0": "S0", "1": "S1"},
        "S1": {"0": "S2", "1": "S0"},
        "S2": {"0": "S1", "1": "S2"},
    }

    # Final state to remainder mapping
    output = {
        "S0": 0,
        "S1": 1,
        "S2": 2,
    }

    state = "S0"  # Initial state

    for bit in binary_str:
        if bit not in ("0", "1"):
            raise ValueError(f"Invalid character '{bit}' found in binary string.")
        state = transition[state][bit]

    return output[state]


print(mod_three_standard("1101"))
print(mod_three_standard("1110"))
print(mod_three_standard("1111"))
