begin transaction;
set constraints all deferred;

insert into aeroporto(codice, nome)
values
('FCO', 'Aeroporto Leonardo da Vinci'),
('MXP', 'Aeroporto di Milano Malpensa');


insert into luogoaeroporto(aeroporto, città, nazione) 
values 
('FCO', 'Roma', 'Italia'),
('MXP', 'Milano', 'Italia');

insert into compagnia (nome, annofondaz)
values
('WizardAir', 2006),
('Apitalia', 1987);

insert into volo (codice, comp, durataminuti)
values
(101, 'WizardAir', 55),
(102, 'Apitalia', 50);

insert into arrpart (codice, comp, partenza, arrivo)
values
(101, 'WizardAir', 'FCO', 'MXP'),
(102, 'Apitalia', 'MXP', 'FCO');

commit;