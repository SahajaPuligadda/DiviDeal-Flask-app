import sqlite3

connection = sqlite3.connect('database.db')

with open('settlement_schema.sql') as f:
	connection.executescript(f.read())

with open('schema.sql') as f:
	connection.executescript(f.read())

with open('pots.sql') as f:
	connection.executescript(f.read())

with open('Items.sql') as f:
	connection.executescript(f.read())

with open('consumers.sql') as f:
	connection.executescript(f.read())

with open('col2.sql') as f:
	connection.executescript(f.read())

# cur = connection.cursor()
# count=cur.execute('''SELECT I.t_id,I.pot_id,I.description,I.created,I.amount,I.paidby, COUNT(C.transaction_id)
#   AS count FROM transactions I JOIN consumers C ON I.t_id=C.transaction_id WHERE I.pot_id={} GROUP BY transaction_id'''.format(3)).fetchall()

# print(count)

# cur.execute("INSERT INTO participants (participant_name, paid, consumed, net) VALUES (?, ?, ?, ?)",
# 		('SUCHITH','0','0','0'))

# "SELECT pot_id,description,created,amount,paidby FROM transactions "
# lists = cur.execute("SELECT T.pot_id, T.description,T.created,T.amount, T.paidby,C.c_id,C.transaction_id,C.consumer_name,C.amount FROM transactions T JOIN consumers C ON T.t_id == C.transaction_id ").fetchall()
# lists = cur.execute("SELECT participant_name,paid,consumed,net FROM participants WHERE pot_id = ?",(4,)).fetchall()
connection.commit()
connection.close()

# print(lists)
