from vtkmodules.all import *

def main():
    # Existing cone creation
    coneSource = vtkConeSource()

    coneMapper = vtkPolyDataMapper()
    coneMapper.SetInputConnection(coneSource.GetOutputPort())

    # First cone actor
    coneActor = vtkActor()
    coneActor.SetMapper(coneMapper)
    # Update properties of the first cone
    coneActor.GetProperty().SetColor(0.2, 0.63, 0.79)
    coneActor.GetProperty().SetDiffuse(0.7)
    coneActor.GetProperty().SetSpecular(0.4)
    coneActor.GetProperty().SetSpecularPower(20)
    coneActor.GetProperty().SetOpacity(0.5)

    # Second cone actor with shared mapper
    coneActor2 = vtkActor()
    coneActor2.SetMapper(coneMapper)
    coneActor2.SetPosition(0, 2, 0)
    # Set properties using vtkProperty
    property2 = vtkProperty()
    property2.SetColor(1.0, 0.3882, 0.2784)
    property2.SetDiffuse(0.7)
    property2.SetSpecular(0.4)
    property2.SetSpecularPower(20)
    property2.SetOpacity(0.5)
    coneActor2.SetProperty(property2)

    # First renderer
    ren1 = vtkRenderer()
    ren1.AddActor(coneActor)
    ren1.SetBackground(0.1, 0.2, 0.4)
    ren1.SetViewport(0.0, 0.0, 0.5, 1.0)

    # Second renderer
    ren2 = vtkRenderer()
    ren2.AddActor(coneActor2)
    ren2.SetBackground(0.2, 0.3, 0.4)
    ren2.SetViewport(0.5, 0.0, 1.0, 1.0)

    # Render window
    renWin = vtkRenderWindow()
    renWin.AddRenderer(ren1)
    renWin.AddRenderer(ren2)
    renWin.SetSize(600, 300)
    renWin.SetWindowName('Cone with Multiple Renderers')

    # Interactor
    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)
    iren.Initialize()
    iren.Start()

if __name__ == '__main__':
    main()
