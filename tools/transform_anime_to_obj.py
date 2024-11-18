import numpy as np
import os


def anime_read(filename):
    """
    Read the .anime file and extract animation data.

    :param filename: Path of the .anime file
    :return: nf, nv, nt, vert_data, face_data, offset_data
    """
    with open(filename, 'rb') as f:
        nf = np.fromfile(f, dtype=np.int32, count=1)[0]
        nv = np.fromfile(f, dtype=np.int32, count=1)[0]
        nt = np.fromfile(f, dtype=np.int32, count=1)[0]
        vert_data = np.fromfile(f, dtype=np.float32, count=nv * 3)
        face_data = np.fromfile(f, dtype=np.int32, count=nt * 3)
        offset_data = np.fromfile(f, dtype=np.float32, count=-1)

        if len(offset_data) != (nf - 1) * nv * 3:
            raise ValueError("Data inconsistent error!", filename)

        vert_data = vert_data.reshape((-1, 3))
        face_data = face_data.reshape((-1, 3))
        offset_data = offset_data.reshape((nf - 1, nv, 3))

    return nf, nv, nt, vert_data, face_data, offset_data


def export_obj(filename, vertices, faces):
    """
    Export mesh data to an OBJ file.

    :param filename: Path to save the OBJ file
    :param vertices: Vertex data (list of tuples)
    :param faces: Face data (list of tuples)
    """
    with open(filename, 'w') as f:
        for v in vertices:
            f.write(f'v {v[0]} {v[1]} {v[2]}\n')
        for face in faces:
            f.write(f'f {face[0] + 1} {face[1] + 1} {face[2] + 1}\n')


def extract_and_export_frames(anime_file_path, output_dir):
    """
    Extract frames from the .anime file and export each as an OBJ file.

    :param anime_file_path: Path to the .anime file
    :param output_dir: Directory to save the extracted OBJ files
    """
    # Read the anime file
    nf, nv, nt, vert_data, face_data, offset_data = anime_read(anime_file_path)

    # Ensure output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Export the first frame
    export_obj(os.path.join(output_dir, 'frame_0000.obj'), vert_data, face_data)

    # Export subsequent frames by applying offsets
    for frame_id in range(1, nf):
        current_vertices = vert_data + offset_data[frame_id - 1]
        export_obj(os.path.join(output_dir, f'frame_{frame_id:04d}.obj'), current_vertices, face_data)


# Example usage
anime_file_path = '/home/qianru/Projects/TUM/TUM_3/DLinVC/code/4OTex/data/DeformingThings4D/dragon/dragonQKS_act56/dragonQKS_act56.anime'
output_dir = '/home/qianru/Projects/TUM/TUM_3/DLinVC/code/4OTex/data/DeformingThings4D/dragon/dragonQKS_act56/extracted_frames'
extract_and_export_frames(anime_file_path, output_dir)
