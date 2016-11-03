import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def classical():
    return render_template('home.html')

@app.route('/labor')  
def labor():
   return render_template('deeplook.html')


@app.route('/launch')  
def launch():
   return render_template('androidapps.html')

@app.route('/launch/amhelp')
def amhelp():
   return render_template('amhelp.html')
   
#@app.route('/icebreaker')  
#def icebreaker():
#   return render_template('icebreaker.html')

#@app.route('/money')  
#def money():
#   return render_template('math.html')

#@app.route('/money/countpenny')  
#def countpenny():
#   return render_template('countpenny.html')

@app.route('/interest')  
def interest():
   return render_template('interest.html')

@app.route('/piano')
def piano():
   return render_template('index.html')

@app.route('/piano/fivelittleducks')
def fivelittle():
   return render_template('fivelittleducks.html')

@app.route('/piano/fivelittleducks/print')
def fivelittleprint():
   return render_template('printfivelittleducks.html')

@app.route('/confusion')
def confusion():
   return render_template('gulp/app/index.html')


@app.route('/study')  
def study():
   return render_template('study.html')

@app.route('/study/voronoi')
def voronoi():
   return render_template('voronoi.html')
   
@app.route('/study/programming')
def programming():
   return render_template('programming.html')   

@app.route('/about')
def about():
  return render_template('about.html')





if __name__ == '__main__':
   app.run(debug=True)

