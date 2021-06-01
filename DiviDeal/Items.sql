DROP TABLE IF EXISTS transactions;

CREATE TABLE transactions (
	t_id INTEGER PRIMARY KEY AUTOINCREMENT,
	pot_id INTEGER NOT NULL,
	description VARCHAR NOT NULL,
	created VARCHAR NOT NULL ,
	amount INTEGER NOT NULL,
	paidby VARCHAR NOT NULL,
    split VARCHAR NOT NULL,
	FOREIGN KEY (pot_id) REFERENCES pots (p_id)
);