/*
-- Query: SELECT * FROM `my-blog`.users
LIMIT 0, 1000

-- Date: 2018-12-13 21:18
*/

INSERT INTO `my-blog`.`users` (`id`,`email`,`password`,`name`,`display_name`,`avatar_url`) VALUES (1,'test1@sample.com','0xABCDEF0123456789','test-user','test-user',NULL);
INSERT INTO `my-blog`.`users` (`id`,`email`,`password`,`name`,`display_name`,`avatar_url`) VALUES (2,'test2@sample.com','0xABCDEF0123456789','test-user-2','test-user-2',NULL);
INSERT INTO `my-blog`.`users` (`id`,`email`,`password`,`name`,`display_name`,`avatar_url`) VALUES (3,'test3@sample.com','0xABCDEF0123456789','test-user-3','test-user-3',NULL);
INSERT INTO `my-blog`.`users` (`id`,`email`,`password`,`name`,`display_name`,`avatar_url`) VALUES (4,'test4@sample.com','0xABCDEF0123456789','test-user-4','test-user-4',NULL);

/*
-- Query: SELECT * FROM `my-blog`.blog
LIMIT 0, 1000

-- Date: 2018-12-13 21:18
*/

INSERT INTO `my-blog`.`blog` (`title`,`publish_user_id`,`description`,`content`,`main_image`,`is_public`) VALUES ('test-1-blog-1',1,'test-1','test-1-content','test-1-main-image',1);
INSERT INTO `my-blog`.`blog` (`title`,`publish_user_id`,`description`,`content`,`main_image`,`is_public`) VALUES ('test-1-blog-2',1,'test-2','test-2-content','test-2-main-image',1);
INSERT INTO `my-blog`.`blog` (`title`,`publish_user_id`,`description`,`content`,`main_image`,`is_public`) VALUES ('test-2-blog-1',2,'test-1','test-1-content','test-1-main-image',1);
INSERT INTO `my-blog`.`blog` (`title`,`publish_user_id`,`description`,`content`,`main_image`,`is_public`) VALUES ('test-3-blog-1',3,'test-1','test-1-content','test-1-main-image',1);
INSERT INTO `my-blog`.`blog` (`title`,`publish_user_id`,`description`,`content`,`main_image`,`is_public`) VALUES ('test-3-blog-2',3,'test-2','test-2-content','test-2-main-image',1);
INSERT INTO `my-blog`.`blog` (`title`,`publish_user_id`,`description`,`content`,`main_image`,`is_public`) VALUES ('test-3-blog-3',3,'test-3','test-3-content','test-3-main-image',1);
INSERT INTO `my-blog`.`blog` (`title`,`publish_user_id`,`description`,`content`,`main_image`,`is_public`) VALUES ('test-3-blog-4',3,'test-4','test-4-content','test-4-main-image',1);
