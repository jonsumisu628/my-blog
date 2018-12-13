/*
-- Query: SELECT * FROM `my-blog`.users
LIMIT 0, 1000

-- Date: 2018-12-13 21:18
*/
INSERT INTO `users` (`id`,`password`,`salt`,`name`,`display_name`,`avatar_url`) VALUES (1,'test','test','test-user','test-user',NULL);
INSERT INTO `users` (`id`,`password`,`salt`,`name`,`display_name`,`avatar_url`) VALUES (2,'test2','test2','test-user-2','test-user-2',NULL);
INSERT INTO `users` (`id`,`password`,`salt`,`name`,`display_name`,`avatar_url`) VALUES (3,'test3','test3','test-user-3','test-user-3',NULL);
INSERT INTO `users` (`id`,`password`,`salt`,`name`,`display_name`,`avatar_url`) VALUES (4,'test4','test4','test-user-4','test-user-4',NULL);

/*
-- Query: SELECT * FROM `my-blog`.blog
LIMIT 0, 1000

-- Date: 2018-12-13 21:18
*/
INSERT INTO `blog` (`title`,`publish_user_id`,`description`,`content`,`main_image`,`is_public`) VALUES ('test-1-blog-1',1,'test-1','test-1-content','test-1-main-image',1);
INSERT INTO `blog` (`title`,`publish_user_id`,`description`,`content`,`main_image`,`is_public`) VALUES ('test-1-blog-2',1,'test-2','test-2-content','test-2-main-image',1);
INSERT INTO `blog` (`title`,`publish_user_id`,`description`,`content`,`main_image`,`is_public`) VALUES ('test-2-blog-1',2,'test-1','test-1-content','test-1-main-image',1);
INSERT INTO `blog` (`title`,`publish_user_id`,`description`,`content`,`main_image`,`is_public`) VALUES ('test-3-blog-1',3,'test-1','test-1-content','test-1-main-image',1);
INSERT INTO `blog` (`title`,`publish_user_id`,`description`,`content`,`main_image`,`is_public`) VALUES ('test-3-blog-2',3,'test-2','test-2-content','test-2-main-image',1);
INSERT INTO `blog` (`title`,`publish_user_id`,`description`,`content`,`main_image`,`is_public`) VALUES ('test-3-blog-3',3,'test-3','test-3-content','test-3-main-image',1);
