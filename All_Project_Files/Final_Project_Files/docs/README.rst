.. raw:: html

   <h1 align="center">

Image Processing Project

.. raw:: html

   </h1>

.. raw:: html

   <details open="open">

.. raw:: html

   <summary>

Table of Contents

.. raw:: html

   </summary>

.. raw:: html

   <ol>

.. raw:: html

   <li>

Installation

.. raw:: html

   </li>

.. raw:: html

   <li>

Introduction

.. raw:: html

   </li>

.. raw:: html

   <li>

Objectives and scope

.. raw:: html

   </li>

.. raw:: html

   <li>

Methodology

.. raw:: html

   </li>

.. raw:: html

   <ul>

.. raw:: html

   <li>

Down Sampling

.. raw:: html

   </li>

.. raw:: html

   <li>

Up Sampling

.. raw:: html

   </li>

.. raw:: html

   <li>

Negative of an Image

.. raw:: html

   </li>

.. raw:: html

   <li>

Thresholding

.. raw:: html

   </li>

.. raw:: html

   <li>

Blurring

.. raw:: html

   </li>

.. raw:: html

   <li>

Low Pass Filtering (LPF)

.. raw:: html

   </li>

.. raw:: html

   <li>

Gaussian Noise

.. raw:: html

   </li>

.. raw:: html

   <li>

Facial Feature Detection

.. raw:: html

   </li>

.. raw:: html

   <li>

Laplacian Filter

.. raw:: html

   </li>

.. raw:: html

   </ul>

.. raw:: html

   <li>

Conclusion

.. raw:: html

   </li>

.. raw:: html

   <li>

Contributing

.. raw:: html

   </li>

.. raw:: html

   <li>

To Do

.. raw:: html

   </li>

.. raw:: html

   <li>

Video Demo

.. raw:: html

   </li>

.. raw:: html

   </ol>

.. raw:: html

   </details>

.. raw:: html

   <hr>

.. raw:: html

   <!--![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png) -->

.. raw:: html

   <!-- Installation -->

.. raw:: html

   <h2 id="Installation">

📦: Installation

.. raw:: html

   </h2>

See `the contributing guide <CONTRIBUTING.md>`__ for detailed
instructions on how to get started with our project.

.. raw:: html

   <p align="justify">

1. Obtain a copy of `Python
   3.9 <https://www.python.org/downloads/release/python-3913/>`__
2. `Create a virtual
   environment <https://docs.python.org/3/library/venv.html>`__ &
   activate it.
3. Run the following in the venv…

.. code:: sh

   pip install cmake
   pip install -r requirements.txt

4. You can run the program in the venv

.. code:: sh

   cd (install path)\Image_Processing\All_Project_Files\Final_Project_Files
   python .\Image_Processing_Options.py

.. raw:: html

   </p>

.. raw:: html

   <hr>

.. raw:: html

   <!-- Introduction -->

.. raw:: html

   <h2 id="Introduction">

:pencil: Introduction

.. raw:: html

   </h2>

.. raw:: html

   <p align="justify">

Edge detection is an essential part of image processing that involves
finding the boundaries of objects within an image. This process can be
used to extract useful information from an image, such as object
recognition or feature detection. One of the most common techniques for
edge detection is the Laplacian filter, which is a second-order
derivative filter used to detect changes in the intensity of the image.

In this project, we will explore edge detection using the Laplacian
filter and other image processing techniques such as low pass filtering
(LPF), high pass filtering (HPF), and thresholding. LPF and HPF are
commonly used to enhance images and remove noise, while thresholding is
used to binarize an image into black and white pixels based on a certain
threshold value.

The project will involve implementing these techniques and applying them
to various test images to demonstrate their effectiveness in edge
detection. The results will be analyzed and compared to determine the
most effective approach for edge detection in different scenarios. The
objectives of this project are to gain a deeper understanding of image
processing techniques, specifically edge detection using the Laplacian
filter, LPF, HPF, and thresholding, and to demonstrate the practical
applications of these techniques in real-world scenarios.

