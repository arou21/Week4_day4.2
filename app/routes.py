from app import app
from flask import render_template

@app.route('/')
def homePage():
    
    text = "SENDING THIS FROM PYTHON!!!"
    return render_template('index.html', my_text = text )


@app.route('/fav5')
def fav5():
    people = [('Mohamed Ali','https://sothebys-md.brightspotcdn.com/dims4/default/4833504/2147483647/strip/true/crop/602x909+0+0/resize/800x1208!/quality/90/?url=http%3A%2F%2Fsothebys-brightspot.s3.amazonaws.com%2Fmedia-desk%2F06%2Fb0%2Fdea7b2294c0fb8bea1c47ab88136%2Fccvxc-1.jpg'), 
    ("Bob Marley",'https://static.greatbigcanvas.com/images/singlecanvas_thick_none/movie-goods/bob-marley-,mg0082052.jpg'), 
    ("Messi",'https://cdn.britannica.com/34/212134-050-A7289400/Lionel-Messi-2018.jpg'),
    ("Nelson Mandela",'https://files.magzter.com/resize/magazine/1386586958/1/view/3.jpg'), 
    ("Michael Jackson",'https://cdn.i-scmp.com/sites/default/files/d8/images/canvas/2021/08/27/6aab1fe1-a152-4216-a41e-c3ca9e41fe54_15d28a3f.jpg')]
    return render_template('fav5.html', people=people)


