drop database bdi;

create database bdi;

use bdi;

CREATE TABLE vacina (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255),
    fabricante VARCHAR(255),
    lote VARCHAR(255),
    tempoImunidade INT,
    estoque INT,
    validade date
);

INSERT INTO vacina (nome, fabricante, lote, tempoImunidade, estoque, validade ) VALUES ("hepatite b", "butantan", 10001, 12, 100, "2024-02-05");
INSERT INTO vacina (nome, fabricante, lote, tempoImunidade, estoque, validade ) VALUES ("hepatite b", "pfizer", 10025, 18, 4, "2025-10-12");
INSERT INTO vacina (nome, fabricante, lote, tempoImunidade, estoque, validade ) VALUES ("hepatite b", "janssen", 10300, 12, 100, "2024-09-10");
INSERT INTO vacina (nome, fabricante, lote, tempoImunidade, estoque, validade ) VALUES ("hepatite b", "fiocruz", 10562, 18, 6, "2025-09-05");
INSERT INTO vacina (nome, fabricante, lote, tempoImunidade, estoque, validade ) VALUES ("dupla adulto", "Butantan", 25603, 6, 150, "2025-09-05");
INSERT INTO vacina (nome, fabricante, lote, tempoImunidade, estoque, validade ) VALUES ("dupla adulto", "moderna", 20001, 6, 56, "2024-09-05");
INSERT INTO vacina (nome, fabricante, lote, tempoImunidade, estoque, validade ) VALUES ("dupla adulto", "fiocruz", 28943, 6, 5, "2023-09-05");
INSERT INTO vacina (nome, fabricante, lote, tempoImunidade, estoque, validade ) VALUES ("triplice viral", "fio cruz", 30021, 18, 26, "2024-05-05");
INSERT INTO vacina (nome, fabricante, lote, tempoImunidade, estoque, validade ) VALUES ("triplice viral", "butantan", 30256, 24, 150, "2024-12-05");
INSERT INTO vacina (nome, fabricante, lote, tempoImunidade, estoque, validade ) VALUES ("triplice viral", "astrazeneca", 30300, 24, 9, "2025-01-05");
INSERT INTO vacina (nome, fabricante, lote, tempoImunidade, estoque, validade ) VALUES ("influenza", "janssen", 40001, 6, 63, "2024-09-05");
INSERT INTO vacina (nome, fabricante, lote, tempoImunidade, estoque, validade ) VALUES ("influenza", "fio cruz", 40023, 6, 4, "2024-09-05");
INSERT INTO vacina (nome, fabricante, lote, tempoImunidade, estoque, validade ) VALUES ("influenza", "moderna", 43210, 8, 120, "2025-09-05");
INSERT INTO vacina (nome, fabricante, lote, tempoImunidade, estoque, validade ) VALUES ("influenza", "pfizer", 44044, 8, 45, "2024-12-05");
INSERT INTO vacina (nome, fabricante, lote, tempoImunidade, estoque, validade ) VALUES ("influenza", "butantan", 43234, 8, 5, "2023-12-05");
INSERT INTO vacina (nome, fabricante, lote, tempoImunidade, estoque, validade ) VALUES ("hpv", "butantan", 50001, 24, 50, "2023-12-05");
INSERT INTO vacina (nome, fabricante, lote, tempoImunidade, estoque, validade ) VALUES ("hpv", "fiocruz", 50126, 24, 2, "2023-12-25");
INSERT INTO vacina (nome, fabricante, lote, tempoImunidade, estoque, validade ) VALUES ("covid", "fiocruz", 60126, 6, 100, "2023-12-25");
INSERT INTO vacina (nome, fabricante, lote, tempoImunidade, estoque, validade ) VALUES ("covid", "butantan", 60001, 6, 68, "2025-06-25");
INSERT INTO vacina (nome, fabricante, lote, tempoImunidade, estoque, validade ) VALUES ("covid", "astrazeneca", 60025, 6, 5, "2024-04-25");
INSERT INTO vacina (nome, fabricante, lote, tempoImunidade, estoque, validade ) VALUES ("covid", "janssen", 60780, 6, 2, "2024-12-25");
INSERT INTO vacina (nome, fabricante, lote, tempoImunidade, estoque, validade ) VALUES ("dtpa", "butantan", 70780, 48, 15, "2024-12-25");
INSERT INTO vacina (nome, fabricante, lote, tempoImunidade, estoque, validade ) VALUES ("dtpa", "fiocruz", 70050, 48, 12, "2025-11-25");

select * from vacina