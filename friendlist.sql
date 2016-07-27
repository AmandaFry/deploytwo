-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema friendslist
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema friendslist
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `friendslist` DEFAULT CHARACTER SET utf8 ;
USE `friendslist` ;

-- -----------------------------------------------------
-- Table `friendslist`.`Users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `friendslist`.`Users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `alias` VARCHAR(45) NULL,
  `email` VARCHAR(75) NULL,
  `password` VARCHAR(255) NULL,
  `birthday` DATE NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `friendslist`.`Friendslist`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `friendslist`.`Friendslist` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `friend_id` INT NOT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_Friendslist_Users_idx` (`user_id` ASC),
  INDEX `fk_Friendslist_Users1_idx` (`friend_id` ASC),
  CONSTRAINT `fk_Friendslist_Users`
    FOREIGN KEY (`user_id`)
    REFERENCES `friendslist`.`Users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Friendslist_Users1`
    FOREIGN KEY (`friend_id`)
    REFERENCES `friendslist`.`Users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
