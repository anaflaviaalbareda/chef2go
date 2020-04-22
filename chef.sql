-- MySQL dump 10.13  Distrib 8.0.11, for macos10.13 (x86_64)
--
-- Host: localhost    Database: chef
-- ------------------------------------------------------
-- Server version	8.0.11

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8mb4 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Almuerzos`
--

DROP TABLE IF EXISTS `Almuerzos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Almuerzos` (
  `Almuerzos_id` int(11) NOT NULL AUTO_INCREMENT,
  `Fecha` datetime DEFAULT NULL,
  `Nombre` varchar(45) DEFAULT NULL,
  `Telefono` varchar(45) DEFAULT NULL,
  `Direccion` varchar(45) DEFAULT NULL,
  `opcion` varchar(55) DEFAULT NULL,
  PRIMARY KEY (`Almuerzos_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;


--
-- Table structure for table `Clases`
--

DROP TABLE IF EXISTS `Clases`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Clases` (
  `clases_id` int(11) NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(255) NOT NULL,
  `Descripcion` longtext NOT NULL,
  `Ingredientes` longtext NOT NULL,
  `Pagado` tinyint(1) NOT NULL,
  PRIMARY KEY (`clases_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Colacion`
--

DROP TABLE IF EXISTS `Colacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Colacion` (
  `idColacion` int(11) NOT NULL AUTO_INCREMENT,
  `Entrada` varchar(45) DEFAULT NULL,
  `Entrada_Descripcion` varchar(255) DEFAULT NULL,
  `Principal` varchar(45) DEFAULT NULL,
  `Principa_Descripcion` varchar(255) DEFAULT NULL,
  `Postre` varchar(45) DEFAULT NULL,
  `Postre_Descripcion` varchar(255) DEFAULT NULL,
  `Precio` int(11) DEFAULT NULL,
  `Precio_sin_postre` int(11) DEFAULT NULL,
  `dia` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idColacion`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Inscritos_clase`
--

DROP TABLE IF EXISTS `Inscritos_clase`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE IF NOT EXISTS `Inscritos_clase` (
  `insc_id` INT NOT NULL AUTO_INCREMENT,
  `Nombre` VARCHAR(55) NULL,
  `Telefono` VARCHAR(55) NULL,
  `Email` VARCHAR(55) BINARY NULL,
  `Pagado` TINYINT(1) NOT NULL DEFAULT 0,
  `clases_id` INT NOT NULL,
  PRIMARY KEY (`insc_id`, `clases_id`),
  INDEX `fk_Inscritos_clase_Clases_idx` (`clases_id` ASC),
  CONSTRAINT `fk_Inscritos_clase_Clases`
    FOREIGN KEY (`clases_id`)
    REFERENCES `Clases` (`clases_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;
/*!40101 SET character_set_client = @saved_cs_client */;


/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-04-07 19:37:17