Through this project, we hope to enhance our skills in image processing
and analysis, as well as gain insights into the challenges and
limitations of edge detection techniques.

.. raw:: html

   </p>

.. raw:: html

   <hr>

.. raw:: html

   <!-- Objectives and Scope -->

.. raw:: html

   <h2 id="Objectives and Scope">

:cloud: Objectives and Scope

.. raw:: html

   </h2>

.. raw:: html

   <p align="justify">

Utilizing image processing techniques such as low-pass filtering (LPF),
blurring, and other such techniques to reduce noise and improve the
overall quality of the images, as well as using edge detection to define
boundaries for the images’ borders.

A number of different methods, including thresholding and edge
detection, are utilised in the process of segmenting and extracting
information from images.

The distinction between the different subcategories can be seen through
the employment of a variety of user-defined functions as well as
built-in functions (LPF, Edge detection, etc).

.. raw:: html

   </p>

.. raw:: html

   <hr>

.. raw:: html

   <!-- Methodology -->

.. raw:: html

   <h2 id="Methodology">

:cloud: Methodology

.. raw:: html

   </h2>

.. raw:: html

   <p align="justify">

The methodology for this project involved several steps, including image
acquisition, image preprocessing, edge detection using the Laplacian
filter, LPF, HPF, and thresholding, and analysis of the results. The
first step in the methodology was to acquire test images to be used in
the project. These images were chosen based on their complexity and
variability to test the effectiveness of the different edge detection
techniques.

The second step was image pre-processing, which involved applying noise
reduction techniques such as median filtering and histogram equalization
to enhance the quality of the images. This was done to ensure that the
edge detection techniques were applied to clear and high-quality images.

The third step was edge detection using the Laplacian filter, LPF, HPF,
and thresholding techniques. The Laplacian filter was applied to detect
edges by finding changes in the intensity of the image, while LPF and
HPF were used to remove noise and enhance the edges. Thresholding was
used to binarize the image into black and white pixels based on a
certain threshold value.

Finally, the results were analyzed and compared to determine the most
effective approach for edge detection in different scenarios. This
involved visually comparing the different edge detection techniques and
evaluating their accuracy in detecting edges.

Overall, the methodology for this project was a combination of image
acquisition, pre-processing, edge detection using the Laplacian filter,
LPF, HPF, and thresholding, and analysis of the results to determine the
effectiveness of each technique in edge detection.

.. raw:: html

   </p>

.. raw:: html

   <hr>

.. raw:: html

   <!-- Down Sampling -->

.. raw:: html

   <h2 id="Down Sampling">

:small_orange_diamond: Down Sampling

.. raw:: html

   </h2>

.. raw:: html

   <p align="justify">

Down Sampling:

• The process of resampling in a multi-rate digital signal processing
system is referred to as down sampling, compression, and decimation in
digital signal processing.

• Both down sampling and decimation can refer to the full process of
bandwidth reduction (filtering) and sample-rate reduction, or they can
be used interchangeably with the term compression.

• The technique produces an estimate of the sequence that would have
been generated by sampling the signal at a lower rate when applied to a
sequence of samples of a signal or a continuous function (or density, as
in the case of a photograph).

• In down-sampling technique, the number of pixels in the given image is
reduced depending on the sampling frequency. Due to this, resolution and
size of the image decreases.

• Output:

.. figure:: https://github.com/Haleshot/Projects/assets/57552973/3411e8eb-9375-4527-9724-441978892c61
   :alt: image

   image

.. raw:: html

   </p>

.. raw:: html

   <hr>

.. raw:: html

   <!-- Up Sampling -->

.. raw:: html

   <h2 id="Up Sampling">

:small_orange_diamond: Up Sampling

.. raw:: html

   </h2>

.. raw:: html

   <p align="justify">

Up Sampling:

