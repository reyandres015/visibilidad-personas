def visibility(alturas: []):
    respuesta = []
    for i in range(len(alturas)):
        visibilidad = []
        # print(i)
        if i < len(alturas)-2 and alturas[i] >= alturas[i+1]:
            j = i + 2
            visibilidad.append(alturas[i+1])
            for persona in alturas[i+1:]:
                if alturas[j] >= persona:
                    visibilidad.append(alturas[j])
                if j<len(alturas)-1:
                    j+=1
                else:
                    break
            respuesta.append(len(visibilidad))
        else:
            if i == len(alturas)-1:
                respuesta.append(0)
            else:
                respuesta.append(1)
    return respuesta

print(visibility([10,6,8,5,11,9]))