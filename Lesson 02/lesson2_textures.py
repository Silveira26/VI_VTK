from vtkmodules.all import *

def main():
    # Create a plane source
    planeSource = vtkPlaneSource()
    planeSource.SetOrigin(0.0, 0.0, 0.0)  # Set the origin of the plane
    planeSource.SetPoint1(1.0, 0.0, 0.0)  # SetPoint1 defines the first axis of the plane
    planeSource.SetPoint2(0.0, 1.0, 0.0)  # SetPoint2 defines the second axis of the plane

    # Create a mapper
    planeMapper = vtkPolyDataMapper()
    planeMapper.SetInputConnection(planeSource.GetOutputPort())

    # Create an actor
    planeActor = vtkActor()
    planeActor.SetMapper(planeMapper)

    # Create a texture from an image file
    jpgReader = vtkJPEGReader()
    jpgReader.SetFileName("./images/Lena.jpg")  # Set the file name for the texture image

    # Create a texture and set the jpegReader output as its input
    texture = vtkTexture()
    texture.SetInputConnection(jpgReader.GetOutputPort())

    # Set the texture to the actor
    planeActor.SetTexture(texture)

    # Create a renderer and set the background color
    renderer = vtkRenderer()
    renderer.AddActor(planeActor)
    renderer.SetBackground(0.1, 0.2, 0.3)

    # Create the render window and interactor
    renderWindow = vtkRenderWindow()
    renderWindow.AddRenderer(renderer)

    renderWindowInteractor = vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)

    # Start the interaction
    renderWindow.Render()
    renderWindowInteractor.Initialize()
    renderWindowInteractor.Start()

if __name__ == '__main__':
    main()
