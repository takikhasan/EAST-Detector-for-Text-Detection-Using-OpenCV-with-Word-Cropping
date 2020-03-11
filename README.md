# EAST-Detector-for-Text-Detection-Using-OpenCV-with-Word-Cropping
<h3>How to run:</h3>
<ol>
  <li>Clone the repo on your computer</li>
  <li>Run <code>pip install imutils</code> anywhere</li>
  <li>Run <code>pip install numpy</code> anywhere</li>
  <li>Run <code>pip install opencv-python</code> anywhere</li>
  <li>Run <code>python opencv_text_detection_image.py --image images/Book.jpg --east frozen_east_text_detection.pb</code> in the local repo</li>
</ol>
<h3>FYI:</h3>
<ul>
  <li>Put the input images in the <code>input</code> folder</li>
  <li>The output images will be in the <code>output</code> folder in sorted order</li>
</ul>
<h3>Pro Tip:</h3>
<ul>
  <li>Increase resized width and height for better accuracy (current default: <code>1280</code>)</li>
  <li>Cons: Takes more time the more you increase the size. At <code>1280</code> it takes almost 5 seconds</li>
  <li>Pros: Increases accuracy a lot. At <code>1280</code> accuracy is very high alhamdulillah</li>
</ul>