import os


def resize_in_folder(path: str, sizes: list[int]) \
		-> None:
	"""
	Resizes all images in a specified folder.
	"""

	images: list[str] = os.listdir(path)
	images.remove(__file__.rsplit("\\", 1)[1])
	folder_name: str = path.rsplit("\\", 1)[1].rjust(5, '0')

	for i in range(len(images)):
		for j in range(len(sizes)):
			size: int = sizes[j]
			save_to: str = f"{folder_name}_{i:05d}_{j:05d}.jpg"
			os.system(f"magick {images[i]} -resize {size}x{size}\! {save_to}")

	return


if __name__ == "__main__":
	dir_path = os.path.dirname(os.path.realpath(__file__))
	resize_in_folder(dir_path, [50, 75, 100, 125, 150, 175, 200])
	input()
