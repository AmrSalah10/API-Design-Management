import addressbook_pb2
import sys
import json

# proto buffers
addressbook = addressbook_pb2.AddressBook()

for i in range(10):
    # proto data
    person = addressbook.people.add()
    person.id = 1234
    person.name = "John Doe"
    person.email = "jdoe@example.com"
    
    phone = person.phones.add()
    phone.number = "555-4321"
    phone.type = addressbook_pb2.Person.PHONE_TYPE_HOME

binary_serialized_data = addressbook.SerializeToString()
print(sys.getsizeof(binary_serialized_data)) # 503 bytes

with open("proto.out", "wb") as f:
    f.write(binary_serialized_data)


# json
addressbook_json = []

for i in range(10):
    addressbook_json.append({
        'id': 1234,
        'name': 'John Doe',
        'email': 'jdoe@example.com',
        'phones': [{'number': '555-4321', 'type': 'HOME'}]
    })


json_serialized_data = json.dumps(addressbook_json)
print(sys.getsizeof(json_serialized_data)) # 1191 bytes

with open("json.out", "w") as f:
    f.write(json_serialized_data)
