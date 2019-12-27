import sqlite3
import data.db_session as db_session


def main():
    create_estonian_database('example.sqlite')

def create_estonian_database(filename):
    db_session.global_init(filename)


if __name__ == "__main__":
    main()