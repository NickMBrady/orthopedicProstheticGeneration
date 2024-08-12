import cv2
import numpy as np

def scale_down(image):
    height , width = image.shape[:2]
    new_width = int(width* 0.5)
    new_height = int(height*0.5)
    resized_image = cv2.resize(image, (new_width, new_height))
    x_offset = (width - new_width) //2
    y_offset = (height-new_height) //2
    result = np.full_like(image, (255,255,255), dtype=np.unit8)
    result[y_offset:y_offset + new_height, x_offset:x_offset + new_width] = resized_image
    return result

def rotate(image, contour):
    rect = cv2.minAreaRect(contour)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    side_lengths = [np.linalg.norm(box[i] - box[(i + 1) % 4]) for i in range(4)]
    angle = rect[2] + 180
    width, height = image.shape[1], image.shape[0]
    rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), angle, 1.0)
    rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))
    return rotated_image

def find_paper(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)
    contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    largest_contour = max(contours, key=cv2.contourArea)
    epsilon = 0.05 * cv2.arcLength(largest_contour, True)
    approx = cv2.approxPolyDP(largest_contour, epsilon, True)
    return approx

def warp_paper(image, paper_corners):
    target_width = 8.5 * 300
    target_height = 11 * 300
    target_corners = np.array([[0, 0], [target_width, 0], [target_width, target_height], [0, target_height]], dtype=np.float32)
    paper_corners = paper_corners.astype(np.float32)
    matrix = cv2.getPerspectiveTransform(paper_corners, target_corners)
    warped = cv2.warpPerspective(image, matrix, (int(target_width), int(target_height)))
    return warped

def extract_outline_on_paper(image):
    height, width, channels = image.shape
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.blur(gray, (5, 5))
    binary_mask = cv2.inRange(blurred, 0, 150)
    contours, _ = cv2.findContours(binary_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    rgb_image = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    rgb_image = cv2.drawContours(rgb_image, contours, -1, (0, 255, 0), thickness= 20)
    cv2.imshow("first pass", rgb_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    blank = np.zeros((height, width, 1), dtype=np.uint8)
    blank = cv2.drawContours(blank, contours, -1, (255, 255, 255), thickness= cv2.FILLED)
    blank = cv2.blur(blank, (100,100))
    blank = cv2.blur(blank, (100,100))
    cv2.imshow("second pass", blank)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    mask2 = cv2.inRange(blank, 100, 255)
    cv2.imshow("second pass threshold", mask2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    contours2, _ = cv2.findContours(mask2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours2) > 1:
        contours2 = max(contours2, key=cv2.contourArea)
    outline = np.zeros_like(image)
    cv2.drawContours(outline, contours2, -1, (0, 0, 255), 2)
    contour = contours2[0]
    rotated_image = rotate(outline, contour)
    return rotated_image

image = cv2.imread("IMG_2586.jpeg")
image_with_edges = image.copy()
paper_corners = find_paper(image)
if len(paper_corners) == 4:
    cv2.drawContours(image_with_edges, [paper_corners], -1, (0, 255, 0), 2)
    cv2.imshow("Original Image with Edges", image_with_edges)
    cv2.waitKey(0)
    target_size = (int(8.5 * 300), int(11 * 300))
    warped_paper = warp_paper(image, paper_corners)
    # warped_paper = scale_down(warped_paper)
    cv2.imshow("Warped Paper", warped_paper)
    cv2.waitKey(0)
    outline_image = extract_outline_on_paper(warped_paper)
    cv2.imshow("Extracted Outline", outline_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    gray = cv2.cvtColor(outline_image, cv2.COLOR_BGR2GRAY)
    _, thresholded = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        print(f"width={w}, height={h}")
else:
    print("Paper not found or cannot be approximated as a rectangle.")

