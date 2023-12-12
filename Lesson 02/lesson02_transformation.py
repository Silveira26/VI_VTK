from vtkmodules.all import *

# Function to create a textured plane actor given a translation and rotation
def create_textured_plane_actor(translation, rotation_angle, rotation_axis, image_file):
    # Create a plane source
    plane = vtkPlaneSource()
    
    # Create a transform that applies the translation and rotation
    transform = vtkTransform()
    transform.Translate(*translation)
    transform.RotateWXYZ(rotation_angle, *rotation_axis)
    
    # Apply the transform using a transform filter
    filter = vtkTransformPolyDataFilter()
    filter.SetTransform(transform)
    filter.SetInputConnection(plane.GetOutputPort())
    
    # Map the transformed plane to a polydata mapper
    mapper = vtkPolyDataMapper()
    mapper.SetInputConnection(filter.GetOutputPort())
    
    # Create a texture from the given image file
    texture = vtkTexture()
    reader = vtkJPEGReader()
    reader.SetFileName(image_file)
    texture.SetInputConnection(reader.GetOutputPort())
    
    # Create an actor for the plane and set its mapper and texture
    actor = vtkActor()
    actor.SetMapper(mapper)
    actor.SetTexture(texture)
    
    return actor

def main():
    # Define translations and rotations for each plane of the cube
    plane_definitions = [
        ((0.0, 0.0, 0.5), 0, (1, 0, 0)),   # Front face
        ((0.0, 0.0, -0.5), 180, (1, 0, 0)), # Back face
        ((-0.5, 0.0, 0.0), 90, (0, 1, 0)),  # Left face
        ((0.5, 0.0, 0.0), -90, (0, 1, 0)),  # Right face
        ((0.0, 0.5, 0.0), 90, (1, 0, 0)),   # Top face
        ((0.0, -0.5, 0.0), -90, (1, 0, 0)), # Bottom face
    ]

    # Create a renderer and window
    renderer = vtkRenderer()
    render_window = vtkRenderWindow()
    render_window.AddRenderer(renderer)
    interactor = vtkRenderWindowInteractor()
    interactor.SetRenderWindow(render_window)

    # Add each plane actor to the renderer
    for i, (translation, rotation_angle, rotation_axis) in enumerate(plane_definitions):
        image_file = f"./images/Im{i+1}.jpg"  # Replace with your image path
        actor = create_textured_plane_actor(translation, rotation_angle, rotation_axis, image_file)
        renderer.AddActor(actor)

    # Set up the render window and interactor
    renderer.SetBackground(0.1, 0.1, 0.1)  # Background color
    render_window.SetSize(400, 400)  # Set the window size

    # Start the interaction
    interactor.Initialize()
    render_window.Render()
    interactor.Start()

if __name__ == '__main__':
    main()
