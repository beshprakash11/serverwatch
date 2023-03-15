import os, shutil
dst_path = "/home/arrtsm-blackbox2/Documents/mynfs/GCodeServer"
source1 = "/home/arrtsm-blackbox2/Documents/detectron2/lengemann/Lengeman/BTLX_final/BTLX_final/progress"
contents = os.listdir(source1)
for item in contents:
    if os.path.isdir(os.path.join(source1, item)):
        if os.path.isdir(os.path.join(source1, item + "/gcode")):
            print("Gcode Exist")
        if os.path.exists(dst_path + item + "/gcode"):
            print("Code alread exit")
        else:
            src_path_gcode = os.path.join(source1, item + "/gcode")
            dst_path_gcode = os.path.join(dst_path, item + "/gcode")
            shutil.copytree(src_path_gcode, dst_path_gcode)
            print("GCode copy completed")

        if os.path.exists(dst_path + item + "/suction_cups"):
            print("Suction cup exist")
        else:
            src_path_scup = os.path.join(source1, item + "/suction_cups")
            dst_path_scup = os.path.join(dst_path, item + "/suction_cups")
            shutil.copytree(src_path_scup, dst_path_scup)
            print("SCup copy completed")