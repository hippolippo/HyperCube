from UI import UI
from manager import Manager

ui = UI()
manager = Manager(ui)
ui.draw_2D_Mesh(manager.mesh)
ui.start()
