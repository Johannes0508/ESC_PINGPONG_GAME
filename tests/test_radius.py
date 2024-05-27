import pytest
from radius_component import RadiusComponent

def test_radius_initialization():
    # Arrange
    radius = 10.0
    
    # Act
    component = RadiusComponent(radius)
    
    # Assert
    assert component.radius == radius

def test_radius_attribute():
    # Arrange
    component = RadiusComponent(5.0)
    
    # Act & Assert
    assert component.radius == 5.0
    
    # Modify attribute
    component.radius = 15.0
    
    # Assert
    assert component.radius == 15.0

# För att köra testerna med pytest, använd kommandot:
# pytest test_radius_component.py
