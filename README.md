<h1 align="center"> Image Processing Project </h1>

<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#Installation">  Installation </a></li>
    <li><a href="#Introduction">  Introduction </a></li>
    <li><a href="#Objectives and scope">  Objectives and scope </a></li>
    <li><a href="#Methodology">  Methodology </a></li>
    <ul>
    <li><a href="#Down Sampling">  Down Sampling </a></li>
    <li><a href="#Up Sampling">  Up Sampling </a></li>
    <li><a href="#Negative of an Image">  Negative of an Image </a></li>
    <li><a href="#Thresholding">  Thresholding </a></li>
    <li><a href="#Blurring">  Blurring </a></li>
    <li><a href="#Low Pass Filtering (LPF)">  Low Pass Filtering (LPF) </a></li>
    <li><a href="#Gaussian Noise">  Gaussian Noise </a></li>
    <li><a href="#Facial Feature Detection">  Facial Feature Detection </a></li>
    <li><a href="#Laplacian Edge Detection">  Laplacian Filter </a></li>
    </ul>
    <li><a href="#Conclusion"> Conclusion </a></li>
    <li><a href="#Contributing">  Contributing </a></li>
    <li><a href="#ToDo">  To Do </a></li>
    <li><a href="#Video Demo">  Video Demo </a></li>

  </ol>
</details>
<hr>
<!--![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png) -->






<!-- Installation -->
<h2 id="Installation"> 📦: Installation </h2>

See [the contributing guide](CONTRIBUTING.md) for detailed instructions on how to get started with our project.
<p align="justify">

