#create user table
sql = """CREATE TABLE `users` ( `id` INT NOT NULL AUTO_INCREMENT , `user_id` VARCHAR(100) NOT NULL , `status` VARCHAR(200) NOT NULL , PRIMARY KEY (`id`)) ENGINE = InnoDB;"""
