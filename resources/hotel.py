from flask_restful import Resource, reqparse


hoteis = [
    {
        'hoteis_id': 'alpha',
        'nome': 'alpha hotel',
        'estrelas': 4.4,
        'diaria': 200
    },
    {
        'hoteis_id': 'bravo',
        'nome': 'quintas hotel',
        'estrelas': 4.5,
        'diaria': 100
    },
    {
        'hoteis_id': 'delta',
        'nome': 'japao hotel',
        'estrelas': 1.0,
        'diaria': 50
    },
]

class Hoteis(Resource):
    def get(self):
        return {'hoteis':  hoteis}

class Hotel(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('estrelas')
    argumentos.add_argument('diaria')
    def find_hotel(hoteis_id):
        for hotel in hoteis:
            if hotel['hoteis_id'] == hoteis_id:
                return hotel
        return None


    def get(self, hoteis_id):
        hotel = Hotel.find_hotel(hoteis_id)
        if hotel:
            return hotel
        return {'message': 'Não encontrado, deseja adicionar: '}, 404


    def post(self, hoteis_id):


        dados = Hotel.argumentos.parse_args()
        novo_hotel = { 'hoteis_id': hoteis_id,**dados }

        hoteis.append(novo_hotel)
        return novo_hotel, 200


    def put(self, hoteis_id):
        dados = Hotel.argumentos.parse_args()
        novo_hotel = { 'hoteis_id': hoteis_id,**dados }

        hotel = Hotel.find_hotel(hoteis_id)
        if hotel:
            hotel.update(novo_hotel)
            return novo_hotel, 200
        hoteis.append(novo_hotel)
        return novo_hotel, 201

    def delete(self, hoteis_id):
        global hoteis
        hoteis = [hotel for hotel in hoteis if hotel['hoteis_id'] != hoteis_id]
        return {'message': 'Hotel deleted...'}
