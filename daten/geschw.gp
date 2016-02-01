reset

#set terminal png
p "02011548.TXT" u 1:($4/100) w l lt 6 t 'GPS', "02011548.TXT" u 1:($5/100) w l lt 7 t 'Tacho'

pause -1

