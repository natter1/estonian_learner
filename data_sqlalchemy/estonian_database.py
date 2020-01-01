from data_sqlalchemy.db_session import DbSession


def main():
    create('example.sqlite')


def create(filename: str):
    DbSession.global_init(filename)


if __name__ == "__main__":
    main()
