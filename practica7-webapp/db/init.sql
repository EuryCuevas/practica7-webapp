-- Tabla simple con el mensaje que mostrará la aplicación
CREATE TABLE mensajes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    texto VARCHAR(100) NOT NULL
);

INSERT INTO mensajes (texto) VALUES ('Hola Mundo desde MySQL con Docker Compose');