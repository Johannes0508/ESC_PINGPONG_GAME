import pytest
from pygame import Rect
from rect_component import RectComponent

def test_rect_initialization():
    # Arrange
    x, y, width, height = 10, 20, 30, 40
    
    # Act
    component = RectComponent(x, y, width, height)
    
    # Assert
    assert component.rect.x == x
    assert component.rect.y == y
    assert component.rect.width == width
    assert component.rect.height == height

def test_rect_attributes():
    # Arrange
    component = RectComponent(5, 15, 25, 35)
    
    # Act & Assert
    assert component.rect.x == 5
    assert component.rect.y == 15
    assert component.rect.width == 25
    assert component.rect.height == 35
    
    # Modify attributes
    component.rect.x = 50
    component.rect.y = 60
    component.rect.width = 70
    component.rect.height = 80
    
    # Assert
    assert component.rect.x == 50
    assert component.rect.y == 60
    assert component.rect.width == 70
    assert component.rect.height == 80

# För att köra testerna med pytest, använd kommandot:
# pytest test_rect_component.py
