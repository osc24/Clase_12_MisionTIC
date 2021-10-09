from flask import Flask, json, jsonify, request
from articulos import arts

app=Flask(__name__)


@app.route("/")
def index():
    return jsonify({
        "mensaje": "Buenos dias grupo"
        })

@app.route("/articulos")
def articulos():
    return jsonify({
        "mensaje":"Lista de articulos",
        "articulos": arts
    })


@app.route("/articulos/<string:producto>")
def consulta(producto):
    #list =[]
    
    #for articulo in arts:
     #   if articulo["nombre"]==producto:
      #      list.append(articulo)

    list = [articulo for articulo in arts if articulo['nombre']== producto]
    if list==[]:
        return jsonify({
            "mensaje":"articulo No encontrado"
        })
    return jsonify({
        "mensaje":"Producto encontrado",
        "Producto":list
    })

@app.route("/articulos",methods=["POST"])
def addProduct():
    articulo={
        "nombre": request.json["nombre"],
        "precio": request.json["precio"],
        "cantidad": request.json["cantidad"]
    }
    arts.append(articulo)
    return jsonify({
        "mensaje":"Producto agregado correctamente",
        "producto":arts
    })

@app.route("/articulos/<string:producto>", methods=['PUT'])
def actualizacion(producto):
    list = [articulo for articulo in arts if articulo['nombre']== producto]
    if len(list)==0:
        return jsonify({
            "mensaje":"articulo No encontrado"
        })
    else:
        list[0]["nombre"]=request.json["nombre"]
        list[0]["precio"]=request.json["precio"]
        list[0]["cantidad"]=request.json["cantidad"]
        return jsonify({
            "mensaje":"Producto encontrado",
            "Producto":list[0]
        })
    

@app.route("/articulos/<string:producto>", methods=['DELETE'])
def eliminarArticulo(producto):
    list = [articulo for articulo in arts if articulo['nombre']== producto]
    if len(list)==0:
        return jsonify({
            "mensaje":"articulo No encontrado"
        })
    else:
        arts.remove(list[0])
        return jsonify({
            "mensaje":"Producto encontrado",
            "Productos":arts
        })


if (__name__== "__main__"):
    app.run(debug=True, port=8000)