1. Obtain a copy of [Python 3.9](https://www.python.org/downloads/release/python-3913/)
2. [Create a virtual environment](https://docs.python.org/3/library/venv.html) & activate it.
3. Run the following in the venv...

```sh
pip install cmake
pip install -r requirements.txt
```
4. You can run the program in the venv

```sh
cd (install path)\Image_Processing\All_Project_Files\Final_Project_Files
python .\Image_Processing_Options.py
```

</p>
<hr>










<!-- Introduction -->
<h2 id="Introduction"> :pencil: Introduction </h2>

<p align="justify">
  Edge detection is an essential part of image processing that involves finding the boundaries of objects
within an image. This process can be used to extract useful information from an image, such as object
recognition or feature detection. One of the most common techniques for edge detection is the
Laplacian filter, which is a second-order derivative filter used to detect changes in the intensity of the
image.

In this project, we will explore edge detection using the Laplacian filter and other image processing
techniques such as low pass filtering (LPF), high pass filtering (HPF), and thresholding. LPF and HPF
are commonly used to enhance images and remove noise, while thresholding is used to binarize an
image into black and white pixels based on a certain threshold value.

The project will involve implementing these techniques using MATLAB and applying them to various
test images to demonstrate their effectiveness in edge detection. The results will be analyzed and
compared to determine the most effective approach for edge detection in different scenarios.
The objectives of this project are to gain a deeper understanding of image processing techniques,
specifically edge detection using the Laplacian filter, LPF, HPF, and thresholding, and to demonstrate
the practical applications of these techniques in real-world scenarios.

  Through this project, we hope to
enhance our skills in image processing and analysis, as well as gain insights into the challenges and
limitations of edge detection techniques.

</p>
<hr>


<!-- Objectives and Scope -->
<h2 id="Objectives and Scope"> :cloud: Objectives and Scope</h2>

<p align="justify">
  Utilizing image processing techniques such as low-pass filtering (LPF), blurring, and other such
techniques to reduce noise and improve the overall quality of the images, as well as using edge
detection to define boundaries for the images' borders.

A number of different methods, including thresholding and edge detection, are utilised in the
process of segmenting and extracting information from images.

The distinction between the different subcategories can be seen through the employment of a
variety of user-defined functions as well as built-in functions (LPF, Edge detection, etc).

</p>

<hr>

<!-- Methodology -->
<h2 id="Methodology"> :cloud: Methodology </h2>

<p align="justify">
  The methodology for this project involved several steps, including image acquisition, image preprocessing, edge detection using the Laplacian filter, LPF, HPF, and thresholding, and analysis of the
results.
The first step in the methodology was to acquire test images to be used in the project. These images
were chosen based on their complexity and variability to test the effectiveness of the different edge
detection techniques.

The second step was image pre-processing, which involved applying noise reduction techniques such
as median filtering and histogram equalization to enhance the quality of the images. This was done to
ensure that the edge detection techniques were applied to clear and high-quality images.

The third step was edge detection using the Laplacian filter, LPF, HPF, and thresholding techniques.
The Laplacian filter was applied to detect edges by finding changes in the intensity of the image,
while LPF and HPF were used to remove noise and enhance the edges. Thresholding was used to
binarize the image into black and white pixels based on a certain threshold value.

Finally, the results were analyzed and compared to determine the most effective approach for edge
detection in different scenarios. This involved visually comparing the different edge detection
techniques and evaluating their accuracy in detecting edges.

Overall, the methodology for this project was a combination of image acquisition, pre-processing,
edge detection using the Laplacian filter, LPF, HPF, and thresholding, and analysis of the results to
determine the effectiveness of each technique in edge detection.


</p>

<hr>

<!-- Down Sampling -->
<h2 id="Down Sampling"> :small_orange_diamond: Down Sampling </h2>

<p align="justify">
  Down Sampling:

• The process of resampling in a multi-rate digital signal processing system is referred to as
down sampling, compression, and decimation in digital signal processing.

• Both down sampling and decimation can refer to the full process of bandwidth reduction
(filtering) and sample-rate reduction, or they can be used interchangeably with the term
compression.

• The technique produces an estimate of the sequence that would have been generated by
sampling the signal at a lower rate when applied to a sequence of samples of a signal or a
continuous function (or density, as in the case of a photograph).

• In down-sampling technique, the number of pixels in the given image is reduced depending
on the sampling frequency. Due to this, resolution and size of the image decreases.

• Output:

 ![image](https://github.com/Haleshot/Projects/assets/57552973/3411e8eb-9375-4527-9724-441978892c61)



</p>

<hr>




<!-- Up Sampling -->
<h2 id="Up Sampling"> :small_orange_diamond: Up Sampling </h2>

<p align="justify">
  Up Sampling:

• Up sampling, expansion, and interpolation are terminologies used to describe the resampling
procedure in a mult-irate digital signal processing system.

• Up sampling can refer to either expansion or the full expansion and filtering process
(interpolation).

• Up-sampling technique increases the resolution as well as the size of the image.
• Some commonly used up-sampling techniques are:

  · Nearest neighbour interpolation
  · Bilinear interpolation
  · Cubic interpolation

• Output:

  ![image](https://github.com/Haleshot/Projects/assets/57552973/ef7a1644-8d8f-4642-a0ee-725156ccd550)




</p>

<hr>




<!-- Negative of an Image -->
<h2 id="Negative of an Image"> :small_orange_diamond: Negative of an Image </h2>

<p align="justify">
Negative of an Image:

• Photographic negative in which the light areas of the subject are reproduced as dark and the
dark areas as light.

• Negatives typically take the form of a transparent material, such glass or plastic.

• These tones are reversed and result in a positive photographic print when sensitised paper is
exposed through a negative, which can be achieved either by placing the negative and paper
in close proximity or by projecting a negative image onto the paper.

• s = (L-1) – r , where L= number of gray levels


• Output:

  ![image](https://github.com/Haleshot/Projects/assets/57552973/6ddca68e-e229-441f-8915-858e52232082)

</p>

<hr>



<!-- Thresholding -->
<h2 id="Thresholding"> :small_orange_diamond: Thresholding </h2>

<p align="justify">
Thresholding:

• Thresholding is a type of image segmentation, where we change the pixels of an image to
make the image easier to analyze.

• In thresholding, we convert an image from colour or grayscale into a binary image, i.e., one
that is simply black and white.

• Image thresholding is a simple, yet effective, way of partitioning an image into a foreground
and background.

• We use two types of thresholding i.e. with and without background.


• Output:

  Thresholding with background:
        ![image](https://github.com/Haleshot/Projects/assets/57552973/5d894d79-0800-4ed3-a44b-ce07cba33eb1)

  Thresholding without background:
  ![image](https://github.com/Haleshot/Projects/assets/57552973/137a155c-6d6b-4797-b099-8135cfed17aa)


</p>

<hr>


<!-- Blurring -->
<h2 id="Blurring"> :small_orange_diamond: Blurring </h2>

<p align="justify">
Blurring an image makes the image look less sharp.

• This can be done by smoothing the color transition between the pixels.

• When we blur an image, we make the colour transition from one side of an edge in the image
to another smooth rather than sudden.

• The effect is to average out rapid changes in pixel intensity.

• We subtract the maximum pixel value(255) from the given image's matrix.



• Output:

  ![image](https://github.com/Haleshot/Projects/assets/57552973/3b5820f7-efdf-42ba-acc9-45fff8bc9e3d)


</p>

<hr>



<!-- LPF -->
<h2 id="Low Pass Filtering (LPF)"> :small_orange_diamond: Low Pass Filtering (LPF) </h2>

<p align="justify">
Low Pass Filtering (LPF):

• It is also known as a smoothing filter. It removes the high frequency content from the image.

• Example of Low pass averaging filter mask is as shown:
  ![image](https://github.com/Haleshot/Projects/assets/57552973/68c8097f-1528-4471-87cf-c87e13f720f7)




• Output:

  ![image](https://github.com/Haleshot/Projects/assets/57552973/3317e1ee-b827-45e1-b71f-349d4b5e29cf)



</p>

<hr>

<!-- Gaussian Noise -->
<h2 id="Gaussian Noise"> :small_orange_diamond: Gaussian Noise </h2>

<p align="justify">
Gaussian Noise:

• A Gaussian Filter is a low pass filter used for reducing noise (high frequency components)
and blurring regions of an image.

• The filter is implemented as an Odd sized Symmetric Kernel (DIP version of a Matrix) which
is passed through each pixel of the Region of Interest to get the desired effect.


• Output:

  ![image](https://github.com/Haleshot/Projects/assets/57552973/2877adbe-2b77-4092-bf7f-17e45edfd45b)


</p>

<hr>



<!-- Facial Feature Detection -->
<h2 id="Facial Feature Detection"> :small_orange_diamond: Facial Feature Detection </h2>

<p align="justify">
Facial Feature Detection:

Facial feature detection is a computer vision technique that identifies and locates the key features of a human face in an image, such as eyes, nose, mouth, eyebrows, etc. It can be used for various applications such as face recognition, emotion analysis, face editing, and more. This python program performs facial feature detection using the following steps:

- Load an image file as input
- Convert the image to grayscale
- Detect faces in the image using a pre-trained Haar cascade classifier
- For each detected face, draw a bounding box around it.
- Detects facial features in each face using a pre-trained shape predictor model (eye haarcasacade classifier).
- Display the output image with the detected faces and facial features highlighted.


• Output:

  ![image](https://github.com/Haleshot/Projects/assets/57552973/eee541da-74ec-4fdc-801b-06fea5cb5166)



</p>

<hr>

<!-- Laplace Edge Detection -->
<h2 id="Laplacian Filter"> :small_orange_diamond: Laplacian Filter </h2>

<p align="justify">
Laplacian Filter:

• A Laplacian filter is an edge detector used to compute the second derivatives of an image,
measuring the rate at which the first derivatives change. This determines if a change in
adjacent pixel values is from an edge or continuous progression.

• Laplacian filter kernels usually contain negative values in a cross pattern, centered within the
array. The corners are either zero or positive values. The center value can be either negative or
positive.


• Output:

  ![image](https://github.com/Haleshot/Projects/assets/57552973/d200434b-1fe1-4c32-8627-e324e872a690)




</p>

<hr>






<!-- Conclusion -->
<h2 id="Conclusion"> :small_orange_diamond: Conclusion </h2>

<p align="justify">
Conclusion:

• In conclusion, the project demonstrated the effectiveness of edge detection techniques using the
Laplacian filter, LPF, HPF, and thresholding.

  • The results showed that the Laplacian filter was the most
    effective technique for edge detection, with high accuracy in detecting edges in various test images.
    LPF and HPF were also effective in enhancing the edges and removing noise, respectively, which
    resulted in more accurate edge detection using the Laplacian filter. Thresholding was found to be less
    effective in detecting edges, but was still useful in binarizing the image for further analysis.

  • The project also highlighted the importance of image pre-processing in edge detection, as the quality
    of the input image significantly impacted the accuracy of the results. The application of preprocessing techniques such as median filtering and histogram equalization was found to be critical in improving the quality of the images.

  • Overall, the project provided valuable insights into the practical applications of edge detection
    techniques in image processing and analysis. The results demonstrate the potential of these techniques
    for a range of applications, from object recognition to feature detection. The limitations and
    challenges of these techniques were also discussed, providing insights for future research and
    development in this area.




</p>

<hr>






<!-- Contributing -->
<h2 id="Contributing"> Contributing </h2>

<p align="justify">

See [the contributing guide](CONTRIBUTING.md) for detailed instructions on how to get started with our project.

If you're looking for a way to contribute, you can scan through our [existing issues](https://github.com/Haleshot/Projects/issues) for something to work on. When ready, check out [Getting Started with Contributing](CONTRIBUTING.md) for detailed instructions.


Click on these badges to see how you might be able to help:

<div align="center" markdown="1">

[![GitHub repo Issues](https://img.shields.io/github/issues/Haleshot/Image_Processing?style=flat&logo=github&logoColor=red&label=Issues)](https://github.com/Haleshot/Image_Processing/issues) [![GitHub repo PRs](https://img.shields.io/github/issues-pr/Haleshot/Image_Processing?style=flat&logo=github&logoColor=orange&label=PRs)](https://github.com/Haleshot/Image_Processing/pulls) [![GitHub repo Merged PRs](https://img.shields.io/github/issues-search/Haleshot/Image_Processing?style=flat&logo=github&logoColor=green&label=Merged%20PRs&query=is%3Amerged)](https://github.com/Haleshot/Image_Processing/pulls?q=is%3Apr+is%3Amerged)

</div>

Simple terms:

1. `Fork` this repository
2. Create a `branch`
3. `Commit` your changes
4. `Push` your `commits` to the `branch`
5. Submit a `pull request`

</p>
<hr>



<!-- To Do -->
<h2 id="ToDo"> To Do </h2>

<p align="justify">


- [ ] Refine UI more, add Video processing and Erosion/Dilation features
  - [ ] PyQt5 Editor

### In Progress

- [ ] Improve README guides, contributing guides, etc.
- [ ] Add a Video demo in the form of Gif Link for viewers to easily see the working.

- [ ] Showing user, which file to run as main file - portraying user flow.
- [ ] Adding Save as button

### Done ✓
- [x] Add exceptions to prevent program from crashing when user opens window to select input image but clicks on the close button of the window; same with Save as button.
- [x] Add Facial Feature Detection Button.

</p>
<hr>



<!-- Video Demo -->
<h2 id="Video Demo"> Video Demo </h2>
<!-- 
<p align="center">

<img src="https://media.tenor.com/hB9OTbewrikAAAAi/work-work-in-progress.gif" width="200" height="300" />

</p> -->
    <ul>
    <li><a href="Down Sampling">  Down Sampling </a></li>
    <li><a href="#Up Sampling">  Up Sampling </a></li>
    <li><a href="#Negative of an Image">  Negative of an Image </a></li>
    <li><a href="#Thresholding">  Thresholding </a></li>
    <li><a href="#Blurring">  Blurring </a></li>
    <li><a href="#Low Pass Filtering (LPF)">  Low Pass Filtering (LPF) </a></li>
    <li><a href="#Gaussian Noise">  Gaussian Noise </a></li>
    <li><a href="#Facial Feature Detection">  Facial Feature Detection </a></li>
    <li><a href="#Laplacian Edge Detection">  Laplacian Filter </a></li>
    </ul>
  
<h2 id="Down Sampling"> Down Sampling </h2>
<img src="https://github.com/Haleshot/Image_Processing/assets/57552973/382ed130-5229-4f8b-8df5-1a02af4e71ed" />

<!-- ![Down_Sampling_Demo](https://github.com/Haleshot/Image_Processing/assets/57552973/382ed130-5229-4f8b-8df5-1a02af4e71ed)
 -->

