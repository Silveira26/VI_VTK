from vtkmodules.all import *

# Callback class for interaction
class vtkMyCallback:
    def __init__(self, renderer):
        self.ren = renderer

    def __call__(self, caller, ev):
        print(caller.GetClassName(), 'Event Id:', ev)
        camera_position = self.ren.GetActiveCamera().GetPosition()
        print("Camera Position: %f, %f, %f" % camera_position)

def main():
    # Create a cone source
    coneSource = vtkConeSource()
    coneSource.SetResolution(60)

    # Create a mapper
    coneMapper = vtkPolyDataMapper()
    coneMapper.SetInputConnection(coneSource.GetOutputPort())

    # Create an actor
    coneActor = vtkActor()
    coneActor.SetMapper(coneMapper)

    # Create a renderer
    ren = vtkRenderer()
    ren.AddActor(coneActor)
    ren.SetBackground(0.1, 0.2, 0.3)

    # Create a render window
    renWin = vtkRenderWindow()
    renWin.AddRenderer(ren)

    # Create a render window interactor
    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)

    # Set up the observer with the callback
    mo1 = vtkMyCallback(ren)
    ren.AddObserver(vtkCommand.ResetCameraEvent, mo1)

    # Start the interaction
    iren.Initialize()
    renWin.Render()
    iren.Start()

if __name__ == '__main__':
    main()
