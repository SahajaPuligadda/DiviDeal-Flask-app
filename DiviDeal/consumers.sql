DROP TABLE IF EXISTS consumers;

CREATE TABLE consumers (
	c_id INTEGER PRIMARY KEY AUTOINCREMENT,
	transaction_id INTEGER NOT NULL,
	consumer_name VARCHAR NOT NULL,
	amount INTEGER NOT NULL,
	FOREIGN KEY (transaction_id) REFERENCES transactions (t_id)
	
);