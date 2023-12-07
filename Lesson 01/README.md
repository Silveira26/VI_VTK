# VTK Lesson 01

This README accompanies the Python scripts for the first lesson in VTK, providing context and highlighting differences between the implementation in code .

## Primitives.py

This script demonstrates the creation of basic VTK primitives, including a sphere (`vtkSphereSource`) and cubes (`vtkCubeSource`). While the report discusses the rendering of various primitives and the ability to change the render window's size, this script specifically instantiates the primitives corresponding to the light sources used in the later lessons.

## Interaction.py

Aligning with the Interaction section of the report, this script adds a render window interactor (`vtkRenderWindowInteractor`) to facilitate user interaction with the rendered scene. The script enables the user to rotate, pan, and zoom into the scene using mouse controls, as well as to use specific keys to change the rendering mode, which is in direct correspondence with the described interactions in the report.

## Camera.py

Corresponding to the Camera Control section of the report, this script modifies the camera's position to provide a top-down view of the primitives. The script showcases the use of `GetActiveCamera()` and sets the camera to an orthographic projection by enabling `ParallelProjectionOn()`, which is in line with the report's explanation of camera control for an undistorted view.

## Lighting.py

In this script, the lighting setup is detailed, with multiple light sources added to the scene. This is consistent with the Lighting section of the report, where the function `activateLight` is used to activate and position lights. However, the script goes further by actually implementing these lights within the scene, a practical demonstration that complements the theoretical description in the report.

## Actor.py

This script focuses on modifying actor properties, particularly turning off the default lighting to maintain the color integrity of the cubes representing the light sources. The report's section on Actor properties discusses the potential modifications of an actor's appearance, and this script provides a practical example of how to implement these changes.

