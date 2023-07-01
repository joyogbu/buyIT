-- MySQL dump 10.13  Distrib 5.7.42, for Linux (x86_64)
--
-- Host: localhost    Database: portfolio_db
-- ------------------------------------------------------
-- Server version	5.7.42-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `cartitems`
--

DROP TABLE IF EXISTS `cartitems`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cartitems` (
  `cart_id` int(11) NOT NULL AUTO_INCREMENT,
  `cart_product_id` int(11) DEFAULT NULL,
  `cart_customer_id` int(11) DEFAULT NULL,
  `cart_quantity` int(11) DEFAULT NULL,
  `Cart_date_created` datetime DEFAULT NULL,
  PRIMARY KEY (`cart_id`),
  KEY `cart_product_id` (`cart_product_id`),
  KEY `cart_customer_id` (`cart_customer_id`),
  CONSTRAINT `cartitems_ibfk_1` FOREIGN KEY (`cart_product_id`) REFERENCES `products` (`product_id`),
  CONSTRAINT `cartitems_ibfk_2` FOREIGN KEY (`cart_customer_id`) REFERENCES `customers` (`customer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cartitems`
--

LOCK TABLES `cartitems` WRITE;
/*!40000 ALTER TABLE `cartitems` DISABLE KEYS */;
INSERT INTO `cartitems` VALUES (3,3,8,7,'2023-06-12 10:26:36'),(6,5,10,1,'2023-06-13 08:52:51'),(7,3,13,1,'2023-06-14 21:07:30'),(8,3,14,1,'2023-06-14 21:07:30'),(9,5,16,126,'2023-06-15 13:20:47'),(10,6,17,1,'2023-06-15 13:20:47'),(11,5,9,1,'2023-06-15 13:20:47'),(12,6,9,3,'2023-06-22 13:10:54'),(13,12,9,1,'2023-06-22 13:10:54');
/*!40000 ALTER TABLE `cartitems` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customers`
--