• Up sampling, expansion, and interpolation are terminologies used to
describe the resampling procedure in a mult-irate digital signal
processing system.

• Up sampling can refer to either expansion or the full expansion and
filtering process (interpolation).

• Up-sampling technique increases the resolution as well as the size of
the image. • Some commonly used up-sampling techniques are:

· Nearest neighbour interpolation · Bilinear interpolation · Cubic
interpolation

• Output:

.. figure:: https://github.com/Haleshot/Projects/assets/57552973/ef7a1644-8d8f-4642-a0ee-725156ccd550
   :alt: image

   image

.. raw:: html

   </p>

.. raw:: html

   <hr>

.. raw:: html

   <!-- Negative of an Image -->

.. raw:: html

   <h2 id="Negative of an Image">

:small_orange_diamond: Negative of an Image

.. raw:: html

   </h2>

.. raw:: html

   <p align="justify">

Negative of an Image:

• Photographic negative in which the light areas of the subject are
reproduced as dark and the dark areas as light.

• Negatives typically take the form of a transparent material, such
glass or plastic.

• These tones are reversed and result in a positive photographic print
when sensitised paper is exposed through a negative, which can be
achieved either by placing the negative and paper in close proximity or
by projecting a negative image onto the paper.

• s = (L-1) – r , where L= number of gray levels

• Output:

.. figure:: https://github.com/Haleshot/Projects/assets/57552973/6ddca68e-e229-441f-8915-858e52232082
   :alt: image

   image

.. raw:: html

   </p>

.. raw:: html

   <hr>

.. raw:: html

   <!-- Thresholding -->

.. raw:: html

   <h2 id="Thresholding">

:small_orange_diamond: Thresholding

.. raw:: html

   </h2>

.. raw:: html

   <p align="justify">

Thresholding:

• Thresholding is a type of image segmentation, where we change the
pixels of an image to make the image easier to analyze.

• In thresholding, we convert an image from colour or grayscale into a
binary image, i.e., one that is simply black and white.

• Image thresholding is a simple, yet effective, way of partitioning an
image into a foreground and background.

• We use two types of thresholding i.e. with and without background.

• Output:

Thresholding with background: |image|

Thresholding without background: |image1|

.. raw:: html

   </p>

.. raw:: html

   <hr>

.. raw:: html

   <!-- Blurring -->

.. raw:: html

   <h2 id="Blurring">

:small_orange_diamond: Blurring

.. raw:: html

   </h2>

.. raw:: html

   <p align="justify">

Blurring an image makes the image look less sharp.

• This can be done by smoothing the color transition between the pixels.

• When we blur an image, we make the colour transition from one side of
an edge in the image to another smooth rather than sudden.

• The effect is to average out rapid changes in pixel intensity.

• We subtract the maximum pixel value(255) from the given image’s
matrix.

• Output:

.. figure:: https://github.com/Haleshot/Projects/assets/57552973/3b5820f7-efdf-42ba-acc9-45fff8bc9e3d
   :alt: image

   image

.. raw:: html

   </p>

.. raw:: html

   <hr>

.. raw:: html

   <!-- LPF -->

.. raw:: html

   <h2 id="Low Pass Filtering (LPF)">

:small_orange_diamond: Low Pass Filtering (LPF)

.. raw:: html

   </h2>

.. raw:: html

   <p align="justify">

Low Pass Filtering (LPF):

• It is also known as a smoothing filter. It removes the high frequency
content from the image.

• Example of Low pass averaging filter mask is as shown: |image2|

• Output:

.. figure:: https://github.com/Haleshot/Projects/assets/57552973/3317e1ee-b827-45e1-b71f-349d4b5e29cf
   :alt: image

   image

.. raw:: html

   </p>

.. raw:: html

   <hr>

.. raw:: html

   <!-- Gaussian Noise -->

.. raw:: html

   <h2 id="Gaussian Noise">

:small_orange_diamond: Gaussian Noise

.. raw:: html

   </h2>

.. raw:: html

   <p align="justify">

