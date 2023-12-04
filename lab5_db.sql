CREATE SCHEMA IF NOT EXISTS `iot_db` DEFAULT CHARACTER SET utf8mb3;
USE `iot_db`;

CREATE TABLE IF NOT EXISTS `review`
(
    `id`       INT         NOT NULL AUTO_INCREMENT,
    `rating`   VARCHAR(45) NULL DEFAULT NULL,
    `plot`     VARCHAR(45) NULL DEFAULT NULL,
    `acting`   VARCHAR(45) NULL DEFAULT NULL,
    `music`    VARCHAR(45) NULL DEFAULT NULL,
    `graphics` VARCHAR(45) NULL DEFAULT NULL,
    `film_id`  INT         NOT NULL,
    PRIMARY KEY (`id`, `film_id`)
)
    ENGINE = InnoDB
    AUTO_INCREMENT = 6
    DEFAULT CHARACTER SET = utf8mb4;

CREATE TRIGGER `review_insert_before`
    BEFORE INSERT
    ON `review`
    FOR EACH ROW
BEGIN
    IF NOT EXISTS (SELECT *
                   FROM `film`
                   WHERE `id` = NEW.`film_id`) THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Неможливо додати відгук до фільму, який не існує.';
    END IF;
END;

CREATE TRIGGER `budget_insert_before`
    BEFORE INSERT
    ON `budget`
    FOR EACH ROW
BEGIN
    IF REGEXP_INSTR(NEW.`actors_fee`, '00$') > 0 THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Значення actors_fee не може закінчуватися двома нулями.';
    END IF;
END;

SELECT *
FROM `budget`;

CREATE TRIGGER `director_insert_before`
    BEFORE INSERT
    ON director
    FOR EACH ROW
BEGIN
    IF NEW.`name` NOT IN ('Christopher', 'Petro', 'Mel', 'Taras') THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Допустимі значення для name: Christopher, Petro, Mel, Taras.';
    END IF;
END;

SELECT *
FROM director;

USE `iot_db`;

CREATE TRIGGER `actor_insert_before`
    BEFORE INSERT
    ON actor
    FOR EACH ROW
BEGIN
    IF LEFT(NEW.`name`, 1) <> LEFT(NEW.`surname`, 1) THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Перша літера у значенні імені повинна відповідати першій літері значення прізвища.';
    END IF;
END;

SELECT *
FROM iot_db.actor;
# 2a
DELIMITER //
CREATE PROCEDURE IF NOT EXISTS insert_into_movie_description(
    IN p_plot VARCHAR(500),
    IN p_scene VARCHAR(45),
    IN p_action_time VARCHAR(45),
    IN p_awards VARCHAR(45),
    IN p_age_group VARCHAR(45)
)
BEGIN
    INSERT INTO `movie_description` (`plot`, `scene`, `action_time`, `awards`, `age_group`)
    VALUES (p_plot, p_scene, p_action_time, p_awards, p_age_group);
END;
//
DELIMITER ;


CREATE PROCEDURE `insert_movie_descriptions`()
BEGIN
    DECLARE i INT;

    SET i = 1;

    WHILE i <= 10
        DO
            INSERT INTO `movie_description`
                (`plot`)
            VALUES (CONCAT('Movie description ', i));

            SET i = i + 1;
        END WHILE;
END;

CALL `insert_movie_descriptions`;

SELECT *
FROM `movie_description`;


CREATE FUNCTION `get_actors_fee_stat`(
    `function_type` VARCHAR(255)
)
    RETURNS DOUBLE
    DETERMINISTIC
    READS SQL DATA
BEGIN
    DECLARE result DOUBLE;
    CASE function_type
        WHEN 'MAX' THEN SELECT MAX(`actors_fee`)
                        INTO result
                        FROM budget;
        WHEN 'MIN' THEN SELECT MIN(actors_fee)
                        INTO result
                        FROM budget;
        WHEN 'SUM' THEN SELECT SUM(actors_fee)
                        INTO result
                        FROM budget;
        WHEN 'AVG' THEN SELECT AVG(actors_fee)
                        INTO result
                        FROM budget;
        END CASE;
    RETURN result;
END;

SELECT get_actors_fee_stat('SUM');


