import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def classical():
    return render_template('home.html')
    #return render_template('mfps.html')

@app.route('/recordmedicalstatistics')
def recordmedstat():
   return render_template('recordmedstat.html')

@app.route('/certificatemedicalstatistics')
def certificatemedstat():
   return render_template('certificatemedstat.html')

@app.route('/transcriptstatistics')
def transcript():
   return render_template('transcript.html')

@app.route('/intermediateexamination')
def interexam():
   return render_template('interexam.html')

@app.route('/finalexamination')
def finalexam():
   return render_template('finalexam.html')

@app.route('/diploma')
def diploma():
   return render_template('diploma.html')

@app.route('/germanmedicaldegree')
def medgermany():
   return render_template('medgermany.html')

@app.route('/hungarianmedicaldegree')
def medhungary():
   return render_template('medhungary.html')

@app.route('/medstat1unit1')
def ms1u1():
   return render_template('MS1U1.html')

@app.route('/medstat1unit2')
def ms1u2():
   return render_template('MS1U2.html')

@app.route('/medstat1unit3')
def ms1u3():
   return render_template('MS1U3.html')

@app.route('/medstat1unit4')
def ms1u4():
   return render_template('MS1U4.html')

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

@app.route('/piano/londonbridge')
def londonbridge():
   return render_template('londonbridge.html')

@app.route('/piano/londonbridge/print')
def londonbridgeprint():
   return render_template('printlondonbridge.html')

@app.route('/piano/rowyourboat')
def rowyourboat():
   return render_template('rowyourboat.html')

@app.route('/piano/rowyourboat/print')
def rowyourboatprint():
   return render_template('printrowyourboat.html')

@app.route('/piano/blacksheep')
def blacksheep():
   return render_template('blacksheep.html')

@app.route('/piano/blacksheep/print')
def blacksheepprint():
   return render_template('printblacksheep.html')


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
    app.run()
