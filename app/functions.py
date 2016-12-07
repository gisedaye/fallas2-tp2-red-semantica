from app.DbManager import DbManager as DB
import json
from pprint import pprint

def queryOutput(vertex, name):
	if (vertex != "") and (name != ""):
		return queryFromVertexName(vertex,name)
	else:
		return queryFromVertex(vertex)

def openDB():
    dbManager = getDbManager();
    if canOpenDB(getDbManager()):
        dbManager.open("semanticNetworkDB")
        return dbManager
    return False

def queryFromVertex(vertex):
    dbManager = openDB();
    if dbManager != false:
        eaters = dbManager.getcommand("SELECT expand( in( Related )) FROM " + vertex)
        for aux in eaters:
            output += aux.name + "\n"

    return output

def queryFromVertexName(vertex,name):
    dbManager = openDB();
    if dbManager != false:
        eaters = dbManager.getcommand("SELECT expand( in( Related )) FROM " + vertex + " WHERE name = '" + name + "'")
        for aux in eaters:
            output += aux.name + "\n"

    return output

def getDbManager():
    dbManager = DB("localhost",2424,'root','07E35090F5FBA940C9BE67DC2CB56A261CE4E6917C860DF4106C562EA49088F5')
    dbManager.connect('root','07E35090F5FBA940C9BE67DC2CB56A261CE4E6917C860DF4106C562EA49088F5')
    return dbManager


def canOpenDB(dbManager):
    if (dbManager.checkDbExists("semanticNetworkDB") == False):
        print("DB does not exist")
        return False
    return True


def addFileToDB(filename):
    dbManager = getDbManager()
    if (canOpenDB(dbManager)):
        dbManager.drop("semanticNetworkDB")

    dbManager.create("semanticNetworkDB")
    dbManager.open("semanticNetworkDB")

    with open(fileName) as data_file:
        arrayFile = json.load(data_file)

    #get vertexes
    vertexes = {x.title() : [] for x in arrayFile[0].keys()}

    #get vertexes values
    for data in arrayFile:
        for key in data.keys():
            vertexes[key.title()].append(data[key])

    for vertex in vertexes:
        ### Create Vertex
        dbManager.executecommand("CREATE CLASS " + vertex + " extends V")
        for value in vertexes[vertex]:
            ### Insert a new value
            dbManager.executecommand("INSERT INSTO " + vertex + " SET name = '" + value + "'")

    ### Create the edge for the RELATED action
    dbManager.executecommand('CREATE CLASS Related extends E')

    ### Relate all with all in the dictionary
    for data in arrayFile:
        for key in data.keys():
            auxKeys = data.keys()
            auxKeys.remove(key)
            for relatedKey in auxKeys:
                dbManager.executecommand(
                    "CREATE edge Related from ("
                    "SELECT FROM " + key.title() + " WHERE name = '" + data[key] + "'"
                    ") to ("
                    "SELECT FROM " + relatedKey.title() + " WHERE name = '" + data[relatedKey] + "'"
                    ")"
                )
