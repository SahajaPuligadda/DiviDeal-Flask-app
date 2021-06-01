DROP TABLE IF EXISTS col2;

CREATE TABLE col2 (
	c_id	INTEGER,
	col2values	REAL,
	col2_id	 INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	FOREIGN KEY(c_id) REFERENCES consumers(c_id)
);