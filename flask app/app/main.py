from flask import Flask
import views

app = Flask(__name__,)


# url
app.add_url_rule('/','base',views.base)
app.add_url_rule('/faceapp','faceapp',views.faceapp,methods=['GET','POST'])
app.add_url_rule('/mask','mask',views.mask)
app.add_url_rule('/handsign','handsign',views.handsign)
app.add_url_rule('/drowsy','drowsy',views.drowsy)
app.add_url_rule('/gender','gender',views.gender)


# run
if __name__ == "__main__":
    app.run(debug=True)
     