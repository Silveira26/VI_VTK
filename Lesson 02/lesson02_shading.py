from vtkmodules.all import *

# Function to create a sphere actor with specified shading
def create_sphere_actor(shading):
    sphereSource = vtkSphereSource()
    sphereSource.SetThetaResolution(20)
    sphereSource.SetPhiResolution(20)

    sphereMapper = vtkPolyDataMapper()
    sphereMapper.SetInputConnection(sphereSource.GetOutputPort())

    sphereActor = vtkActor()
    sphereActor.SetMapper(sphereMapper)
    
    # Set shading interpolation
    if shading == "Flat":
        sphereActor.GetProperty().SetInterpolationToFlat()
    elif shading == "Gouraud":
        sphereActor.GetProperty().SetInterpolationToGouraud()
    elif shading == "Phong":
        sphereActor.GetProperty().SetInterpolationToPhong()
    # If shading is "None", don't change the interpolation (use default)

    return sphereActor

# Function to create a renderer with specified properties and add a subtitle
def create_renderer(actor, background_color, viewport, subtitle):
    renderer = vtkRenderer()
    renderer.AddActor(actor)
    renderer.SetBackground(background_color)
    renderer.SetViewport(viewport)
    
    # Create the subtitle text actor
    textActor = vtkTextActor()
    textActor.SetInput(subtitle)
    textActor.GetTextProperty().SetColor(1, 1, 1)  # White text color
    textActor.GetTextProperty().SetFontSize(20)
    textActor.SetPosition(10, 10)  # Lower-left corner of the renderer viewport
    
    # Add the text actor to the renderer
    renderer.AddActor(textActor)
    
    return renderer

def main():
    # Create a render window
    renWin = vtkRenderWindow()
    renWin.SetSize(800, 600)  # Set the window size to 600x300 pixels
    renWin.SetWindowName('Multiple Renderers - Different Shading Spheres')

    # Define background colors for each renderer
    backgrounds = [(0.1, 0.2, 0.3), (0.2, 0.4, 0.6), (1.0, 0.6, 0.4), (0.8, 0.5, 0.3)]

    # Define viewports for each renderer (2x2 grid)
    viewports = [(0.0, 0.5, 0.5, 1.0), (0.5, 0.5, 1.0, 1.0), (0.0, 0.0, 0.5, 0.5), (0.5, 0.0, 1.0, 0.5)]

    # Shading techniques
    shadings = ["Default", "Flat", "Gouraud", "Phong"]
    subtitles = ["Default Shading", "Flat Shading", "Gouraud Shading", "Phong Shading"]

    # Create renderers and add them to the render window
    for i in range(4):
        sphere_actor = create_sphere_actor(shadings[i])
        renderer = create_renderer(sphere_actor, backgrounds[i], viewports[i], subtitles[i])
        renWin.AddRenderer(renderer)

    # Interactor
    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)

    # Start the interaction
    iren.Initialize()
    iren.Start()

if __name__ == '__main__':
    main()
