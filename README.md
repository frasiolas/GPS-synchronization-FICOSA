# GPS synchronization tool (FICOSA)

## Outputs of the tool:
*__4 csv files__ with 2 rows each file each corresponding to 1 of the 4 cameras (front,right,left,back) . The first row is the TimestampHDF (GPS) and the second row is the closest frame that it is mapped to.
*__colmap folder__ that contains images.txt, cameras.txt, points3D.txt. These are needed in order to load the sparse model in colmap. 

## How to run the tool:

`python GPS_sync.py --main-folder <path_to_main_folder> --folder-cam <path_to_camera_folder> --total-frames <number_of_frames> --threshold-min <minimum_threshold> --threshold-max <maximum_threshold> --colmap-path <path_to_colmap_output_file>`

