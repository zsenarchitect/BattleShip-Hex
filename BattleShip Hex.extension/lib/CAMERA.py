from pyrevit import UI, DB
from pyrevit import script, revit, forms
from time import sleep
import BOARD

def pause_view(seconds = 2):
    sleep(int(seconds))

def set_view(team, type = "3d"):
    """type = 3d, 2d plan, draft view for transition"""

    view_name = "{}_main_{}".format(type, team)
    view = get_view_by_name(view_name)
    revit.uidoc.ActiveView = view
    revit.uidoc.RefreshActiveView()
    zoom_to_boards()
    #sleep(3)

def return_to_title_screen():
    view = get_view_by_name("Title Screen")
    revit.uidoc.ActiveView = view
    revit.uidoc.RefreshActiveView()

def go_to_game_over_view():
    view = get_view_by_name("Game Over")
    revit.uidoc.ActiveView = view
    revit.uidoc.RefreshActiveView()

def go_to_view_by_name(name):
    view = get_view_by_name(name)
    revit.uidoc.ActiveView = view
    view_zoom_extend(view)
    revit.uidoc.RefreshActiveView()

def go_to_god_view():
    view = get_view_by_name("god view")
    revit.uidoc.ActiveView = view
    revit.uidoc.RefreshActiveView()



def close_other_view():
    return
    from Autodesk.Revit.UI import RevitCommandId
    import clr
    clr.AddReference('RevitServices')
    from RevitServices.Persistence import DocumentManager
    uiapp = DocumentManager.Instance.CurrentUIApplication
    print uiapp
    cmd = Autodesk.Revit.UI.RevitCommandId.LookupPostableCommandId(PostableCommand.CloseInactiveViews)
    #cmdId = cmd.Id
    uiapp.PostCommand(cmd)


def get_view_by_name(name):
    views = DB.FilteredElementCollector(revit.doc).OfClass(DB.View).WhereElementIsNotElementType().ToElements()
    for view in views:
        if view.Name == name:
            return view

def view_zoom_extend(view):
    return
    all_els = DB.FilteredElementCollector(revit.doc, view.Id).WhereElementIsNotElementType().ToElements()
    revit.uidoc.ShowElements(all_els)
    revit.uidoc.RefreshActiveView()
    return
    print UI, UI.UIView
    UI.UIView.ZoomToFit(UI.UIView)

def zoom_to_player(player):
    #with revit.Transaction("redraw views"):
    revit.uidoc.ShowElements(player)
    revit.uidoc.RefreshActiveView()

def highlight_element(element):
    revit.get_selection().set_to(element)

def zoom_to_board(team):
    tiles = BOARD.get_all_tiles(team)
    element_set = DB.ElementSet()
    for tile in tiles:
        element_set.Insert(tile)
    #print element_set
    zoom_to_player(element_set)
    """
    print UI, UI.UIView,UI.UIView.ViewId
    UI.UIView.Zoom(10)
    """

def zoom_to_boards():
    tiles = BOARD.get_all_tiles()
    element_set = DB.ElementSet()
    for tile in tiles:
        element_set.Insert(tile)
    #print element_set
    zoom_to_player(element_set)
    """
    UI.UIView.Zoom(10)
    """
