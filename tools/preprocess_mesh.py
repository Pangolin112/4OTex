import trimesh
import os
import numpy as np

mesh_path = './data/DeformingThings4D/dragon/dragonOLO_act17/meshes/scene.obj'
# mesh_path = '/home/qianru/Projects/TUM/TUM_3/DLinVC/code/ObjectTex/data/scenes/93f59740-4b65-4e8b-8a0f-6420b339469d/room_4/meshes/scene.obj'

# Check if the file exists
if not os.path.exists(mesh_path):
    raise FileNotFoundError(f"File not found: {mesh_path}")

# load the mesh
mesh = trimesh.load(mesh_path)

centroid = mesh.centroid

# Calculate the distances of all vertices from the centroid
distances = np.linalg.norm(mesh.vertices - centroid, axis=1)

# Find the maximum distance to cover all vertices
radius = np.max(distances)

# Add a small epsilon to ensure the sphere does not touch the mesh
epsilon = 0.01 * radius  # Adding 1% of the radius
minimum_cover_radius = radius + epsilon

print(f"Geometrical Center of the Bear Mesh: {centroid}")
print(f"Minimum Sphere Radius (not touching): {minimum_cover_radius}")

