create table team(
    id int,
    teamName varchar(255),
    primary key(id),
)
create table score(
    id int,
    teamid varchar(255),
    userid varchar(255),
    score int,
    primary key(id),
    foreign key (teamid) references team(id),
    foreign key (userid) references user(id)    
)