DROP TABLE IF EXISTS `customers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `customers` (
  `customer_id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_name` varchar(30) NOT NULL,
  `customer_email` varchar(30) NOT NULL,
  `customer_pass` varchar(200) NOT NULL,
  `date_added` datetime DEFAULT NULL,
  PRIMARY KEY (`customer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customers`
--

LOCK TABLES `customers` WRITE;
/*!40000 ALTER TABLE `customers` DISABLE KEYS */;
INSERT INTO `customers` VALUES (1,'','','','2023-05-29 17:50:09'),(7,'David Smith','Davs@gmail.com','$2b$12$lGr3TSTs2rDbTs.5XogWC.dATMUoOx3hoUkTpy0eVNd72ZX.3OJ/.','2023-06-09 22:54:00'),(8,'Jane Smith','Janedoe@yahoo.com','$2b$12$QCGAUzpeyw7NBMP3NSBYxOJ1SZ19TD1fiI4QG3hDOxiW2KuSMJNT2','2023-06-10 22:22:01'),(9,'Joy Ogbu','obyjoy@yahoo.com','$2b$12$K/s674rADVCAAGVGLN8kce7KDp/X7lMsgwrlvU.5bQY1JHqdvEbwW','2023-06-11 14:34:46'),(10,'Joseph Ogiku','josephogiku96@gmail.com','$2b$12$att2wJVfYn4ObogvaOPkLuK6.CGAAV5orkgXbrwLxfOMkU4kH8KLG','2023-06-13 08:52:51'),(11,'Johnathan','jamesjohnathan78@gmail.com','$2b$12$/phvS79lWqxKPPEybvbalOdaMmIBLwEwX0HoaNC0e7M3MESzw4BhG','2023-06-13 08:52:51'),(12,'Paschal','okaforpaschal018@gmail.com ','$2b$12$bPKtTygQoZgCVp7pJP1Q.OjJ/aSMD9p6ffNKLw/mLhqNLZj3jlFQO','2023-06-14 21:07:30'),(13,'Joe exotic ','01234','$2b$12$fF0CwHJmD1/iQjqtqcxr0.yKkw.BaD32D2PJ4mhhP3lGVxg/UvOWu','2023-06-14 21:07:30'),(14,'Samuel','shobayosamuel62@gmail.com','$2b$12$1JT1a4eOw9osiuFyJ43vWuT4PPDgr.4hkX3yNwxG9b3mPQmU67pn2','2023-06-14 21:07:30'),(15,'Ben','688','$2b$12$384iCmc7/8cW/JEuIwWn.eadcR/5YA.uW1HvVUFPB6dZeB.gh.vLO','2023-06-15 13:20:47'),(16,'Ben','benjaminosondu55@gmail.com','$2b$12$huNMM9CIcz9L0Fsy3DNdae82LqDDB.HRmcHKYqdHF6nqCC5eV/2iO','2023-06-15 13:20:47'),(17,'Nicanor Kyamba','nicanormuema@gmail.com','$2b$12$oIj1xC.QFaHmEeEyYar9muvAnYUzLWKwyqz184sdvRZ6l2PuCBBuy','2023-06-15 13:20:47'),(18,'tvBAdlqC','WilhelminaSeitz159@yahoo.com','$2b$12$IHAiiyyJhkkj43ZdTpEI1ew1JKPAi33ffaPKwapxbST1edRWhsDj2','2023-06-26 13:05:10');
/*!40000 ALTER TABLE `customers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `products` (
  `product_id` int(11) NOT NULL AUTO_INCREMENT,
  `product_name` tinytext,
  `product_desc` tinytext,
  `product_cat` varchar(30) DEFAULT NULL,
  `product_price` decimal(10,0) NOT NULL,
  `product_image` varchar(100) DEFAULT NULL,
  `date_added` datetime DEFAULT NULL,
  `date_updated` datetime DEFAULT NULL,
  `cust_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`product_id`),
  KEY `products_ibk_1` (`cust_id`),
  CONSTRAINT `products_ibk_1` FOREIGN KEY (`cust_id`) REFERENCES `customers` (`customer_id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` VALUES (3,'Geneva Unisex Casual Wrist Watch with bracelets','Jazz up your outfits and add sophistication to your look with this exquisite watch that has been specially designed for you','Watches',3500,'watch1.jpg','2023-06-09 18:46:24','2023-06-09 18:46:24',NULL),(4,'2 In 1 Stainless Steel Ladies Women Female Wrist Watch And Bracelet-Blue or Gold','This new fashion rhinestone analog quartz stainless steel gold wrist watch features a round case with double row chronograph decorations , which is a timepiece you will surely love. It is perfect for everyday wear.','Watches',3900,'watch2.jpg','2023-06-09 18:46:24','2023-06-09 18:46:24',NULL),(5,'Infinix Smart 7 HD 6.6\" 64GB vs 2GB RAM 5000mAh Android 12 Fingerprint','Smart 7 HDYou can take advantage of a wide range of outstanding features that complement your lifestyle with the amazing Infinix SMART 7 HD phone.','Phones',55450,'phone1.jpg','2023-06-09 19:38:11','2023-06-09 19:38:11',NULL),(6,'Senwei 4.5KVA Manul Start Generator SV5200. - Low Noise Level','This amazing generator adopts an advanced technology in design and performance peculiar only to the Senwei Brand.','Generators',120909,'generator1.jpg','2023-06-09 19:38:11','2023-06-09 19:38:11',NULL),(7,'Women Handbag For Women Bag Ladies Purse Crossbody Satchel - White','Women Handbag For Women Bag Ladies Purse Crossbody Satchel - White color','Bags',7900,'bag1.jpg','2023-06-09 19:51:31','2023-06-09 19:51:31',NULL),(8,'ADIDAS Core Neo Sport Shoes Vs Advantage','These court-inspired shoes add style with stitched 3-Stripes on the outer side and perforated 3-Stripes on the inner side. adidas men\'s sneakers mixing comfort and style','Shoes',32400,'shoe1.jpg','2023-06-09 19:51:31','2023-06-09 19:51:31',NULL),(9,'Hp Pavilion 15 - Intel Core I3 12GB RAM - 512GB SSD-Win 11','Designed to keep you productive and entertained from anywhere, the HP 39.6 cm laptop combines a long battery life with a sleek and portable, micro-edge bezel design.PROCESSOR FAMILY - INTEL CORE i3 - 12TH GENERATION INTEL PROCESSORIntel® Core™ i3-1215U','Laptops',295000,'laptop1.jpg','2023-06-14 21:07:32','2023-06-14 21:07:32',NULL),(10,'Hp Notebook 15 Core I5 -TOUCH 12GB RAM-1TB HDD+256 SSD - Win 11','Designed to keep you productive and entertained from anywhere, the HP 39.6 cm 15inch laptop combines a long battery life with a sleek and portable, micro-edge bezel design.','laptops',400000,'laptop2.jpg','2023-06-23 08:03:35','2023-06-23 08:03:35',NULL),(11,'Tecno Camon 20 FreeSpeaker 6.67inch 8GB and 256GB Android 13-GlacierGlow','TECNO Camon 20 RGBW Ultra Sensitive Sensor 64 million pixels form an ultra large sensor, equipped with an extra W channel on top of the traditional RGB color filter','phones',129300,'phone2.jpg','2023-06-23 08:21:27','2023-06-23 08:21:27',NULL),(12,'Hisense 5kg Top Load Twin Tub Washing Machine, WM503-WSPA, With One Year Warranty.','The Hisense WSPA503 twin tub semi-automatic washing machine comes with a spin dryer. Featuring a wash and spin capacity of 5kg, a water-proof and rust-proof full plastic body.','electronics',69990,'electronics1.jpg','2023-06-23 08:35:59','2023-06-23 08:35:59',NULL);
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shipping`
--

DROP TABLE IF EXISTS `shipping`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `shipping` (
  `details_id` int(11) NOT NULL AUTO_INCREMENT,
  `shipping_customer_id` int(11) DEFAULT NULL,
  `shipping_address` varchar(200) DEFAULT NULL,
  `shipping_city` varchar(100) DEFAULT NULL,
  `shipping_state` varchar(50) DEFAULT NULL,
  `shipping_country` varchar(50) DEFAULT NULL,
  `shipping_phone` varchar(11) DEFAULT NULL,
  `shipping_zip` varchar(10) DEFAULT NULL,
  `shipping_amount` decimal(10,0) DEFAULT NULL,
  `date_added` datetime DEFAULT NULL,
  `date_updated` datetime DEFAULT NULL,
  PRIMARY KEY (`details_id`),
  KEY `shipping_customer_id` (`shipping_customer_id`),
  CONSTRAINT `shipping_ibfk_1` FOREIGN KEY (`shipping_customer_id`) REFERENCES `customers` (`customer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shipping`
--

LOCK TABLES `shipping` WRITE;
/*!40000 ALTER TABLE `shipping` DISABLE KEYS */;
INSERT INTO `shipping` VALUES (1,9,'No 2 Hospital Road, Opposite Zenith Bank, Ogoja','Ogoja','Cross River','Nigeria','07088804418','550101',720,'2023-06-11 17:42:49','2023-06-11 17:42:49'),(2,9,NULL,NULL,NULL,NULL,NULL,NULL,720,'2023-06-11 19:37:53','2023-06-11 19:37:53'),(3,9,'No 2 Hospital Road, Opposite Zenith Bank, Ogoja','Ogoja','Cross River','Nigeria','07088804418','550101',720,'2023-06-11 19:37:53','2023-06-11 19:37:53'),(4,9,NULL,NULL,NULL,NULL,NULL,NULL,720,'2023-06-11 19:39:41','2023-06-11 19:39:41'),(6,9,NULL,NULL,NULL,NULL,NULL,NULL,720,'2023-06-11 19:41:32','2023-06-11 19:41:32'),(7,9,NULL,NULL,NULL,NULL,NULL,NULL,720,'2023-06-11 19:50:35','2023-06-11 19:50:35'),(8,9,NULL,NULL,NULL,NULL,NULL,NULL,720,'2023-06-11 19:52:54','2023-06-11 19:52:54'),(9,9,NULL,NULL,NULL,NULL,NULL,NULL,720,'2023-06-11 19:54:20','2023-06-11 19:54:20'),(10,9,NULL,NULL,NULL,NULL,NULL,NULL,720,'2023-06-11 19:58:28','2023-06-11 19:58:28'),(11,9,NULL,NULL,NULL,NULL,NULL,NULL,720,'2023-06-11 19:58:28','2023-06-11 19:58:28'),(12,9,NULL,NULL,NULL,NULL,NULL,NULL,720,'2023-06-11 19:58:28','2023-06-11 19:58:28'),(13,9,NULL,NULL,NULL,NULL,NULL,NULL,720,'2023-06-11 19:58:28','2023-06-11 19:58:28'),(14,9,NULL,NULL,NULL,NULL,NULL,NULL,720,'2023-06-11 19:58:28','2023-06-11 19:58:28'),(15,9,NULL,NULL,NULL,NULL,NULL,NULL,720,'2023-06-11 19:58:28','2023-06-11 19:58:28'),(16,9,NULL,NULL,NULL,NULL,NULL,NULL,720,'2023-06-11 19:58:28','2023-06-11 19:58:28'),(17,9,NULL,NULL,NULL,NULL,NULL,NULL,720,'2023-06-11 20:10:39','2023-06-11 20:10:39'),(18,9,NULL,NULL,NULL,NULL,NULL,NULL,720,'2023-06-11 20:10:39','2023-06-11 20:10:39'),(19,9,NULL,NULL,NULL,NULL,NULL,NULL,720,'2023-06-11 20:10:39','2023-06-11 20:10:39'),(20,9,NULL,NULL,NULL,NULL,NULL,NULL,720,'2023-06-11 20:10:39','2023-06-11 20:10:39'),(21,9,NULL,NULL,NULL,NULL,NULL,NULL,720,'2023-06-11 20:24:42','2023-06-11 20:24:42'),(22,9,NULL,NULL,NULL,NULL,NULL,NULL,720,'2023-06-11 20:24:42','2023-06-11 20:24:42'),(23,9,NULL,NULL,NULL,NULL,NULL,NULL,720,'2023-06-11 20:24:42','2023-06-11 20:24:42'),(24,9,NULL,NULL,NULL,NULL,NULL,NULL,720,'2023-06-11 20:24:42','2023-06-11 20:24:42'),(25,9,NULL,NULL,NULL,NULL,NULL,NULL,720,'2023-06-11 20:24:42','2023-06-11 20:24:42'),(26,9,NULL,NULL,NULL,NULL,NULL,NULL,720,'2023-06-11 20:24:42','2023-06-11 20:24:42'),(27,9,NULL,NULL,NULL,NULL,NULL,NULL,720,'2023-06-11 20:24:42','2023-06-11 20:24:42'),(28,9,NULL,NULL,NULL,NULL,NULL,NULL,720,'2023-06-11 20:24:42','2023-06-11 20:24:42'),(29,9,NULL,NULL,NULL,NULL,NULL,NULL,720,'2023-06-11 20:24:42','2023-06-11 20:24:42'),(30,9,NULL,NULL,NULL,NULL,NULL,NULL,720,'2023-06-11 20:24:42','2023-06-11 20:24:42'),(31,9,'No 2 Hospital Road, Opposite Zenith Bank, Ogoja','Ogoja','Cross River','Nigeria','07088804418','550101',720,'2023-06-11 20:40:22','2023-06-11 20:40:22'),(32,9,'No 2 Hospital Road, Opposite Zenith Bank, Ogoja','Ogoja','Cross River','Nigeria','07088804418','550101',720,'2023-06-11 20:47:48','2023-06-11 20:47:48'),(33,9,'No 2 Hospital Road, Opposite Zenith Bank, Ogoja','Ogoja','Cross River','Nigeria','07088804418','550101',720,'2023-06-11 23:07:48','2023-06-11 23:07:48'),(34,8,'No 2 Hospital Road, Opposite Zenith Bank, Ogoja','Ogoja','Cross River','Nigeria','07088804418','550101',720,'2023-06-12 10:26:36','2023-06-12 10:26:36'),(35,8,'No 2 Hospital Road, Opposite Zenith Bank, Ogoja','Ogoja','Cross River','Nigeria','07088804418','550101',720,'2023-06-12 11:19:52','2023-06-12 11:19:52'),(36,8,'No 2 Hospital Road, Opposite Zenith Bank, Ogoja','Ogoja','Cross River','Nigeria','07088804418','550101',720,'2023-06-12 11:23:03','2023-06-12 11:23:03'),(37,8,'No 2 Hospital Road, Opposite Zenith Bank, Ogoja','Ogoja','Cross River','Nigeria','07088804418','550101',720,'2023-06-12 11:24:55','2023-06-12 11:24:55'),(38,8,'No 2 Hospital Road, Opposite Zenith Bank, Ogoja','Ogoja','Cross River','Nigeria','07088804418','550101',720,'2023-06-12 11:37:58','2023-06-12 11:37:58'),(39,8,'No 2 Hospital Road, Opposite Zenith Bank, Ogoja','Ogoja','Cross River','Nigeria','07088804418','550101',720,'2023-06-12 12:05:05','2023-06-12 12:05:05'),(40,9,'No 2 Hospital Road, Opposite Zenith Bank, Ogoja','Ogoja','Cross River','Nigeria','07088804418','550101',720,'2023-06-13 08:52:51','2023-06-13 08:52:51'),(41,10,'Gshsusve','Sbeje','Heueb','Nigeria','08155392962','100001',720,'2023-06-13 08:52:51','2023-06-13 08:52:51'),(42,8,'No 2 Hospital Road, Opposite Zenith Bank, Ogoja','Ogoja','Cross River','Nigeria','07088804418','550101',720,'2023-06-14 20:34:38','2023-06-14 20:34:38');
/*!40000 ALTER TABLE `shipping` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-07-01  0:31:40
