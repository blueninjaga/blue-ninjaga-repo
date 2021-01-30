import turtle
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

turtle.pencolor('yellow')
turtle.circle(0,Sun_color*(-1))
turtle.down()
turtle.circle(sun_orb)
turtle.up()
turtle.goto(0,mercury_orb*(-1))
turtle.down()
turtle.circle(mercury_orb)
turtle.up()
turtle.goto(0,venus_orb*(-1))
turtle.down()
turtle.circle(venus_orb)
turtle.up()
turtle.goto(0,earth_orb*(-1))
turtle.down()
turtle.circle(earth_orb)
turtle.up()
turtle.goto(0,mars_orb*(-1))
turtle.down()
turtle.circle(mars_orb)
turtle.up()
turtle.goto(0,Jupiter_orb*(-1))
turtle.down()
turtle.circle(Jupiter_orb)
turtle.up()
turtle.goto(0,saturn_orb*(-1))
turtle.down()
turtle.circle(saturn_orb)
turtle.up()
turtle.goto(0,uran_orb*(-1))
turtle.down()
turtle.circle(uran_orb*(-1))
turtle.up()
turtle.circle(neptune_orb*(-1))
turtle.down()
turtle.circle(neptune_orb*(-1))