Gaussian Noise:

• A Gaussian Filter is a low pass filter used for reducing noise (high
frequency components) and blurring regions of an image.

• The filter is implemented as an Odd sized Symmetric Kernel (DIP
version of a Matrix) which is passed through each pixel of the Region of
Interest to get the desired effect.

• Output:

.. figure:: https://github.com/Haleshot/Projects/assets/57552973/2877adbe-2b77-4092-bf7f-17e45edfd45b
   :alt: image

   image

.. raw:: html

   </p>

.. raw:: html

   <hr>

.. raw:: html

   <!-- Facial Feature Detection -->

.. raw:: html

   <h2 id="Facial Feature Detection">

:small_orange_diamond: Facial Feature Detection

.. raw:: html

   </h2>

.. raw:: html

   <p align="justify">

Facial Feature Detection:

Facial feature detection is a computer vision technique that identifies
and locates the key features of a human face in an image, such as eyes,
nose, mouth, eyebrows, etc. It can be used for various applications such
as face recognition, emotion analysis, face editing, and more. This
python program performs facial feature detection using the following
steps:

-  Load an image file as input
-  Convert the image to grayscale
-  Detect faces in the image using a pre-trained Haar cascade classifier
-  For each detected face, draw a bounding box around it.
-  Detects facial features in each face using a pre-trained shape
   predictor model (eye haarcasacade classifier).
-  Display the output image with the detected faces and facial features
   highlighted.

• Output:

.. figure:: https://github.com/Haleshot/Projects/assets/57552973/eee541da-74ec-4fdc-801b-06fea5cb5166
   :alt: image

   image

.. raw:: html

   </p>

.. raw:: html

   <hr>

.. raw:: html

   <!-- Laplace Edge Detection -->

.. raw:: html

   <h2 id="Laplacian Edge Detection">

:small_orange_diamond: Laplacian Filter

.. raw:: html

   </h2>

.. raw:: html

   <p align="justify">

Laplacian Filter:

• A Laplacian filter is an edge detector used to compute the second
derivatives of an image, measuring the rate at which the first
derivatives change. This determines if a change in adjacent pixel values
is from an edge or continuous progression.

• Laplacian filter kernels usually contain negative values in a cross
pattern, centered within the array. The corners are either zero or
positive values. The center value can be either negative or positive.

• Output:

.. figure:: https://github.com/Haleshot/Projects/assets/57552973/d200434b-1fe1-4c32-8627-e324e872a690
   :alt: image

   image

.. raw:: html

   </p>

.. raw:: html

   <hr>

.. raw:: html

   <!-- Conclusion -->

.. raw:: html

   <h2 id="Conclusion">

:small_orange_diamond: Conclusion

.. raw:: html

   </h2>

.. raw:: html

   <p align="justify">

Conclusion:

• In conclusion, the project demonstrated the effectiveness of edge
detection techniques using the Laplacian filter, LPF, HPF, and
thresholding.

• The results showed that the Laplacian filter was the most effective
technique for edge detection, with high accuracy in detecting edges in
various test images. LPF and HPF were also effective in enhancing the
edges and removing noise, respectively, which resulted in more accurate
edge detection using the Laplacian filter. Thresholding was found to be
less effective in detecting edges, but was still useful in binarizing
the image for further analysis.

• The project also highlighted the importance of image pre-processing in
edge detection, as the quality of the input image significantly impacted
the accuracy of the results. The application of preprocessing techniques
such as median filtering and histogram equalization was found to be
critical in improving the quality of the images.

• Overall, the project provided valuable insights into the practical
applications of edge detection techniques in image processing and
analysis. The results demonstrate the potential of these techniques for
a range of applications, from object recognition to feature detection.
The limitations and challenges of these techniques were also discussed,
providing insights for future research and development in this area.

.. raw:: html

   </p>

.. raw:: html

   <hr>

.. raw:: html

   <!-- Contributing -->

