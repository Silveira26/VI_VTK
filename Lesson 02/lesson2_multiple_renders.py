from vtkmodules.all import *

def main():
    # Create the cone source
    coneSource = vtkConeSource()
    coneSource.SetResolution(60)

    coneMapper = vtkPolyDataMapper()
    coneMapper.SetInputConnection(coneSource.GetOutputPort())

    coneActor = vtkActor()
    coneActor.SetMapper(coneMapper)

    # First Renderer
    ren1 = vtkRenderer()
    ren1.AddActor(coneActor)
    ren1.SetBackground(0.1, 0.2, 0.4)  # Set the background color for the first renderer
    ren1.SetViewport(0.0, 0.0, 0.5, 1.0)  # Set the viewport for the left half of the window

    # Second Renderer
    ren2 = vtkRenderer()
    ren2.AddActor(coneActor)
    ren2.SetBackground(0.2, 0.3, 0.4)  # Set a different background color for distinction
    ren2.SetViewport(0.5, 0.0, 1.0, 1.0)  # Set the viewport for the right half of the window

    # Modify the camera position for the second renderer
    camera2 = vtkCamera()
    camera2.Azimuth(90)  # Rotate 90 degrees around the view-up vector
    ren2.SetActiveCamera(camera2)
    ren2.ResetCamera()

    # Render Window
    renWin = vtkRenderWindow()
    renWin.AddRenderer(ren1)
    renWin.AddRenderer(ren2)
    renWin.SetSize(600, 300)  # Set the window size to 600x300 pixels
    renWin.SetWindowName('Multiple Renderers - Cone Example')

    # Interactor
    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)

    # Start the interaction
    iren.Initialize()
    iren.Start()

if __name__ == '__main__':
    main()