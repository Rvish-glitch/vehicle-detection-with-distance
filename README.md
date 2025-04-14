
ABOUT:
=

• A vehicle recognition project based on opencv-python . 

• It is the classification of vehicle from video and it gives distance from camera . 

• In future , i will add some more features in it.

• Video also can be changed according to your preference in script.py.

Ex: video='video/clear_road.mp4'

![video_screenshot_14 04 2025](https://github.com/user-attachments/assets/566f9829-b8a0-4729-85b7-c056b065031e)


Mathematics Explanation:
=

📌 Function Signature:

<pre> def estimate_distance(y, h, H_img=720, FOV_vert=20, tilt_angle_deg=10, cam_height_m=5): </pre>
y: Top Y-coordinate (in pixels) of the detected object (bounding box).

h: Height (in pixels) of the bounding box.

H_img: Height of the image in pixels (default: 720p).

FOV_vert: Vertical field of view of the camera (in degrees).

tilt_angle_deg: Tilt angle of the camera downwards (from horizontal), in degrees.

cam_height_m: Height of the camera from the ground, in meters.

🧠 Step-by-Step Breakdown
=
✅ Step 1: Calculate the vertical angle from the center of the image to the bottom of the object

<pre> 
 y_bottom = y + h
 alpha = ((y_bottom / H_img) - 0.5) * FOV_vert 
</pre> 
y + h gets the Y-position of the bottom of the object.

(y_bottom / H_img) normalizes that position to a range of 0–1.

Subtracting 0.5 centers the range around 0 (i.e., image center = 0).

Multiply by FOV_vert to get the vertical angle alpha from the image center to the object bottom in degrees.

✅ Step 2: Add camera tilt angle

<pre> theta_total = tilt_angle_deg + alpha </pre>
The actual angle from the camera to the object bottom is the camera’s downward tilt plus the angle offset (alpha).

✅ Step 3: Use trigonometry to estimate distance

<pre> 
theta_rad = math.radians(theta_total)
distance = cam_height_m / math.tan(theta_rad) 
</pre>
Convert the angle from degrees to radians (because math.tan() expects radians).

Using trigonometry:
=
<pre>
tan(𝜃)=camera height/ distance 
distance = camera height / tan(𝜃) 
</pre>

​
​
 
✅ Return the result:

<pre> return distance </pre>
This gives the estimated distance from the camera to the base of the object, assuming a flat ground and calibrated camera.\\



Requirements:
=

python 3.8 above,

opencv-python ,numpy (install using pip install command)
