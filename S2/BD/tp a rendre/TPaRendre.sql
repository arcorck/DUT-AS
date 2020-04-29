-- -- Question 1
-- delimiter |
-- drop procedure if exists completeIncompatible|
-- create procedure completeIncompatible()
-- begin
--     declare fini int default false;
--     declare comp_1 varchar(4);
--     declare comp_2 varchar(4);
--     declare ingredients cursor for 
--         select refComp_1, refComp_2 from INCOMPATIBLE;
--     declare continue handler for not found set fini = true;
--     open ingredients;
--     while not fini do
--         fetch ingredients into comp_1, comp_2;
--         if not fini then
--             INSERT INTO INCOMPATIBLE VALUES (comp_2, comp_1);
--         end if;
--     end while;
--     close ingredients;
-- end|
-- delimiter ;

-- call completeIncompatible();


-- Question 2
delimiter |
drop function if exists effectuerCommande|
create function effectuerCommande() returns varchar(500)
BEGIN
    declare res varchar(500) default '';
    declare fini int default false;
    declare ref varchar(4);
    declare nom varchar(20);
    declare qte integer;
    declare nomform varchar(20);
    declare ingredients cursor for 
        select refcomp, nomComp, qte, nomform
        from COMPOSE natural join CONSTITUER natural join FORMULE;
    declare continue handler for not found set fini = true;
    open ingredients;
    while not fini do
        fetch ingredients into ref, nom, qte, nomform;
        if not fini then
            set res := concat(res,ref);
            set res := concat(res,concat(' ',concat(nom,'\n')));
            -- set res := concat(res,concat('    ',concat(nomform, concat('  ', concat(convert(qte,char),'\n')))));
        end if;
    end while;
    close ingredients;
    return res;
end|
delimiter ;

select effectuerCommande();