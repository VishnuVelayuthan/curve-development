import numpy as np
import matplotlib.pyplot as plt
import os
import pdb

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
        # pdb.set_trace()

        og_file_name = "og-pdf-" + fp[ 8 : len(fp)-4 ] + ".pkl"
        pickle.dump(view, open( og_file_name , "wb" ))

        return [ ( (0,0), (0,1), fp ) ] # Dummy value 



scene_filepath = "../data/apartment_1.glb"
og_file_name = "og-pdf-" + scene_filepath[ 8 : len(scene_filepath)-4 ] + ".pkl"

extractor = ImageExtractor(
    scene_filepath,
    img_size=(512, 512),
    output=["rgba", "depth", "semantic"],
    pose_extractor_name="og_conv_pdf",
    split=(100,0)
)

og_file = open(og_file_name, "rb")
og_view = pickle.load(og_file)
og_file.close()

print(og_view)


