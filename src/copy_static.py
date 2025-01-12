import os
import shutil

def copy_dir_to_new_dir(rel_src_dir_path: str, relative_dest_dir_path: str):
    if os.path.exists(relative_dest_dir_path):
        shutil.rmtree(relative_dest_dir_path)
    os.mkdir(relative_dest_dir_path)


    dir_raw_contents = os.listdir(rel_src_dir_path)
    dir_content_paths = []
    for thing in dir_raw_contents:
        dir_content_paths.append(os.path.join(rel_src_dir_path, thing))

    for i in range(len(dir_content_paths)):
        current_dir_item = dir_content_paths[i]

        if os.path.isfile(current_dir_item):
            shutil.copy(current_dir_item, relative_dest_dir_path)
            continue

        new_dest_dir_path = os.path.join(relative_dest_dir_path, dir_raw_contents[i])
        copy_dir_to_new_dir(current_dir_item, new_dest_dir_path)

    return 0

