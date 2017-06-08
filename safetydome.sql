CREATE TABLE type (
		name VARCHAR(255) PRIMARY KEY
	);

CREATE TABLE attack (
		id SERIAL PRIMARY KEY,
		name TEXT NOT NULL,
		type TEXT NOT NULL REFERENCES type(name),
		min INTEGER NOT NULL,
		max INTEGER NOT NULL,
		speed TIME NOT NULL
	);

CREATE TABLE species (
		id SERIAL PRIMARY KEY,
		name TEXT NOT NULL,
		type TEXT NOT NULL REFERENCES type(name),
		base_atk INTEGER NOT NULL,
		base_dfn INTEGER NOT NULL,
		base_hp INTEGER NOT NULL
	);

CREATE TABLE combatant (
		id SERIAL PRIMARY KEY,
		name TEXT NOT NULL,
		species_id INTEGER NOT NULL REFERENCES species(id),
		plus_atk INTEGER NOT NULL,
		plus_dfn INTEGER NOT NULL,
		plus_hp INTEGER NOT NULL
	);

CREATE TABLE species_attack (
		species_id INTEGER NOT NULL REFERENCES species(id),
		attack_id INTEGER NOT NULL REFERENCES attack(id)
	);

CREATE TABLE fight (
		combatant_one INTEGER NOT NULL REFERENCES combatant(id),
		combatant_two INTEGER NOT NULL REFERENCES combatant(id),
		winner_id INTEGER REFERENCES combatant(id),
		start DATETIME NOT NULL,
		finish DATETIME NOT NULL
	);

INSERT INTO type (name) VALUES ('Physical'), ('Biological'), ('Radioactive'),
	('Chemical'), ('Technological'), ('Mystical'), ('Mineral');


INSERT INTO species (name, type, base_atk, base_dfn, base_hp) VALUES
	('human', 'Physical', 100, 100, 100),
	('zombie', 'Biological', 50, 110, 140),
	('mutant', 'Radioactive', 110, 140, 50),
	('ooze', 'Chemical', 140, 50, 110),
	('robot', 'Technological', 50, 140, 110),
	('wendigo', 'Mystical', 140, 110, 50),
	('xorn', 'Mineral', 110, 50, 140),

	('monkey', 'Physical', 50, 200, 50),
	('sentient offal', 'Biological', 150, 0, 150),
	('imaginary dragon', 'Radioactive', 50, 50, 200),
	('toxic revenger', 'Chemical', 200, 50, 50),
	('land mine', 'Technological', 300, 0, 0),
	('ghost', 'Mystical', 150, 150, 0),
	('large rock', 'Mineral', 0, 150, 150);

INSERT INTO attack (name, type, min, max, speed) VALUES
	('punch','Physical',15,15, '1'),
	('kick','Physical',20,40, '1'),
	('suplex','Physical',30,90, '4'),

	('venom bite','Biological',5,55, '2'),
	('loogie','Biological',10,230, '8'),
	('disease','Biological',15,285, '10'),

	('alpha particle','Radioactive',0,30, '1'),
	('beta particle','Radioactive',0,90, '3'),
	('gamma particle','Radioactive',0,150, '5'),

	('acid spit','Chemical',60,90, '5'),
	('lye vomit','Chemical',90,120, '7'),
	('hydroxic acid','Chemical',120,150, '9'),

	('buzz saw','Technological',60,60, '4'),
	('laser','Technological',120,120, '8'),
	('thermonuclear warhead','Technological',240,240, '16'),

	('magic missle','Mystical',10,20, '1'),
	('fireball','Mystical',40,80, '4'),
	('lightning bolt','Mystical',80,160, '8'),

	('pocket sand','Mineral',30,60, '3'),
	('very small rocks','Mineral',5,85, '3'),
	('rock smash','Mineral',0,90, '3'),

	('crushing boredom','Mineral',30000,30000, '3320'),
	('explode','Physical',30,30, '2');

INSERT INTO species_attack (species_id, attack_id) VALUES
	(1, 1), (1, 2), (1, 3),
	(2, 4), (2, 5), (2, 6),
	(3, 7), (3, 8), (3, 9),
	(4, 10), (4, 11), (4, 12),
	(5, 13), (5, 14), (5, 15),
	(6, 16), (6, 17), (6, 18),
	(7, 19), (7, 20), (7, 21),

	(8, 1), (8, 5), (8, 19),
	(9, 6), (9, 11), (9, 15),
	(11, 4), (11, 12), (11, 13),
	(12, 15), (12, 23),
	(13, 18), (13, 7), (13, 2),
	(14, 22);

