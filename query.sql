CREATE DATABASE db_residen;

USE db_residen;

CREATE TABLE hunian (
  id INT PRIMARY KEY AUTO_INCREMENT,
  jenis VARCHAR(255) NOT NULL,
  jml_penghuni INT NOT NULL,
  jml_kamar INT NOT NULL,
  foto VARCHAR(255)
);

CREATE TABLE apartemen (
  id INT PRIMARY KEY,
  nama_pemilik VARCHAR(255) NOT NULL,
  FOREIGN KEY (id) REFERENCES hunian(id)
);

CREATE TABLE indekos (
  id INT PRIMARY KEY,
  nama_pemilik VARCHAR(255) NOT NULL,
  nama_penghuni VARCHAR(255) NOT NULL,
  FOREIGN KEY (id) REFERENCES hunian(id)
);

CREATE TABLE rumah (
  id INT PRIMARY KEY,
  nama_pemilik VARCHAR(255) NOT NULL,
  FOREIGN KEY (id) REFERENCES hunian(id)
);
