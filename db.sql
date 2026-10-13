-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema cinepedia
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema cinepedia
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `cinepedia` DEFAULT CHARACTER SET utf8 ;
USE `cinepedia` ;

-- -----------------------------------------------------
-- Table `cinepedia`.`usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cinepedia`.`usuarios` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(255) NULL,
  `apellido` VARCHAR(255) NULL,
  `email` VARCHAR(255) NULL,
  `password` VARCHAR(255) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cinepedia`.`peliculas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cinepedia`.`peliculas` (
  `id` INT NOT NULL,
  `nombre` VARCHAR(255) NULL,
  `director` VARCHAR(255) NULL,
  `fecha_estreno` DATETIME NULL,
  `sinopsis` TEXT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  `usuario_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_peliculas_usuarios_idx` (`usuario_id` ASC) VISIBLE,
  CONSTRAINT `fk_peliculas_usuarios`
    FOREIGN KEY (`usuario_id`)
    REFERENCES `cinepedia`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
