import rpyc

class CalculadoraService(rpyc.Service):
    def exposed_soma(self, a, b):
        print("Somando %d + %d" % (a, b))
        return a + b
    def exposed_subtracao(self, a, b):
        return a - b
    def exposed_multiplicacao(self, a, b):
        print("Multiplicando %d * %d" % (a, b))
        return a * b
    def exposed_divisao(self, a, b):
        return a / b
    def exposed_teste(self):
        print("Oi! Testando...")

if __name__ == "__main__":
    server = rpyc.ThreadedServer(CalculadoraService, port = 18811)
    server.start()