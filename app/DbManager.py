import pyorient

class DbManager:

    def __init__(self,host, port, user, password):
        self.client = pyorient.OrientDB(host,port)
        self.user = user
        self.password = password
        self.session_id = None

    def connect(self):
        self.session_id = self.client.connect(self.user, self.password )

    def connect(self, user, password):
        self.session_id = self.client.connect(user, password )

    def checkDbExists(self,db_name):
        return self.client.db_exists(db_name, pyorient.STORAGE_TYPE_MEMORY)

    def create(self, db_name):
        if not self.checkDbExists(db_name):
            self.client.db_create( db_name, pyorient.DB_TYPE_GRAPH, pyorient.STORAGE_TYPE_MEMORY )

    def open(self,db_name):
        if self.checkDbExists(db_name):
            self.client.db_open( db_name, self.user, self.password)

    def drop(self,db_name):
        self.client.db_drop(db_name)

    def closeConnection(self):
        self.client.db_close()

    def executecommand(self, command):
        self.client.command(command)

    def getcommand(self, command):
        return self.client.command(command)

    def executeQuery(self, query):
        self.client.execute(query)
