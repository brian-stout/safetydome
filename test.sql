select combatant.id, combatant.name, species.name, type, (base_atk + plus_atk), (base_dfn + plus_dfn), (base_hp + plus_hp)
from combatant, species
where combatant.id = 1 and species.id = species_id;

select COUNT(combatant_one) as 'wins' from fight where winner_id = 1;
select COUNT(combatant_one) as 'losses' from fight
where (combatant_one = 1 or combatant_two = 1) and winner_id != 1;

select combatant_one, combatant_two, winner_id, start, TIMESTAMPDIFF(SECOND, start, finish)
from fight;

select (select name from combatant where id=winner_id), COUNT(winner_id) from fight group by winner_id order by winner_id ASC;




