import trimesh
import numpy as np

# Load the mesh
mesh = trimesh.load('/home/qianru/Projects/TUM/TUM_3/DLinVC/code/4OTex/data/DeformingThings4D/dragon/dragonQKS_act56/meshes/scene.obj')

# Define a rotation matrix for 180 degrees around the x-axis
rotation_matrix = trimesh.transformations.rotation_matrix(
    angle=np.deg2rad(180),  # Convert 180 degrees to radians
    direction=[1, 0, 0],    # Rotation around the x-axis
    point=[0, 0, 0]         # Rotate around origin
)

# Apply the rotation to the mesh
mesh.apply_transform(rotation_matrix)

# Save the transformed mesh back to a new file
mesh.export('/home/qianru/Projects/TUM/TUM_3/DLinVC/code/4OTex/data/DeformingThings4D/dragon/dragonQKS_act56/meshes/scene_rotated.obj')

print("Mesh has been rotated by 180 degrees around the x-axis and saved as 'scene_rotated.obj'.")