.. raw:: html

   <h2 id="Contributing">

Contributing

.. raw:: html

   </h2>

.. raw:: html

   <p align="justify">

See `the contributing guide <CONTRIBUTING.md>`__ for detailed
instructions on how to get started with our project.

If you’re looking for a way to contribute, you can scan through our
`existing
issues <https://github.com/Haleshot/Image_Processing/issues>`__ for
something to work on. When ready, check out `Getting Started with
Contributing <CONTRIBUTING.md>`__ for detailed instructions.

Click on these badges to see how you might be able to help:

.. container::

   |GitHub repo Issues| |GitHub repo PRs| |GitHub repo Merged PRs|

Simple terms:

1. ``Fork`` this repository
2. Create a ``branch``
3. ``Commit`` your changes
4. ``Push`` your ``commits`` to the ``branch``
5. Submit a ``pull request``

.. raw:: html

   </p>

.. raw:: html

   <hr>

.. raw:: html

   <!-- To Do -->

.. raw:: html

   <h2 id="ToDo">

To Do

.. raw:: html

   </h2>

.. raw:: html

   <p align="justify">

-  ☐ Refine UI more, add Video processing and Erosion/Dilation features

   -  ☐ PyQt5 Editor

In Progress
~~~~~~~~~~~

-  ☐ Showing user, which file to run as main file - portraying user
   flow.

Done ✓
~~~~~~

-  ☒ Add exceptions to prevent program from crashing when user opens
   window to select input image but clicks on the close button of the
   window; same with Save as button.
-  ☒ Add Facial Feature Detection Button.
-  ☒ Add a Video demo in the form of Gif Link for viewers to easily see
   the working.
-  ☒ Adding Save as button
-  ☒ Improve README guides, contributing guides, etc.

.. raw:: html

   </p>

.. raw:: html

   <hr>

.. raw:: html

   <!-- Video Demo -->

.. raw:: html

   <h2 id="Video Demo">

Video Demo

.. raw:: html

   </h2>

.. raw:: html

   <!-- 
   <p align="center"> <img src="https://media.tenor.com/hB9OTbewrikAAAAi/work-work-in-progress.gif" width="200" height="300" /> </p> -->

The entire project demo can be seen here - https://youtu.be/O-x44AT6ylU

.. raw:: html

   <li>

Down Sampling

.. raw:: html

   </li>

.. raw:: html

   <li>

Up Sampling

.. raw:: html

   </li>

.. raw:: html

   <li>

Negative of an Image

.. raw:: html

   </li>

.. raw:: html

   <li>

Thresholding With Background

.. raw:: html

   </li>

.. raw:: html

   <li>

Thresholding Without Background

.. raw:: html

   </li>

.. raw:: html

   <li>

Blurring

.. raw:: html

   </li>

.. raw:: html

   <li>

Low Pass Filtering (LPF)

.. raw:: html

   </li>

.. raw:: html

   <li>

Gaussian Noise

.. raw:: html

   </li>

.. raw:: html

   <li>

Facial Feature Detection

.. raw:: html

   </li>

.. raw:: html

   <li>

Laplacian Filter

.. raw:: html

   </li>

.. raw:: html

   <h3 id="#Down Sampling">

Down Sampling

.. raw:: html

   </h3>

.. figure:: https://github.com/Haleshot/Image_Processing/assets/57552973/382ed130-5229-4f8b-8df5-1a02af4e71ed
   :alt: Down_Sampling_Demo

   Down_Sampling_Demo

.. raw:: html

   <h3 id="#Up Sampling">

Up Sampling

.. raw:: html

   </h3>

.. figure:: https://github.com/Haleshot/Image_Processing/assets/57552973/00875f15-96bf-4644-a8f9-ead2a79441b5
   :alt: Up_Sampling_Demo

   Up_Sampling_Demo

.. raw:: html

   <h3 id="#Negative of an Image">

Negative of an Image

.. raw:: html

   </h3>

