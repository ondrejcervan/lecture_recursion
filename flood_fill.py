import matplotlib.pyplot as plt

def flood_fill(image, x, y):
    if x < 0 or x >= image.shape[0] or y < 0 or y >= image.shape[1] or image[x, y] != 1:
        return image

    image[x, y] = 2

    flood_fill(image, x+1, y)
    flood_fill(image, x-1, y)
    flood_fill(image, x, y+1)
    flood_fill(image, x, y-1)

    return image

def main():
    # img = plt.imread("files/img0.png")[:, :, 0]
    img = plt.imread("files/img1.png")[:, :, 0]
    # img = plt.imread("files/img2.png")[:, :, 0]

    filled_img = flood_fill(img, 0, 0)

    plt.imshow(filled_img, cmap="gray")
    plt.show(block=False)
    plt.pause(5)
    plt.clf()

if __name__ == "__main__":
    main()