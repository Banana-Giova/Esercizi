-- 1. Politiche di accesso ai dati: non permettere ad alcun utente di cambiare gli id artificiali
REVOKE UPDATE (id) ON Persona FROM PUBLIC;
REVOKE UPDATE (persona) ON Studente FROM PUBLIC;
REVOKE UPDATE (persona) ON Docente FROM PUBLIC;


-- 2. Trigger compl_1 per INSERT into Persona
create or replace function V_Persona_gen_compl_1() returns trigger as $V_Persona_gen_compl_1$
-- la funzione vedrà 'new' come argomento
declare isError boolean := false;
begin
isError = NOT EXISTS (
    SELECT persona FROM Studente WHERE persona = new.id
    UNION ALL
    SELECT persona FROM Docente WHERE persona = new.id
);
if (isError) then raise exception 'Vincolo V_Persona_gen_compl_1 violato (persona.id=%)', new.id;
end if;
return new; -- lascia passare la ennupla; in realtà il valore di ritorno per i trigger ‘after’ è ignorato, non lo sarebbe per i trigger ‘before’
end; 
$V_Persona_gen_compl_1$ language plpgsql;
create constraint trigger V_Persona_gen_compl_1_persona
after insert on Persona
deferrable -- affinché sia deferrable, il trigger deve essere di tipo ‘constraint’
for each row execute procedure V_Persona_gen_compl_1();


-- 3. Trigger compl_2 per DELETE from Studente or Docente
create or replace function V_Persona_gen_compl_2() returns trigger as $V_Persona_gen_compl_2$
-- la funzione vedrà 'old' come argomento
declare isError boolean := false;
begin
isError := EXISTS(
    SELECT * FROM (Persona p LEFT OUTER JOIN Studente s ON p.id = s.persona) LEFT OUTER JOIN Docente d ON p.id = d.persona
    WHERE p.id = old.persona AND (s.persona IS NULL) AND (d.persona IS NULL)
);
if (isError) then raise exception 'Vincolo V_Persona_isa_compl_2 violato (persona=%)', old.persona;
end if;
return old; -- il valore di ritorno per i trigger ‘after’ è ignorato, non lo è per i trigger ‘before’
end;$V_Persona_gen_compl_2$ language plpgsql;
create constraint trigger V_Persona_gen_compl_2_studente
after delete on Studente
deferrable for each row execute procedure V_Persona_gen_compl_2();
create constraint trigger V_Persona_gen_compl_2_docente
after delete on Docente
deferrable for each row execute procedure V_Persona_gen_compl_2();