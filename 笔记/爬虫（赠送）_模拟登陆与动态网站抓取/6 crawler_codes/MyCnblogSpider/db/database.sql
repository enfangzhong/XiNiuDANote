CREATE DATABASE cnblogsdb DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
CREATE TABLE `cnblogsinfo` (
  `linkmd5id` char(32) NOT NULL COMMENT 'url md5编码id',
  `title` text COMMENT '标题',
  `description` text COMMENT '描述',
  `link` text  COMMENT 'url链接',
  `read_num` text  COMMENT '博客阅读数',
  `comment_num` text COMMENT '评论数',
  `update_time` datetime DEFAULT NULL  COMMENT '最后更新时间',
  PRIMARY KEY (`linkmd5id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

