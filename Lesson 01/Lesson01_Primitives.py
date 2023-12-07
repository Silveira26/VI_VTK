# Import all VTK modules
from vtkmodules.all import *
import time

# Function to create a cube actor
def createCubeActor(sideLength, position, ren):
    cubeSource = vtkCubeSource()
    cubeSource.SetXLength(sideLength)
    cubeSource.SetYLength(sideLength)
    cubeSource.SetZLength(sideLength)

    cubeMapper = vtkPolyDataMapper()
    cubeMapper.SetInputConnection(cubeSource.GetOutputPort())

    cubeActor = vtkActor()
    cubeActor.SetMapper(cubeMapper)
    cubeActor.SetPosition(position)

    ren.AddActor(cubeActor)
    return cubeActor

# Main function
def main():
    # Renderer
    ren = vtkRenderer()
    #ren.SetBackground(1.0, 1.0, 1.0)  # Set background to white

    # Create cube actors
    createCubeActor(1, (-5,0,0), ren)
    createCubeActor(1, (0,0,-5), ren)
    createCubeActor(1, (5,0,0), ren)
    createCubeActor(1, (0,0,5), ren)

    # Create sphere
    sphereSource = vtkSphereSource()
    sphereSource.SetRadius(2)
    sphereSource.SetThetaResolution(50)
    sphereSource.SetPhiResolution(50)

    # Create a mapper for the sphere
    sphereMapper = vtkPolyDataMapper()
    sphereMapper.SetInputConnection(sphereSource.GetOutputPort())

    # Create an actor for the sphere
    sphereActor = vtkActor()
    sphereActor.SetMapper(sphereMapper)
    ren.AddActor(sphereActor)

    # Create a render window
    renWin = vtkRenderWindow()
    renWin.AddRenderer(ren)
    renWin.SetSize(300, 300) # Default is 300, 300
    renWin.SetWindowName('Sphere and Cubes with Lighting')


    for i in range(0,1000):
        # render the image
        renWin.Render()
        # rotate the active camera by one degree
        ren.GetActiveCamera().Azimuth(1)
        time.sleep(0.01)

if __name__ == '__main__':
    main()