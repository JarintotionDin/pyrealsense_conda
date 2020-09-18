mkdir build

cd build

cmake .. -DCMAKE_BUILD_TYPE=Release -DBUILD_EXAMPLES=False -DBUILD_PYTHON_BINDINGS=bool:true -DPYTHON_EXECUTABLE=$CONDA_PREFIX/bin/python -DCMAKE_INSTALL_PREFIX=$CONDA_PREFIX

cp ../wrappers/python/pyrealsense2/__init__.py ./wrappers/python

make -j4

make install

cd ..
