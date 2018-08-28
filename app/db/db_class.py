import psycopg2
import psycopg2.extras


class Database:
    def __init__(self):
        pass

    # def getDbConnection(self):
    # return self.conn

    # def fetchAll(self, query):
    # cur = self._executeQuery(query)
    # rows = cur.fetchall()
    # return rows

    # def fetchOne(self, query):
    # cur = self._executeQuery(query)
    # rows = cur.fetchone()
    # return rows

    # # Execute the query and return the cursor object
    # def _executeQuery(self, query):
    # cur = self.conn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    # cur.execute(query)
    # return cur


import datetime


class DB():
    def __init__(self):
        pass

    @staticmethod
    def connectToDB(dbName=None, userName=None, dbPassword=None, dbHost=None):

        """
        connect to postgresSQL database server
        """
        conec = None

        try:
            # Start DB connection
            connectionString = "dbname='" + dbName + "'"
            if userName is not None and userName != '':
                connectionString += " user='" + userName + "'"
            if dbHost is not None and dbHost != '':
                connectionString += " host='" + dbHost + "'"
            if dbPassword is not None and dbPassword != '':
                connectionString += " password='" + dbPassword + "'"

            # test connection to the database
            print('...connecting to database...')
            conec = psycopg2.connect(connectionString)

            # create a cursor object
            _ = conec.cursor()

        except(Exception, psycopg2.DatabaseError) as error:
            print(error)

        finally:
            if conec is not None:
                return conec

    def create_tables(self):
        """ create tables in the PostgreSQL database"""

        users = """CREATE TABLE IF NOT EXISTS users (id  SERIAL PRIMARY KEY,
        username varchar(50) NOT NULL UNIQUE,
        email varchar(50) NOT NULL UNIQUE,
        password varchar(50) NOT NULL)"""

        try:
            # connect to the PostgreSQL server
            conn = self.connectToDB('test_database',
                                    'Myko', '1987', 'localhost')
            cur = conn.cursor()
            # create table one by one
            cur.execute(users)
            # close communication with the PostgreSQL database server
            cur.close()
            # commit the changes
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                print('closing table creation connectioniiii')
                conn.close()

    def insert_user(self):
        conn = None
        stmt = "INSERT INTO users (username, email, password) VALUES ('michael', 'mickie@g.com', '1234567')"

        try:
            conn = self.connectToDB('test_database', 'Myko', '1987', 'localhost')
            cur = conn.cursor()
            cur.execute(stmt)
            conn.commit()
            cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        finally:
            if conn is not None:
                conn.close()


db = DB()
