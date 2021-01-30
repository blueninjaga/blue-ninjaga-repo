import turtle


def draw_orbit(orbit):
    t.goto(0, orbit * (-1))
    t.down()
    t.circle(orbit)
    t.up()


Sun =30
Mercury =4.87
Venus =12.10
Earth =12.72
Mars = 6.77
Jupiter =139.82
Saturn =116.46
Uranus =50.72
Neptune =49.24

Sun_color='#ffcc00'
Mercury_color='#8585ad'
Venus_color='#ff6600'
Earth_color='#6699ff'
Mars_color='#804000'
Jupiter_color='ff9933'
Saturn_color='ff9966'
uranus_color='#1a53ff'
neptune_color='1a53ff'

sun_orb=0
mercury_orb=20
venus_orb=36
earth_orb=50
mars_orb=76
Jupiter_orb=260
saturn_orb=470
uran_orb=600
neptune_orb=750

t = turtle.Pen()
t.pencolor('yellow')
turtle.Screen().bgcolor("black")
draw_orbit(sun_orb)
draw_orbit(mercury_orb)
draw_orbit(venus_orb)
draw_orbit(earth_orb)
draw_orbit(mars_orb)
draw_orbit(Jupiter_orb)
draw_orbit(saturn_orb)
draw_orbit(uran_orb)
draw_orbit(neptune_orb)

