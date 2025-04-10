import pytest

from advanced_fsm import mod_three_advanced
from standard_fsm import mod_three_standard


class TestStandardFSM:
    """Tests for the standard finite state machine (mod_three_standard)."""

    def test_mod_three_standard_1(self):
        assert mod_three_standard("1101") == 1

    def test_mod_three_standard_2(self):
        assert mod_three_standard("1110") == 2

    def test_mod_three_standard_3(self):
        assert mod_three_standard("1111") == 0


class TestAdvancedFSM:
    """Tests for the advanced finite state machine (mod_three_advanced)."""

    def test_mod_three_advanced_1(self):
        assert mod_three_advanced("1101") == 1

    def test_mod_three_advanced_2(self):
        assert mod_three_advanced("1110") == 2

    def test_mod_three_advanced_3(self):
        assert mod_three_advanced("1111") == 0
