from flask import Flask
from flask import render_template, request, redirect, session
from flask import flash
#from flask_bcrypt import Bcrypt

app = Flask(__name__)

#bcrypt = Bcrypt(app)# estamos creando un objeto llamado bcrypt
                    # que se realiza invocando la función Bcrypt con nuestra aplicación como argumento




PRODUCTOS = {
    "LTD-4943": {
        "tipo": "guitarra",
        "serie": "EC-256",
        "marca": "LTD",
        "codigo": "LTD-4943",
        "nombre": "LTD-EC 256",
        "stock": "43",
        "precio": [
            {
                "fecha": "2020-12-09T03:00:00.000Z", 
                "valor": 290890.98
            } ]
    },
    "TAMA-IE58H6W": {
        "tipo": "batería acústica",
        "serie": "Imperialstar",
        "marca": "TAMA",
        "codigo": "IE58H6W",
        "nombre": "Imperialstar IE58H6W 6 piezas HBK",
        "stock": "12",
        "precio": [
            {
                "fecha": "2023-22-09T03:00:00.000Z", 
                "valor": 479900
            } ]
    },
    "IBANEZ-GSR180": {
        "tipo": "bajo",
        "serie": "SR",
        "marca": "IBANEZ",
        "codigo": "GSR180",
        "nombre": "Bajo eléctrico Ibanez GSR180 - Black",
        "stock": "5",
        "precio": [
            {
                "fecha": "2023-22-09T03:00:00.000Z", 
                "valor": 259899
            } ]
    }
}




def abort_if_todo_doesnt_exist(id):
    if id not in PRODUCTOS:
        return "ESTA RUTA NO FUE ENCONTRADA", 404



@app.route('/Producto/<id>', methods=['GET','DELETE','PUT']) 
def get_producto(id):
    abort_if_todo_doesnt_exist(id)
    if request.method == 'GET':
        return PRODUCTOS[id]
    elif request.method == 'DELETE':
        del PRODUCTOS[id]
        return '', 204
    elif request.method == 'PUT':
        data = request.get_json()
        producto = {'tipo': data.get('tipo'),
                    'serie': data.get('serie'),
                    'marca': data.get('marca'),
                    'codigo': data.get('codigo'),
                    'nombre': data.get('nombre'),
                    'stock': data.get('stock'),
                    'precio': data.get('precio')
                    }
        PRODUCTOS[id] = producto
        return producto, 201
        

    
@app.route('/Productos', methods=['GET','POST'])
def get_productos():
    if request.method == 'GET':
        return PRODUCTOS
    elif request.method == 'POST':
        data = request.get_json()
        print(f'data: {data}')
        prod_id = data['marca']+'-'+data['codigo']
        PRODUCTOS[prod_id] = {'tipo': data.get('tipo'),
                    'serie': data.get('serie'),
                    'marca': data.get('marca'),
                    'codigo': data.get('codigo'),
                    'nombre': data.get('nombre'),
                    'stock': data.get('stock'),
                    'precio': data.get('precio')
                    }
        return PRODUCTOS[prod_id], 201



if __name__ == '__main__':
    app.run(debug=True)