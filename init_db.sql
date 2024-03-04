USE mydatabase;
CREATE TABLE chat_history (
    id INT AUTO_INCREMENT PRIMARY KEY,
    input_text TEXT,
    output_text TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

