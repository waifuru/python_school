import psycopg2


class DataConn:

    def __init__(self, ip, port, db_name, db_user, db_password):
        self.ip = ip
        self.port = port
        self.db_name = db_name
        self.db_user = db_user
        self.db_password = db_password

    def __enter__(self):
        """
        Открываем подключение с базой данных.
        """
        self.conn = psycopg2.connect(
            host=self.ip, port=self.port, database=self.db_name, user=self.db_user, password=self.db_password)
        return self.conn

    def __exit__(self, err1, err2, err3):
        """
        Закрываем подключение.
        """
        self.conn.close()


def fetch_one_record_from_sql_result(query):
    with DataConn("10.10.30.252", "5432", "countries", "postgres", "p0S+gre") as conn:
        cur = conn.cursor()
        cur.execute(query)
        return cur.fetchone()


if __name__ == '__main__':
    print("Fetching one record from remote DB.")
    print(fetch_one_record_from_sql_result('SELECT * FROM public."Capital"'))
    print("Finished.")

