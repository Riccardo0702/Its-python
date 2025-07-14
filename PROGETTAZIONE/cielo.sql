begin transaction;

set constraints all deferred;

create domain posinteger as integer
    check(value >= 0);

create domain stringam as varchar(100);

create domain codIATA as chat(3);

create table compagnia (
    nome stringam primary key,
    annofondaz posinteger
);

create table volo (
    codice posinteger not null,
    comp stringam not null,
    primary key(codice, comp),
    durataMinuti posinteger not null,
    foreign key (comp)
        references compagnia(nome)

        --posticipo la definizione della foreign
        --key (codice, comp) verso ArrPart per
        -- evitare errori
);

create table aeroporto(
    codice codIATA primary key,
    nome stringam not null,
    --posticipo la definizione della fk
    --verso luogoaeroporto, che ancora non esiste
);

create table luogoaeroporto (
    aeroporto codIATA primary key,
    città stringam not null,
    nazione stringam not null,
    foreign key (aeroport)
        references Aeroporto(codice) deferrable on delete cascade
);

alter table aeroporto
    add constraint aeroporto_luogoaeroporto_fk
        foreign key (codice)
            references luogoaeroporto(aeroporto) deferreable on delete cascade;



create table arrpart (
    codice posinteger not null,
    comp stringam not null,
    primary key (codice, comp),
    foreign key (codice, comp)
        references volo(codice, comp),
    partenza codIATA not null,
    arrivo codIATA not null,
    foreign key (partenza)
        references aeroporto(codice),
    foreign key (arrivo)
        references aeroporto(codice),
);

--foreign key di volo, posticipata per evitare errori
alter table volo
    add constraint volo_arrpart_fk
    foreign key (codice, comp)
        references arrpart(codice, comp);

commit;