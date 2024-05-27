# test_position.py
# test_position_component.py
import pytest
from position_component import PositionComponent

def test_position_initialization():
    # Arrange
    x = 10
    y = 20
    
    # Act
    position = PositionComponent(x, y)
    
    # Assert
    assert position.x == x
    assert position.y == y

def test_position_attributes():
    # Arrange
    position = PositionComponent(5, 15)
    
    # Act & Assert
    assert position.x == 5
    assert position.y == 15
    
    # Modify attributes
    position.x = 25
    position.y = 35
    
    # Assert
    assert position.x == 25
    assert position.y == 35

# Om du vill köra testerna med pytest, använd kommandot:
# pytest test_position_component.py
