from sqlalchemy import(
    create_engine,Column,Float,ForeignKey,Integer,String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# executing the instructions from our localhost "chinook"db
db = create_engine("postgresql:///chinook")
base = declarative_base()

# instead of connecting to the database directly,we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session =sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session=Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)

# creating a class-based model for the "Artist" table
class Artist(base):
    __tablename__="Artist"
    ArtistId=Column(Integer,primary_key=True)
    Name =Column(String)

# create a class-based model for the "Album" table
class Album(base):
    __tablename__="Album"
    AlbumId=Column(Integer,primary_key=True)
    Title =Column(String)
    ArtistId = Column(Integer, ForeignKey("Artist.ArtistId"))

# create a class-based model for the "Track" table
class Track(base):
    __tablename__ = "Track"
    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey("Album.AlbumId"))
    MediaTypeId = Column(Integer, primary_key=False)
    GenreId = Column(Integer, primary_key=False)
    Composer = Column(String)
    Milliseconds = Column(Integer, primary_key=False)
    Bytes = Column(Integer, primary_key=False)
    UnitPrice = Column(Float)





# Query 1 -select all records from the "Artist" table
artists = session.query(Artist)
for artist in artists:
    print(artist.ArtistId,artist.Name, sep="|")



    # Query 2 -select only the "Name" column from the "Artist" table
    # select_query = artist_table.select().with_only_columns([artist_table.c.Name])
    # results = connection.execute(select_query)
    # for result in results:
    #     print(result)


    # Query 3 -select only the "Queen" column from the "Artist" table
    # select_query = artist_table.select().where(artist_table.c.Name=="Queen")
    # results = connection.execute(select_query)
    # for result in results:
    #     print(result)

    # Query 4 -select only the "ArtistId" #51 from the "Artist" table
    # select_query = artist_table.select().where(artist_table.c.ArtistId== 51)
    # results = connection.execute(select_query)
    # for result in results:
    #     print(result)

    # Query 5 -select only the albums with "ArtistId" #51 from the "Artist" table
    # select_query = album_table.select().where(album_table.c.ArtistId== 51)
    # results = connection.execute(select_query)
    # for result in results:
    #     print(result)

    # Query 6 -select all tracks where the composer is "Queen" from the "Track" table


