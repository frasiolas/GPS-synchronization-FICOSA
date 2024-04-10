# GPS synchronization tool (FICOSA)

## How to run the tool:
1. Run to rename and crop the images.
   
`python crop_rename --source-folder /path/to/source/folder --target-folder /path/to/target/folder --crop-left 0 --crop-upper 0 --crop-right 968 --crop-lower 600`

2. Run to create the csv files and the colmap folder
   
`python GPS_sync.py --main-folder <path_to_main_folder> --folder-cam <path_to_camera_folder> --total-frames <number_of_frames> --threshold-min <minimum_threshold> --threshold-max <maximum_threshold> --colmap-path <path_to_colmap_output_file>`

### crop_rename
* source-folder: Path to the source folder containing images
* target-folder: Path to the target folder to save cropped images
* crop-left: Left coordinate of the crop box
* crop-upper: Upper coordinate of the crop box
* crop-right: Right coordinate of the crop box
* crop-lower: Lower coordinate of the crop box


## Outputs of the tool:
* __4 csv files__ (0_cam, 1_cam, 2_cam, 3_cam) each corresponding to 1 of the 4 cameras (front,right,left,back).
  
  ![Example of csv file](csv_example.png)
* __colmap folder__ that contains images.txt, cameras.txt, points3D.txt. These are needed in order to load the sparse model in colmap. 


