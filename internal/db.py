
# TODO: Have to rewrite this with aiosqlite or something better, and add the defs to get and record the stats of songs played.

# import mysql.connector


# class Database:
#     def __init__(self) -> None:
#         self.db = mysql.connector.connect(
#             host='localhost', user='root', password='mysql', database='testdb2')

#     def add_server(self, server_id, channel_id, msg_id, log_ch_id="NULL"):
#         cursor = self.db.cursor()
#         cursor.execute("INSERT INTO server_data VALUES (?, ?, ?, ?)",
#                        (server_id, channel_id, msg_id, log_ch_id,))
#         self.db.commit()

#     def remove_server(self, server_id):
#         cursor = self.db.cursor()
#         cursor.execute(
#             f"DELETE FROM server_data WHERE server_id = {server_id}")
#         self.db.commit()

#     def check_server(self, server_id):
#         cursor = self.db.cursor()
#         cursor.execute(f"SELECT server_id FROM server_data")
#         return server_id in [i[0] for i in cursor]

#     def get_msg_id(self, server_id):
#         cursor = self.db.cursor()
#         cursor.execute(
#             f"SELECT message_id FROM server_data WHERE server_id = {server_id}")
#         msgId = cursor.fetchone()
#         return msgId[0]

#     def get_ch_id(self, server_id):
#         cursor = self.db.cursor()
#         cursor.execute(
#             f"SELECT channel_id FROM server_data WHERE server_id = {server_id}")
#         chId = cursor.fetchone()
#         return chId[0]

#     def get_log_ch_id(self, server_id):
#         cursor = self.db.cursor()
#         cursor.execute(
#             f"SELECT log_ch_id FROM server_data WHERE server_id = {server_id}")
#         logChId = cursor.fetchone()
#         return logChId[0]
