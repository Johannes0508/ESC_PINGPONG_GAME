import pytest
from speed_component import SpeedComponent

def test_speed_initialization():
    # Arrange
    speed = 10.0
    
    # Act
    component = SpeedComponent(speed)
    
    # Assert
    assert component.speed == speed
    assert component.x_speed == speed
    assert component.y_speed == -speed

def test_speed_attributes():
    # Arrange
    component = SpeedComponent(5.0)
    
    # Act & Assert
    assert component.speed == 5.0
    assert component.x_speed == 5.0
    assert component.y_speed == -5.0
    
    # Modify attributes
    component.speed = 15.0
    component.x_speed = 20.0
    component.y_speed = -20.0
    
    # Assert
    assert component.speed == 15.0
    assert component.x_speed == 20.0
    assert component.y_speed == -20.0

# För att köra testerna med pytest, använd kommandot:
# pytest test_speed_component.py
