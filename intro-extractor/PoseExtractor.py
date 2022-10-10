import numpy as np
import habitat_sim.registry as registry

from habitat_sim.utils.data import ImageExtractor, PoseExtractor

@registry.register_pose_extractor(name="random_pose_extractor")
class RandomPoseExtractor(PoseExtractor):
    def extract_poses(self, view, fp):
        height, width = view.shape
        num_random_points = 4
        points = []
        while len(points) < num_random_points:
            # Get the row and column of a random point on the topdown view
            row, col = np.random.randint(0, height), np.random.randint(0, width)

            # Convenient method in the PoseExtractor class to check if a point
            # is navigable
            if self._valid_point(row, col, view):
                points.append((row, col))

        poses = []

        # Now we need to define a "point of interest" which is the point the camera will
        # look at. These two points together define a camera position and angle
        for point in points:
            r, c = point
            point_of_interest = (r - 1, c) # Just look forward
            pose = (point, point_of_interest, fp)
            poses.append(pose)

        return poses


