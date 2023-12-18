from vtkmodules.all import (
    vtkConeSource, vtkPolyDataMapper, vtkActor, vtkRenderer, vtkRenderWindow,
    vtkRenderWindowInteractor, vtkCommand, vtkTextMapper, vtkActor2D, vtkPointPicker
)
from vtkmodules.vtkFiltersCore import vtkGlyph3D
from vtkmodules.vtkFiltersSources import vtkSphereSource


# Callback class for interaction
class vtkMyCallback:
    def __init__(self, renderer, textMapper, textActor, picker, actor):
        self.ren = renderer
        self.tMapper = textMapper
        self.tActor = textActor
        self.picker = picker
        self.actor = actor

    def __call__(self, caller, ev):
        if ev == "KeyPressEvent":
            key = caller.GetKeySym()
            if key == 'l':
                x, y = caller.GetEventPosition()
                self.picker.Pick(x, y, 0, self.ren)

                picked = self.picker.GetPickPosition()
                print("Picked at: {:.3f}, {:.3f}, {:.3f}".format(*picked))

                # Update the TextMapper with the picked coordinates
                self.tMapper.SetInput("Picked at: {:.3f}, {:.3f}, {:.3f}".format(*picked))

                # Position the text actor slightly above the picked position
                self.tActor.SetPosition(x, y + 20)

                # Make the actor visible
                self.tActor.VisibilityOn()
                self.ren.Render()
            if key=='p':
                x, y, z = self.picker.GetPickPosition()
                print(f"Picked point coordinates: ({x}, {y}, {z})")
                self.actor.SetPosition(x, y, z)
                self.actor.VisibilityOn()


def main():
    # Create a sphere source
    sphereSource = vtkSphereSource()
    sphereSource.SetThetaResolution(12)
    sphereSource.SetPhiResolution(12)

    # Create a cone source
    coneSource = vtkConeSource()

    # Create a glyph3D object
    glyph = vtkGlyph3D()
    glyph.SetSourceConnection(coneSource.GetOutputPort())
    glyph.SetInputConnection(sphereSource.GetOutputPort())
    glyph.SetVectorModeToUseNormal()
    glyph.SetScaleFactor(0.2)

    # Create a mapper and actor for the glyphs
    mapper = vtkPolyDataMapper()
    mapper.SetInputConnection(glyph.GetOutputPort())

    glyphActor = vtkActor()
    glyphActor.SetMapper(mapper)

    # Create a mapper and actor for the indicator sphere
    indicatorSphereSource = vtkSphereSource()
    indicatorSphereSource.SetRadius(0.05)  # Small radius for the indicator sphere

    indicatorMapper = vtkPolyDataMapper()
    indicatorMapper.SetInputConnection(indicatorSphereSource.GetOutputPort())

    indicatorActor = vtkActor()
    indicatorActor.SetMapper(indicatorMapper)
    indicatorActor.VisibilityOff()  # Start with the indicator sphere invisible

    # Create a renderer and render window
    renderer = vtkRenderer()
    renderWindow = vtkRenderWindow()
    renderWindow.AddRenderer(renderer)

    # Create a render window interactor
    renderWindowInteractor = vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)

    # Add the actors to the scene
    renderer.AddActor(glyphActor)
    renderer.AddActor(indicatorActor)
    renderer.SetBackground(0.5, 0.5, 1)

    # Create a text mapper and actor for displaying coordinates
    textMapper = vtkTextMapper()
    tprop = textMapper.GetTextProperty()
    tprop.SetFontFamilyToCourier()
    tprop.BoldOn()
    tprop.SetFontSize(24)
    tprop.SetJustificationToCentered()

    textActor = vtkActor2D()
    textActor.SetMapper(textMapper)
    textActor.VisibilityOff()

    # Add text actor to the renderer
    renderer.AddActor(textActor)

    # Create a render window
    renWin = vtkRenderWindow()
    renWin.AddRenderer(renderer)

    # Create a render window interactor
    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)

    myPicker = vtkPointPicker()

    # Set up the observer with the callback
    mo1 = vtkMyCallback(renderer, textMapper, textActor, myPicker, indicatorActor)
    iren.AddObserver(vtkCommand.KeyPressEvent, mo1)

    # Start the interaction
    iren.Initialize()
    renWin.Render()
    iren.Start()


if __name__ == '__main__':
    main()
