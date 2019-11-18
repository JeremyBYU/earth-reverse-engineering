import math
import trimesh
import argparse
import numpy as np
from pathlib import Path
import ipdb

def parse_args():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-f', '--file', metavar='N', type=str, help='Obj File')
    args = parser.parse_args()
    return args

def save_as_glb(obj_file_path, mesh, gltf=False):
    p = Path(obj_file_path)
    suffix = '.gltf' if gltf else '.glb'
    p = p.with_suffix(suffix)
    mesh.export(str(p))

def get_rotatation_matrix(origin):
    radius = np.linalg.norm(origin)
    lat = np.arcsin(origin[2] / radius)
    lon = np.arctan2(origin[1], origin[0])

    sin_lat = np.sin(lat)
    cos_lat = np.cos(lat)
    sin_lon = np.sin(lon)
    cos_lon = np.cos(lon)

    Rz = np.array([[cos_lon, sin_lon, 0, 0], [-sin_lon, cos_lon, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    Ry = np.array([[cos_lat, 0, sin_lat, 0], [0, 1, 0, 0], [-sin_lat, 0, cos_lat, 0], [0, 0, 0, 1]])

    sin_90 = np.sin(-math.radians(90))
    cos_90 = np.cos(-math.radians(90))
    Rf = np.array([[cos_90, sin_90, 0, 0], [-sin_90, cos_90, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    # print(lat, math.degrees(lat), lon, math.degrees(lon) )
    # Rz = np.eye(4)
    # Ry = np.eye(4)
    R = Rf @ Ry @ Rz

    return R

def get_mesh_mean(mesh_obj):
    return np.mean(np.mean(mesh_obj.triangles,axis=0), axis=0)

def translate_scene(mesh, mesh_min):
    for key, geom in mesh.geometry.items():
        geom.apply_translation(-mesh_min)

def rotate_scene(mesh, rotation_matrix):
    for key, geom in mesh.geometry.items():
        geom.apply_transform(rotation_matrix)

def scale_obj(obj_file_path):
    mesh = trimesh.load_mesh(obj_file_path)
    mesh_min = get_mesh_mean(mesh)
    rot_matrix = get_rotatation_matrix(mesh_min)
    print("Mean Value of Mesh: ", mesh_min)
    translate_scene(mesh, mesh_min)
    rotate_scene(mesh,rot_matrix)
    # mesh.show()
    save_as_glb(obj_file_path, mesh)


def main():
    args = parse_args()
    scale_obj(args.file)
    # convert_obj_to_glb(args.file)

if __name__ == "__main__":
    main()