cmake_minimum_required(VERSION 2.8)
project( Darwin-CV )
find_package( OpenCV REQUIRED )
include_directories( ${OpenCV_INCLUDE_DIRS} )
add_executable( openStream openStream.cpp )
add_executable( faceDetectOP faceDetectOP.cpp)
target_link_libraries(faceDetectOP ${OpenCV_LIBS})
target_link_libraries( openStream ${OpenCV_LIBS} )
