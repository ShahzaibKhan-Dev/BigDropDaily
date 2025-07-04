from ._anvil_designer import Form1Template
from anvil import *
import plotly.graph_objects as go

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def Username(self, **event_args):
    """This method is called when the TextBox loses focus"""

  def text_box_3_lost_focus(self, **event_args):
    """This method is called when the TextBox loses focus"""
    pass

  def rich_text_1_show(self, **event_args):
    """This method is called when the RichText is shown on the screen"""
    pass

  def text_box_4_show(self, **event_args):
    """This method is called when the TextBox is shown on the screen"""
    pass
     
