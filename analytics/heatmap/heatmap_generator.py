import numpy as np
import json
import cv2
import sys

store_name = sys.argv[1]

if store_name == "store1":
    layout_path = "layouts/Store 1 - layout.png"

elif store_name == "store2":
    layout_path = "layouts/store 2 - layout.png"

else:
    layout_path = "data/Store 1/Store 1 - layout.png"

layout = cv2.imread(layout_path)

if layout is None:
    print("Store layout image not found")
    exit()

with open(
    "data/output/heat_points.json",
    "r"
) as f:
    points = json.load(f)

heat_layer = np.zeros(
    (layout.shape[0], layout.shape[1]),
    dtype=np.float32
)

for x, y in points:

    if (
        0 <= x < layout.shape[1]
        and
        0 <= y < layout.shape[0]
    ):

        cv2.circle(
            heat_layer,
            (x, y),
            40,
            1,
            -1
        )

heat_layer = cv2.GaussianBlur(
    heat_layer,
    (0, 0),
    25
)

heat_layer = cv2.normalize(
    heat_layer,
    None,
    0,
    255,
    cv2.NORM_MINMAX
)

heat_layer = heat_layer.astype(np.uint8)

colored_heatmap = cv2.applyColorMap(
    heat_layer,
    cv2.COLORMAP_JET
)

final = cv2.addWeighted(
    layout,
    0.6,
    colored_heatmap,
    0.4,
    0
)

cv2.putText(
    final,
    f"Store: {store_name}",
    (20, 40),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (255, 255, 255),
    2
)

cv2.imwrite(
    "data/output/store_heatmap.jpg",
    final
)

print("Real heatmap generated successfully")