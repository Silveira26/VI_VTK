import vtk
from vtkmodules.vtkCommonCore import vtkPoints
from vtkmodules.vtkCommonDataModel import vtkUnstructuredGrid, VTK_VERTEX
from vtkmodules.vtkRenderingCore import vtkDataSetMapper, vtkActor


def main():
    # Create a vtkFloatArray to hold vector data and set the number of components
    vectors = vtk.vtkFloatArray()
    vectors.SetNumberOfComponents(3)
    vectors.SetName("Vectors")

    # Insert vector data into the vtkFloatArray
    vectors.InsertTuple3(0, 1, 0, 0)
    vectors.InsertTuple3(1, 0, 1, 0)
    vectors.InsertTuple3(2, 0, 0, 1)
    vectors.InsertTuple3(3, 1, 1, 1)

    # Create a vtkFloatArray to hold scalar data
    scalars = vtk.vtkFloatArray()
    scalars.SetName("Scalars")

    # Insert scalar data into the vtkFloatArray
    scalars.InsertTuple1(0, 0.1)
    scalars.InsertTuple1(1, 0.3)
    scalars.InsertTuple1(2, 0.5)
    scalars.InsertTuple1(3, 0.8)

    # Assume 'ugrid' is your vtkUnstructuredGrid object and associate the vectors and scalars with it
    coords = [[0, 0, 0], [1, 0, 0], [0.5, 1, 0], [0.5, 0.5, 1]]
    ugrid = vtkUnstructuredGrid()
    points = vtkPoints()
    
    for i in range(len(coords)):
        points.InsertNextPoint(coords[i])

    # Cell type changed to VTK_VERTEX
    for i in range(len(coords)):
        ugrid.InsertNextCell(VTK_VERTEX, 1, [i])

    ugrid.SetPoints(points)

    # Mapper and actor
    UGriMapper = vtkDataSetMapper()
    UGriMapper.SetInputData(ugrid)

    ugridActor = vtkActor()
    ugridActor.SetMapper(UGriMapper)

    # Modify properties of the actor
    ugridActor.GetProperty().SetColor(1, 0, 0)  # Set color to red
    ugridActor.GetProperty().SetPointSize(5)


    ugrid.GetPointData().SetVectors(vectors)
    ugrid.GetPointData().SetScalars(scalars)

    # Create a cone source
    coneSource = vtk.vtkConeSource()

    # Create a glyph3D object to visualize each vector with a cone
    glyph = vtk.vtkGlyph3D()
    glyph.SetSourceConnection(coneSource.GetOutputPort())
    glyph.SetInputData(ugrid)
    glyph.SetVectorModeToUseVector()
    glyph.SetScaleModeToScaleByVector()
    glyph.SetColorModeToColorByScalar()
    glyph.OrientOn()
    glyph.ScalingOn()

    # Create a mapper and actor
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(glyph.GetOutputPort())
    mapper.SetScalarModeToUsePointData()

    actor = vtk.vtkActor()
    actor.SetMapper(mapper)

    # Create a renderer, render window, and interactor
    renderer = vtk.vtkRenderer()
    renderWindow = vtk.vtkRenderWindow()
    renderWindow.AddRenderer(renderer)
    renderWindowInteractor = vtk.vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)

    # Add the actor to the renderer
    renderer.AddActor(actor)
    renderer.SetBackground(1, 1, 1)  # White background

    # Render and interact
    renderWindow.Render()
    renderWindowInteractor.Start()

if __name__ == '__main__':
    main()
