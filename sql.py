# 用户表
USERS = """
CREATE TABLE IF NOT EXISTS users(
  id INT(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  username VARCHAR(255) NOT NULL,
  password VARCHAR(255) NOT NULL,
  UNIQUE INDEX username_index(username ASC)
)
"""

tables = [USERS]
