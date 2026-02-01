import pytest
from unittest.mock import patch
from ..treasure_island.treasure_island_run import treasure_island_game

def test_treasure_island_left_wait_yellow():
    user_inputs = ["left", "wait", "yellow"]
    expected_output = "You found the treasure! You Win!"

    with patch("builtins.input", side_effect=user_inputs):
        result = treasure_island_game()
        assert result == expected_output

def test_treasure_island_left_wait_red():
    user_inputs = ["left", "wait", "red"]
    expected_output = "It's a room full of fire. Game Over."

    with patch("builtins.input", side_effect=user_inputs):
        result = treasure_island_game()
        assert result == expected_output

def test_treasure_island_left_swim():
    user_inputs = ["left", "swim"]
    expected_output = "You get attacked by an angry trout. Game Over."

    with patch("builtins.input", side_effect=user_inputs):
        result = treasure_island_game()
        assert result == expected_output

def test_treasure_island_right():
    user_inputs = ["right"]
    expected_output = "You fell into a hole. Game Over."

    with patch("builtins.input", side_effect=user_inputs):
        result = treasure_island_game()
        assert result == expected_output

def test_treasure_island_invalid():
    user_inputs = ["invalid", "left", "wait", "yellow"]
    expected_output = "You found the treasure! You Win!"

    with patch("builtins.input", side_effect=user_inputs), patch("builtins.print") as mock_print:
        result = treasure_island_game()
        assert result == expected_output
        mock_print.assert_any_call("You chose a path that doesn't exist. Try again.")