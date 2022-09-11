# Music-Recommendation-based-on-Emotion-Recognition

### Problem Statement :
Nowadays, music platforms provide easy access to large amounts of music. They are working continuously to improve music organization and search management thereby addressing the problem of choice and simplify exploring new music pieces. Recommendation systems gain more and more popularity and help people to select appropriate music for all occasions. However, there is still a gap in personalization and emotions driven recommendations. Music has a great influence on humans and is widely used for relaxing, mood regulation, destruction from stress and diseases, to maintain mental and physical work. <br>
Most of the existing music recommendation systems use collaborative or content based recommendation engines. However, the music choice of a user is not only dependent on the historical preferences or music contents. But also dependent on the mood of that user. This project proposes an emotion based music recommendation framework that learns the emotion of a user either by detecting their facial emotions or by detection the emotion of the song title they input.<br><br>
Our project contains two major modules :
Dividing the songs present in the dataset into 2 moods - relaxing and energetic by using K-means clustering. The emotion of the song title given as input by the user is detected and then the appropriate playlist along with top 10 most relevant songs is recommended.
Detecting the facial emotion of the user using neural networks and recommending songs based on the emotion detected.

### Algorithms Used:
<li>K-Means Clustering</li>
<li>Multiclass Neural Network</li>
<li>Adam Optimization Algorithm</li>
<li>Haar Cascade method to detect real time facial expressions</li>


### Techstack and libraries Used:
<li>HTML, CSS, Bootstrap</li>
<li>Django</li>
<li>Flask</li>
<li>Scikit,pandas,numpy</li>
