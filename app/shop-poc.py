import pyorient
client = pyorient.OrientDB("localhost", 2424)  # host, port

client.connect("root", "07E35090F5FBA940C9BE67DC2CB56A261CE4E6917C860DF4106C562EA49088F5")
client.db_create("shop", pyorient.DB_TYPE_GRAPH, pyorient.STORAGE_TYPE_MEMORY)
client.db_open("shop", "admin", "admin")


#Create the class for a Person
client.command("CREATE CLASS Person EXTENDS V")
#Insert a Person
client.command("INSERT INTO Person SET name = 'Eduardo', sex = 'masculino'")
#Query all
client.query("select * from Person")

#Create the class for Clothe (This will be the vertex)
client.command('CREATE CLASS Clothe extends V')
client.command("INSERT INTO Clothe SET name = 'shirt', color = 'blue'")

# Create the Wear action (This will be the edge)
client.command('create class Wear extends E')

#Eduardo wears a shirt
wear_edges = client.command(
    "create edge Wear from ("
    "select from Person where name = 'Eduardo'"
    ") to ("
    "select from Clothe where name = 'shirt'"
    ")"
)

#Who wears the shirt?
wear_shirt = client.command("select expand( in( Wear )) from Cloth where name = 'shirt'")
for animal in pea_eaters:
    print(person.name, person.sex)
'Eduardo masculino'

#What is each person wearing?
person_wear = client.command("select expand( out( Wear )) from Person")
for wear in person_wear:
    person = client.query(
                "select name from ( select expand( in('Wear') ) from Clothe where name = 'shirt' )"
            )[0]
    print(wear.name, wear.color, person.name)
'shirt blue Eduardo'
