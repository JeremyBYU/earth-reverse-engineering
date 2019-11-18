import trimesh
import argparse
from pathlib import Path

def parse_args():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-f', '--file', metavar='N', type=str, help='Obj File')
    args = parser.parse_args()
    return args

def convert_obj_to_glb(obj_file_path, gltf=False):
    mesh = trimesh.load_mesh(obj_file_path)
    p = Path(args.file)
    suffix = '.gltf' if gltf else '.glb'
    p = p.with_suffix(suffix)
    mesh.export(str(p))

def main():
    args = parse_args()
    convert_obj_to_glb(args.file)

if __name__ == "__main__":
    main()