.. figure:: https://github.com/Haleshot/Image_Processing/assets/57552973/5646e806-2f16-4db0-b39b-e2035c4d8292
   :alt: Negative_Image_Sampling_Demo

   Negative_Image_Sampling_Demo

.. raw:: html

   <h3 id="#Thresholding With Background">

Thresholding With Background

.. raw:: html

   </h3>

.. figure:: https://github.com/Haleshot/Image_Processing/assets/57552973/d1acc2cc-148c-4815-872c-8563376e395f
   :alt: Thresholding_With_Background_Demo

   Thresholding_With_Background_Demo

.. raw:: html

   <h3 id="#Thresholding Without Background">

Thresholding Without Background

.. raw:: html

   </h3>

.. figure:: https://github.com/Haleshot/Image_Processing/assets/57552973/f6c14cf6-ca6a-47e4-85c0-884db070a56e
   :alt: Thresholding_Without_Background_Demo

   Thresholding_Without_Background_Demo

.. raw:: html

   <h3 id="#Blurring">

Blurring

.. raw:: html

   </h3>

.. figure:: https://github.com/Haleshot/Image_Processing/assets/57552973/6040b8f9-efa2-47a8-8563-594603b1e9f6
   :alt: Blurring_Demo

   Blurring_Demo

.. raw:: html

   <h3 id="#Low Pass Filtering (LPF)">

Low Pass Filtering (LPF)

.. raw:: html

   </h3>

.. figure:: https://github.com/Haleshot/Image_Processing/assets/57552973/a78b0123-a14a-4353-8585-077001bde157
   :alt: LPF_Demo

   LPF_Demo

.. raw:: html

   <h3 id="#Gaussian Noise">

Gaussian Noise

.. raw:: html

   </h3>

.. figure:: https://github.com/Haleshot/Image_Processing/assets/57552973/c0284caf-6092-4182-a36a-e92d20832bf7
   :alt: Gaussian_Demo

   Gaussian_Demo

.. raw:: html

   <h3 id="#Facial Feature Detection">

Facial Feature Detection

.. raw:: html

   </h3>

.. figure:: https://github.com/Haleshot/Image_Processing/assets/57552973/1eb2dfcd-7310-45d3-a4af-141575447767
   :alt: Facial_Feature_Detection_Demo

   Facial_Feature_Detection_Demo

.. raw:: html

   <h3 id="#Laplacian Edge Detection">

Laplacian Edge Detection

.. raw:: html

   </h3>

.. figure:: https://github.com/Haleshot/Image_Processing/assets/57552973/eed16965-d6d1-4760-b51f-64b9231d17f9
   :alt: Laplace_Edge_Detection_Demo

   Laplace_Edge_Detection_Demo

.. |image| image:: https://github.com/Haleshot/Projects/assets/57552973/5d894d79-0800-4ed3-a44b-ce07cba33eb1
.. |image1| image:: https://github.com/Haleshot/Projects/assets/57552973/137a155c-6d6b-4797-b099-8135cfed17aa
.. |image2| image:: https://github.com/Haleshot/Projects/assets/57552973/68c8097f-1528-4471-87cf-c87e13f720f7
.. |GitHub repo Issues| image:: https://img.shields.io/github/issues/Haleshot/Image_Processing?style=flat&logo=github&logoColor=red&label=Issues
   :target: https://github.com/Haleshot/Image_Processing/issues
.. |GitHub repo PRs| image:: https://img.shields.io/github/issues-pr/Haleshot/Image_Processing?style=flat&logo=github&logoColor=orange&label=PRs
   :target: https://github.com/Haleshot/Image_Processing/pulls
.. |GitHub repo Merged PRs| image:: https://img.shields.io/github/issues-search/Haleshot/Image_Processing?style=flat&logo=github&logoColor=green&label=Merged%20PRs&query=is%3Amerged
   :target: https://github.com/Haleshot/Image_Processing/pulls?q=is%3Apr+is%3Amerged
