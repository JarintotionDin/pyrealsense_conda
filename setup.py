import os

with open("build.sh", "w") as build_sh:
    print("mkdir build")
    build_sh.write("mkdir build\n")

    print("cd build")
    build_sh.write("cd build\n")

    os_dir = os.__file__
    site_packages_dir = os.path.split(os_dir)[:-1]
    dir_list = list(site_packages_dir) + ["site-packages", "pyrealsense2"]
    python_install_dir = ""
    for dir_ in dir_list:
        python_install_dir = os.path.join(python_install_dir, dir_)

    cmake_cmd_str = " ".join(("cmake",
                              "..",
                              "-DCMAKE_BUILD_TYPE=Release",
                              "-DBUILD_EXAMPLES=False",
                              "-DBUILD_PYTHON_BINDINGS=bool:true",
                              os.path.join("-DPYTHON_EXECUTABLE=$CONDA_PREFIX", "bin", "python"),
                              "-DCMAKE_INSTALL_PREFIX=$CONDA_PREFIX",
                              "-DPYTHON_INSTALL_DIR={}".format(python_install_dir)))
    print(cmake_cmd_str)
    build_sh.write(cmake_cmd_str + "\n")

    make_cmd_str = "make -j{}".format(os.cpu_count())
    print(make_cmd_str)
    build_sh.write(make_cmd_str + "\n")

    make_install_str = "make install"
    print(make_install_str)
    build_sh.write(make_install_str + "\n")

    print("cd ..")
    build_sh.write("cd .." + "\n")

    source_init = os.path.join(".", "wrappers", "python", "pyrealsense2", "__init__.py")

    cp_cmd_str = " ".join(("cp", source_init, os.path.join(python_install_dir, "__init__.py")))
    print(cp_cmd_str)
    build_sh.write(cp_cmd_str + "\n")
    build_sh.close()

os.system("sh build.sh")





