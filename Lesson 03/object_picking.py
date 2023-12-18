import vtk

class vtkMyCallback:
    def __init__(self, picker, actor):
        self.picker = picker
        self.actor = actor

    def __call__(self, caller, event):
        x, y, z = self.picker.GetPickPosition()
        print(f"Picked point coordinates: ({x}, {y}, {z})")
        self.actor.SetPosition(x, y, z)
        self.actor.VisibilityOn()

def main():
    # Create a sphere source
    sphereSource = vtk.vtkSphereSource()
    sphereSource.SetThetaResolution(12)
    sphereSource.SetPhiResolution(12)

    # Create a cone source
    coneSource = vtk.vtkConeSource()

    # Create a glyph3D object
    glyph = vtk.vtkGlyph3D()
    glyph.SetSourceConnection(coneSource.GetOutputPort())
    glyph.SetInputConnection(sphereSource.GetOutputPort())
    glyph.SetVectorModeToUseNormal()
    glyph.SetScaleFactor(0.2)

    # Create a mapper and actor for the glyphs
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(glyph.GetOutputPort())

    glyphActor = vtk.vtkActor()
    glyphActor.SetMapper(mapper)

    # Create a mapper and actor for the indicator sphere
    indicatorSphereSource = vtk.vtkSphereSource()
    indicatorSphereSource.SetRadius(0.05)  # Small radius for the indicator sphere

    indicatorMapper = vtk.vtkPolyDataMapper()
    indicatorMapper.SetInputConnection(indicatorSphereSource.GetOutputPort())

    indicatorActor = vtk.vtkActor()
    indicatorActor.SetMapper(indicatorMapper)
    indicatorActor.VisibilityOff()  # Start with the indicator sphere invisible

    # Create a renderer and render window
    renderer = vtk.vtkRenderer()
    renderWindow = vtk.vtkRenderWindow()
    renderWindow.AddRenderer(renderer)

    # Create a render window interactor
    renderWindowInteractor = vtk.vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)

    # Add the actors to the scene
    renderer.AddActor(glyphActor)
    renderer.AddActor(indicatorActor)
    renderer.SetBackground(1, 1, 1)  # White background

    # Initialize a point picker
    myPicker = vtk.vtkPointPicker()
    myPicker.AddObserver("EndPickEvent", vtkMyCallback(myPicker, indicatorActor))
    renderWindowInteractor.SetPicker(myPicker)

    # Render and start interaction
    renderWindow.Render()
    renderWindowInteractor.Start()

if __name__ == '__main__':
    main()