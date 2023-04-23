from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

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
        abort(404, message="Producto {} no existe".format(id))

parser = reqparse.RequestParser()
parser.add_argument('tipo')
parser.add_argument('serie')
parser.add_argument('marca')
parser.add_argument('codigo')
parser.add_argument('nombre')
parser.add_argument('stock')
parser.add_argument('precio')

class Producto(Resource):
    def get(self, id):
        abort_if_todo_doesnt_exist(id)
        return PRODUCTOS[id]
    

    def delete(self, id):
        abort_if_todo_doesnt_exist(id)
        del PRODUCTOS[id]
        return '', 204

    def put(self, id):
        args = parser.parse_args()
        producto = {'tipo': args['tipo'],
                    'serie': args['serie'],
                    'marca': args['marca'],
                    'codigo': args['codigo'],
                    'nombre': args['nombre'],
                    'stock': args['stock'],
                    'precio': args['precio']
                    }
        PRODUCTOS[id] = producto
        return producto, 201
    

    
class Productos(Resource):
    def get(self):
        return PRODUCTOS
    
    def post(self):
        args = parser.parse_args()
        prod_id = args['marca']+'-'+args['codigo']
        PRODUCTOS[prod_id] = {'tipo': args['tipo'],
                    'serie': args['serie'],
                    'marca': args['marca'],
                    'codigo': args['codigo'],
                    'nombre': args['nombre'],
                    'stock': args['stock'],
                    'precio': args['precio']
                    }
        return PRODUCTOS[prod_id], 201
    
api.add_resource(Productos, '/productos')
api.add_resource(Producto, '/productos/<id>')


if __name__ == '__main__':
    app.run(debug=True)