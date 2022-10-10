import numpy as np
import habitat_sim.registry as registry

from ImageExtractor import x, y, theta

from habitat_sim.utils.data import ImageExtractor, PoseExtractor

@registry.register_pose_extractor(name="input_pose_extractor")
class InputPoseExtractor(PoseExtractor):
    def extract_poses(self, view, fp):

        poses = []

        point = (x, y)

        # calculating poi by rotation from looking up the y-axis 
        # using a fixed radius and to rotate from fixed radius
        # need to check if poi can be out of bounds
        # sin(90 - theta) 
        radius = 10
        y_off = 10 * sin(90 - theta)
        x_off = 10 * cos(90 - theta)

        point_of_interest = (x + x_off, y + y_off)

        pose = (point, point_of_interest, fp)

        poses.append(pose)
        return poses


