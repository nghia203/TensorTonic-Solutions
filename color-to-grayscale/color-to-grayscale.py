def color_to_grayscale(image):
    """
    Convert an RGB image to grayscale using luminance weights.
    """
    # Write code here
    return [
        [image[i][j][0] * 0.299 + image[i][j][1] * 0.587 + image[i][j][2] * 0.114 for j in range(len(image[0]))]
            for i in range(len(image))
           ]