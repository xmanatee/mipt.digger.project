import cv2
import numpy as np


def resize_to_width(image, width):
  r = 1.0 * width / image.shape[1]
  dim = (width, int(image.shape[0] * r))
  resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
  return resized


def image_concat(images, cells):
  output_dims = (720, 405)
  images_copy = []
  # images_copy.extend(images)
  for image in images:
    resized = cv2.resize(image, output_dims)
    images_copy.append(resized)
  while cells[0] * cells[1] > len(images_copy):
    images_copy.append(images_copy[0])

  vertical_stack = []
  for row in range(cells[0]):
    left = row * cells[1]
    right = left + cells[1]
    vertical_stack.append(np.hstack(images_copy[left: right]))
  compiled_image = np.vstack(vertical_stack)
  return compiled_image
