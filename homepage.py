import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def classical():
    return render_template('home.html')
    #return render_template('mfps.html')

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

@app.route('/mfp')
def mfp():
   return render_template('mfps.html')

@app.route('/mfp/mfps2to6')
def mfps2to6():
   return render_template('mfps2to6.html')

@app.route('/mfp/mfps7to10')
def mfps7to10():
   return render_template('mfps7to10.html')

@app.route('/mfp/mfps2to10')
def mfps2to10():
   return render_template('mfps2to10.html')

@app.route('/mfp/mfps2to12')
def mfps2to12():
   return render_template('mfps2to12.html')

@app.route('/mfp/dfps2to6')
def dfps2to6():
   return render_template('dfps2to6.html')

@app.route('/mfp/dfps7to10')
def dfps7to10():
   return render_template('dfps7to10.html')

@app.route('/mfp/dfps2to10')
def dfps2to10():
   return render_template('dfps2to10.html')

@app.route('/mfp/dfps2to12')
def dfps2to12():
   return render_template('dfps2to12.html')

@app.route('/mfp/afps2to6')
def afps2to6():
   return render_template('afps2to6.html')

@app.route('/mfp/afps7to10')
def afps7to10():
   return render_template('afps7to10.html')

@app.route('/mfp/afps2to10')
def afps2to10():
   return render_template('afps2to10.html')

@app.route('/mfp/afps2to12')
def afps2to12():
   return render_template('afps2to12.html')

@app.route('/mfp/sfps2to6')
def sfps2to6():
   return render_template('sfps2to6.html')

@app.route('/mfp/sfps7to10')
def sfps7to10():
   return render_template('sfps7to10.html')

@app.route('/mfp/sfps2to10')
def sfps2to10():
   return render_template('sfps2to10.html')

@app.route('/mfp/sfps2to12')
def sfps2to12():
   return render_template('sfps2to12.html')

@app.route('/piano')
def piano():
   return render_template('index.html')

@app.route('/piano/fivelittleducks')
def fivelittle():
   return render_template('fivelittleducks.html')

@app.route('/piano/fivelittleducks/print')
def fivelittleprint():
   return render_template('printfivelittleducks.html')

@app.route('/piano/frerejaques')
def frerejaques():
   return render_template('frerejaques.html')

@app.route('/piano/frerejaques/print')
def frerejaquesprint():
   return render_template('printfrerejaques.html')


@app.route('/confusion')
def confusion():
   return render_template('confusion.html')


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

