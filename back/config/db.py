from pony import orm
from pony.orm.dbapiprovider import OperationalError
from pony.options import CUT_TRACEBACK



db = orm.Database()

def init_db():
    try:
        db.bind(provider="mysql", host="144.91.70.164",
                user="root", password="izigo.online@root.3344", db="izigo")
    except OperationalError as e:
        print(e)
    print("initialisation de la db")

    db.generate_mapping()

# def init_db():
#     try:
#         db.bind(provider="sqlite", filename="database.sqlite", create_db=True)
#     except Exception as e:
#         print(e)
#
#     db.generate_mapping(create_tables=True)

