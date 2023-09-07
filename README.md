# visibilidad-personas
A quién veo en la fila?
Suponga que hay n
 personas paradas en una fila, y estan numeradas desde el 0
 hasta n−1
 de izquierda a derecha.


Se le suministra un arreglo alturas de enteros distintos donde alturas[i] representa la altura de la i-esima persona.


Una persona puede ver a otra a su derecha en la fila si todos los que estan en medio son mas bajos que la persona a la cual se esta viendo


Formalmente: la i-esima persona peude ver a la j-esima persona si i < j y min(allturas[i], alturas[j]) > max(alturas[i+1], alturas[i+2], ..., alturas[j-1])


Retorne como respuesta un arreglo respuesta de tamaño n
 donde respuesta[i] es la cantidad de personas que la i-esima persona puede ver a su derecha en la fila.

Entrada
Una estrucutra de datos lineal llamada alturas donde cada alturas[i] (entero) representa la altura de cada persona en la fila


Salida
Una estructura lineal respuesta de tamaño n
 en la siguiente representación: [respuesta[0], repuesta[1], ..., respuesta[n-1]]
