from flask import Flask, request

from yourturn_5_4 import WeaG

w = WeaG()
app = Flask(__name__)

@app.route("/")
def wea():
    loc = request.args.get('location')
    ans = ''
    
    if loc:
        r = w.grab(loc)
        if r:
            ans = f"{r['O']} 溫度:{r['T']:.1f}°C, 濕度:{r['H']:.0%}, 雨量:{r['R']:.1f}mm"
        else:
            ans = 'no such site!'
            
    content = f"""
    <form>
        站名 <input type="text" name='location' value={loc or ''}> <input type="submit" value="確定">
    </form>""" + ans
    
    return content

app.run()
