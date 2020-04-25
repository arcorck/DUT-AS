-- Question 1
delimiter |
drop procedure if exists completeIncompatible|
create procedure completeIncompatible()
begin
    declare fini int default false;
    declare comp_1 varchar(4);
    declare comp_2 varchar(4);
    declare ingredients cursor for 
        select refComp_1, refComp_2 from INCOMPATIBLE;
    declare continue handler for not found set fini = true;
    open ingredients;
    while not fini do
        fetch ingredients into comp_1, comp_2;
        INSERT INTO INCOMPATIBLE VALUES (comp_2, comp_1);
    end while;
    close ingredients;
end|
delimiter ;

