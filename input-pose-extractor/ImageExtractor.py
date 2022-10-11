import numpy as np
import matplotlib.pyplot as plt
import InputPoseExtractor 

from habitat_sim.utils.data import ImageExtractor


# For viewing the extractor output
def display_sample(sample):
    img = sample["rgba"]
    depth = sample["depth"]
    semantic = sample["semantic"]

    arr = [img, depth, semantic]
    titles = ["rgba", "depth", "semantic"]
    plt.figure(figsize=(12, 8))
    for i, data in enumerate(arr):
        ax = plt.subplot(1, 3, i + 1)
        ax.axis("off")
        ax.set_title(titles[i])
        plt.imshow(data)

    plt.show()


# Get input for image (x, y, theta)

# x, y, theta = map(lambda x: int(x), input("Input x y theta: ").split(" "))


scene_filepath = "../data/apartment_1.glb"

extractor = ImageExtractor(
    scene_filepath,
    img_size=(512, 512),
    output=["rgba", "depth", "semantic"],
    pose_extractor_name="input_pose_extractor"
)

# Use the list of train outputs instead of the default, which is the full list
# of outputs (test + train)
extractor.set_mode('train')

# Index in to the extractor like a normal python list
sample = extractor[0]

# Or use slicing
display_sample(sample)

# Close the extractor so we can instantiate another one later
# (see close method for detailed explanation)
extractor.close()
