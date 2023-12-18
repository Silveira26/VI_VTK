# Import all VTK modules
from vtkmodules.all import *


def main():
    sphereSource = vtkSphereSource()

    # Create a cone source
    coneSource = vtkConeSource()

    # Create a glyph3D object
    glyph = vtkGlyph3D()
    glyph.SetSourceConnection(coneSource.GetOutputPort())
    glyph.SetInputConnection(sphereSource.GetOutputPort())
    glyph.SetVectorModeToUseNormal()
    glyph.SetScaleFactor(0.2)  # Adjust the scale factor as needed

    # Create a mapper and actor for the glyphs
    mapper = vtkPolyDataMapper()
    mapper.SetInputConnection(glyph.GetOutputPort())

    actor = vtkActor()
    actor.SetMapper(mapper)

    # Create a renderer and render window
    renderer = vtkRenderer()
    renderWindow = vtkRenderWindow()
    renderWindow.AddRenderer(renderer)

    # Create a render window interactor
    renderWindowInteractor = vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)

    # Add the actor to the scene
    renderer.AddActor(actor)
    renderer.SetBackground(1, 1, 0.5)  # Set background to white

    # Render and start interaction
    renderWindow.Render()
    renderWindowInteractor.Start()


if __name__ == '__main__':
    main()
