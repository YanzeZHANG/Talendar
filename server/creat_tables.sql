DROP TABLE IF EXISTS student_info;

DROP TABLE IF EXISTS user_info;

CREATE TABLE user_info(
    userid int(11) NOT NULL AUTO_INCREMENT,
    username varchar(255) COLLATE utf8mb4_unicode_ci NULL,
    mailbox  varchar(255) COLLATE utf8mb4_unicode_ci NULL,
    passwd   varchar(255) COLLATE utf8mb4_unicode_ci NULL,
    CONSTRAINT userinforpk PRIMARY KEY (userid)
);

DROP TABLE IF EXISTS student_info;

CREATE TABLE student_info(
    stuid int(10) NOT NULL,
    userid int(11) NOT NULL,
    info_passwd int(11) NOT NULL,
    CONSTRAINT studentinfopk PRIMARY KEY (stuid),
    CONSTRAINT studentinfofk FOREIGN KEY (userid) REFERENCES user_info(userid)
);

DROP TABLE IF EXISTS tags;

CREATE TABLE tags(
    tagid int(11) NOT NULL AUTO_INCREMENT,
    content varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
    createdby int(11) NULL,
    CONSTRAINT tagpk PRIMARY KEY (tagid)
);

DROP TABLE IF EXISTS works;

CREATE TABLE works(
    tagid int(11) NOT NULL AUTO_INCREMENT,
    userid int(11) NOT NULL,
    name varchar(255) NOT NULL,
    location varchar(255) NULL,
    begintime char(12) NULL,
    endtime char(12) NULL,
    notation varchar(255) NULL,
    child varchar(255) NULL,
    attach varchar(255) NULL,
    tagnum int(11) NULL,
    tags varchar(255) NULL,
    repeat boolean False,
    frequency int(11) NULL,
    
)
