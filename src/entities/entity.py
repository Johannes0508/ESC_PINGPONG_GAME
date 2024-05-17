class Entity:
  """A class representing an entity in the game.

  Attributes:
      id (int): The unique ID of the entity.
      components (dict): A dictionary to store the components of the entity.

  Methods:
      add_component(component): Adds a component to the entity.
      get_component(component_type): Retrieves a component from the entity.

  """
  id_counter = 0

  def __init__(self):
    self.id = Entity.id_counter
    Entity.id_counter += 1
    self.components = {}

  def add_component(self, component):
    """
    Add a component to the game.

    Args:
      component (object): The component to be added.

    Returns:
      None
    """
    self.components[type(component)] = component

  def get_component(self, component_type):
    """Get a component of the specified type.

    Args:
      component_type (type): The type of the component.

    Returns:
      object: The component of the specified type, or None if not found.
    """    
    return self.components.get(component_type, None)
