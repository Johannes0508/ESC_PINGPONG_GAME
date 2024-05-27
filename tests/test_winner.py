import pytest
from winner_component import WinnerComponent

def test_winner_initialization():
    # Test default initialization
    component = WinnerComponent()
    assert component.winner == 0

    # Test initialization with a specified winner
    component = WinnerComponent(1)
    assert component.winner == 1

def test_winner_attribute():
    # Arrange
    component = WinnerComponent(2)
    
    # Act & Assert
    assert component.winner == 2
    
    # Modify attribute
    component.winner = 3
    
    # Assert
    assert component.winner == 3

# För att köra testerna med pytest, använd kommandot:
# pytest test_winner_component.py
