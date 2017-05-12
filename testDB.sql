PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE STUDENT(ID INT primary key not null, name char[10]);
INSERT INTO "STUDENT" VALUES(1,'leslie');
COMMIT;
