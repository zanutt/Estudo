import random
from faker import Faker

fake = Faker('pt_BR')

def make_route(num_routes):
    routes = []
    for _ in range(num_routes):
        route = {
            'ip': fake.ipv4_private(),
            'latencia': fake.random_number(digits=2, fix_len=True),
        }
        routes.append(route)
    return routes

if __name__ == '__main__':
    num_routes = random.randint(3, 10)  # Gera um número aleatório entre 3 e 10
    routes = make_route(num_routes)
    print(routes)