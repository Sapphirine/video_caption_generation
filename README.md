# Video Caption Generation Using Deep Learning and NLP

## Project Description

With the increasing volume of Multimedia operations in our everyday life, advancements in the
digital space have become essential. Captioning is
a natural language processing task that can revolutionize this segment. For instance, Web browsing
greatly relies on finding the tags/titles of media.
Image and Video Captioning would allow automatic annotation of the occurrences. This would
not only facilitate the development of efficient
search algorithms that search by contents of the
media but would also help in the design of better recommendation systems for users. The goal
of this project is to build Image Captioning and
Video Captioning models. In the first part of the
project, an Image Captioning Model is designed
using Deep Learning and Encoder-Decoder architecture. In the second part, the scope of the
model is expanded to Video Captioning. Flickr8k
and TRECVID-VTT Data are used for the tasks.
BLEU scores are calculated for the evaluation of
the models. Greedy and Beam Search Algorithms
are used for Real-Time Testing

<h2 id="Setup">Setup</h2>
Clone the repository : <code>git clone https://github.com/Sapphirine/video_caption_generation.git</code>

<h2 id="Video">Video</h2>

The video explaining the project can be found  <a href="https://www.youtube.com/watch?v=rJquNZ1nzvY">here</a>

<h2 id="System Overview">System Overview</h2>

<p align = "center"><img align = "center" src = "https://github.com/Sapphirine/video_caption_generation/blob/main/Report%20and%20Slides/figures/vd_system_overview.PNG" /></p>


## RESULTS
<center>
 <table> 
  <tr>
   <th>Video</th>
  <th>Predicted Caption</th>
  </tr>
 <tr>
  <td><img src="outputs/a boy sitting on a car seat of a car .gif" width="320px"/></td>
  <td>a boy sitting on a car seat of a car </td>
 <tr>
  <td><img src="outputs/a man is talking to a crowd .gif" width="320px"/></td>
  <td>a man is talking to a crowd </td>
  </tr>
  <tr>
  <td><img src="outputs/a man in a bathtub .gif" width="320px"/></td>
  <td>a boy in a bathtub </td>
  </tr>
  <tr>
  <td><img src="outputs/a cat in a room.gif" width="320px"/></td>
  <td>a cat in a room </td>
  </tr>
  <tr>
  <td><img src="outputs/a video of a video of a person.gif" width="320px"/></td>
  <td>a video of a video of a person </td>
  </tr>
  </table>
 </center>
 

 
 ## Actual v/s Predicted Captions
 
 <p align = "center"><img align = "center" src = "https://github.com/Sapphirine/video_caption_generation/blob/main/Report%20and%20Slides/figures/ap.PNG" /></p>
 
