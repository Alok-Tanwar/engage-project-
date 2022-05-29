To run the project on your local machines you need to install all the requirements from requirement.txt file. Obviously you need to have
python installed on your computer to install the packages

There are certain packages like dlib which are not officially available for the python versions above 3.6. If you are not able to 
install that due to new version there are various unofficial versions available on internet. I only need to install dlib from unofficial 
sources. I am mentioning the link for the github repo from where I installed dlib. I found it on stackoverflow.


The Project contains 3 folders :
1. flask app : contain the main flask application.
2. html files used in flask webapp: contains the html css and js files which can be used to run if the flask app does not work on your local machine due to some reasons.
3. pyhton codes used in building model : It contains the python codes which were used by me while training the model.

## THE MAIN WEBAPP USING FLASK FRAMEWORK IS IN THE FLASK APP FOLDER. IF DUE TO SOME REASON YOU ARE NOT ABLE TO RUN FLASK WEBAPP THEN IN
THAT CASE I HAVE PROVIDED A HTML FILE FOLDER WHICH WILL BE ABLE TO RUN ALL OF MY FUNCTIONALITY EXCEPT THE ONE WHICH I HAVE MADE FROM 
PYTHON CODE.


### HOW TO RUN THE FLASK WEBAPP ###
STEPS :
1. Open the flask app folder in the visual studio code and then install requirements using pip install -r requirements.txt
2. Then through the vs code navigate to app folder inside the flask app folder (root folder). Inside the app folder open main.py and run this pyhton file.
3. after running main.py we will get the link to open the webapp in the output terminal of vs code.
4. On clicking that link you will reach the homepage of the webpage in your default browser. You can also copy that link and can copy that in your browser.
## Now you can use the webapp/website on your browser

## If due to some reason the flask app does not work on your local machine then you can open the folder named html files used in flask app.
then open the base.html file and then you will reach the home page of the website. 
You will be able to use all the functionality as in flask but except one functionality of face and emotion recognition which works in the python function in the flask application(utilss.py).   
  

## "python codes used in building model" folder contains the jupyter notebook files which were used by me while training and pipelining my model. 
My engage mentor told us to upload the train and pipeline code in the repository. But it is of no use in running the flask app.

  