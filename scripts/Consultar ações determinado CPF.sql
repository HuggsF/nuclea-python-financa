SELECT ordem.ticket
	FROM cliente, ordem where cliente.id = ordem.cliente_id AND cliente.cpf='082.242.092-22';