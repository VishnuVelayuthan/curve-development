import numpy as np
import habitat_sim.registry as registry
from math import sin, cos

# from ImageExtractor import x, y, theta

from habitat_sim.utils.data import ImageExtractor, PoseExtractor

@registry.register_pose_extractor(name="input_pose_extractor")
class InputPoseExtractor(PoseExtractor):
    # view is the occupancy grid
    # fp is the file path
    # need to return an array of poses   
    #   pose = (point on map, point to direct, fp)
    def extract_poses(self, view, fp):

        poses = []

        # x, y  theta = map(lambda x: int(x), input("Input x y theta: ").split(" "))

        var_file = open("var-file.txt", "r")

        x, y, theta = map(lambda x: int(x), var_file.read().split(" "))
        
        var_file.close();

        point = (x, y)

        # calculating poi by rotation from looking up the y-axis 
        # using a fixed radius and to rotate from fixed radius
        # need to check if poi can be out of bounds
        #  though, in theory it should not matter whether it's out of bounds or noT 
        # sin(90 - theta) 
        radius = 10
        y_off = radius * sin(90 + theta)
        x_off = radius * cos(90 + theta)

        point_of_interest = (int(x - x_off), int(y - y_off))

        if self._valid_point(x, y, view):
            pose = (point, point_of_interest, fp)
        else :
            pose = ( (0,0) , (0,-10) , fp)

        poses.append(pose)

        return poses


