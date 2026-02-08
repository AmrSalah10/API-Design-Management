from zeep import Client

def main():
    client = Client(wsdl="http://localhost:8080/calc?wsdl")
    print(client.service.Add(15, 30))

if __name__ == "__main__":
    main()
