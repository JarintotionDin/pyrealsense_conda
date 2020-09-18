import os
os_dir = os.__file__
site_packages_dir = os.path.split(os_dir)[:-1]
dir_list = list(site_packages_dir) + ["site-packages", "pyrealsense2"]
install_dir = ""
for dir_ in dir_list:
    install_dir = os.path.join(install_dir, dir_)
source_init = os.path.join("wrappers", "python", "pyrealsense2", "__init__.py")
os.system("sh build.sh")
cmd_cp_str = " ".join(("cp", source_init, install_dir))
print(cmd_cp_str)

