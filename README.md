
# Face Recognition Engage project

This is my project for Microsoft Engage 2022. I have choosen the face recognition path.
I have created a web application using flask framework.

The web application consist of 5 services and each uses a different model. The first one is trained using python while other 4 are trained in google teachable machine are present in the form of JavaScript inside the html files.

Link for video demo of the functioning of the web application : https://youtu.be/nI3EeEeFesk





## Folders of project
The repository of the project mainly consist of 3 folders:
1. flask app : contain the main flask application.
2. html files used in flask webapp : contains the html css and js files which can be used to run if the flask app does not work on your local machine due to some reasons.
3. pyhton codes used in building model : It contains the python codes which were used by me while training the model. This file is added in repo because our mentor asked us to add the pipeline and training model pyhton codes.

* The main web app using flask framework is in the flask app folder but if due to some reason you are not able to run flask webapp then in that case I have provided a html files folder which has html, css and js files. These can be used to run all my functionalities except one which requires python code to run.

## How to install requirements

To run the project on your local machines you need to install all the requirements from requirements.txt file.
All the packages mentioned in the requirements.txt are according to my python version which is 3.10.4. The requirements.txt file 
is automatically created using commmand pip freeze > requirements.txt and hence has mentioned all the packages version from my computer.

you can install these using command pip install -r requirements.

But sometimes we get error in installing through the requirements.txt
file. So can individually install the following packages using pip install command :

* opencv 
* numpy
* sklearn
* scipy
* pillow
* flask

according to me these will be enough as all other required are already 
present in pyhton3.

But if it still some package missing then install them accordingly.

I also used dlib and face_recognition but I don't think they will be required to install to run flask web app 
as it was used during training the model. After installing dlib face_recognition can be easily installed using 
pip install face_recognition. To install dlib you need to install cmake in
your computer through its website. The dlib wheel file is not offically available for python versions above
3.6. It can be downloaded according to your python version from : https://github.com/datamagic2020/Install-dlib 
## How to run the web app on your local machine
To run the web application you need to follow following steps :
1. Open the flask app folder in the visual studio code and then install requirements using pip install -r requirements.txt. If requiremenst are already installed go to next step.
2. Then through the vs code navigate to app folder inside the flask app folder (root folder). Inside the app folder open main.py and run this pyhton file.
3. after running main.py we will get the link to open the webapp in the output terminal of vs code.
4. On clicking that link you will reach the homepage of the webpage in your default browser.

* Now you can use the web application.

* If due to some reason the flask app does not work on your local machine then you can open the folder named html files used in flask app.Then open the base.html file and then you will reach the home page of the website. You will be able to use all the functionality as in flask app but except one functionality of face and emotion recognition which works in the python function in the flask application(utilss.py). All other AI models are in Js and can be accessed from there also.   
## Functioning
The Interface of the app is very easy and self explainatry. The web app has 
5 services which can be accessed from the home page. These are :
* FACE AND EMOTION RECOGNITON :  this page takes a picture from user and then print the both the initial and the resultant image. The resultant image contains the name and emotion of the people in the image. It is capable of recognising face of 10 famous personalities which I have mentioned on the webpage. for emotion detection I have used dataset of kaggle. the model is made, train and pipelined from scratch in pyhton.
* GENDER DETECTION : On this page after clicking on start button permisson for web cam is asked and then webcam is opened and then the gender of the person in front of the webcam is displayed below the webcam. This model is developed with the help of google teachable machine.
* MASK DETECTION : On this page after clicking on start button permisson for web cam is asked and then webcam is opened and then the face of person is scanned and then the status of the person (i.e wearing mask, not wearing mask, not wearing mask correctly) based on persons state is displayed below the cam. This model is developed with the help of google teachable machine.
* DROWSINESS DETECTION : On this page after clicking on start button permisson for web cam is asked and then webcam is opened and then the status of person whether alert or drowsy is displayed below the cam  . This model is developed with the help of google teachable machine.
* HAND SIGN DETECTION : On this page after clicking on start button permisson for web cam is asked and then webcam is opened. This service take input of the hand from the webcam and based on your hand placements and movement it shows the following outputs:(thumbs up, thumbs down, fist, victory sign, palm and namaste sign) . This model is developed with the help of google teachable machine.

All the links of the teachable machines are present inside the html pages of the respective model, inside the script tag.
