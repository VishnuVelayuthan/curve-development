import numpy as np
import os
import pdb

from PIL import Image
import matplotlib.pyplot as mp;


import pickle

from habitat_sim.utils.data import ImageExtractor, PoseExtractor
import habitat_sim.registry as registry


# Class to extract occupancy grid from mesh scan 
@registry.register_pose_extractor(name="og_conv_pdf")
class InputPoseExtractor(PoseExtractor):
    # view is the occupancy grid
    # fp is the file path
    # need to return an array of poses   
    #   pose = (point on map, point to direct, fp)
    def extract_poses(self, view, fp):

        var_file = open(".var-file.txt", "r") 
        output_fp = var_file.read() 

        pickle.dump(view, open(output_fp, "wb"))

        return [ ( (0,0), (0,1), fp ) ] # Dummy value 


def get_pkl_of_occ_grid(scene_fp, output_fp):

    
    var_file = open(".var-file.txt", "w")
    var_file.write(output_fp)
    var_file.close();

    extractor = ImageExtractor(
        scene_fp,
        img_size=(512, 512),
        output=["rgba", "depth", "semantic"],
        pose_extractor_name="og_conv_pdf",
        split=(100,0)
    )

    os.remove(".var-file.txt")
    extractor.close()


def get_img_of_occ_grid(pkl_fp, output_fp):
    og_file = open(pkl_fp, "rb")
    og_view = pickle.load(og_file)
    og_file.close()

    mp.imshow(og_view)
    mp.savefig(output_fp)


def get_occ_grid_pkl_img(scene_fp, pkl_output_fp, img_output_fp):
    get_occ_grid_pkl(scene_fp, pkl_output_fp)
    get_img_of_occ_grid(pkl_output_fp, img_output_fp)


if __name__ == "__main__" :
    get_occ_grid_pkl_img("../data/apartment_1.glb", "./og-var-apartment_1.pkl", "./og-img-apartment_1.jpg")

