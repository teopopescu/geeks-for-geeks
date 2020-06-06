build:
	sudo rm -rf geeks_db_data
	mkdir geeks_db_data
	sudo rm -rf db_backups
	mkdir db_backups
	docker stop geeks_db_c1 || true
	docker rm geeks_db_c1 || true
	docker rmi geeks_db || true
	docker stop geeks_server_c1 || true
	docker rm geeks_server_c1 || true
	docker rmi geeks_server || true
	docker-compose up
	sleep 2

up:
	docker stop geeks_db_c1 || true
	docker stop geeks_server_c1 || true
	docker-compose up
	sleep 2

rerun:
	sudo rm -rf data
	mkdir data
	docker stop geeks_db_c1 || true
	docker stop geeks_server_c1 || true
	docker-compose up
	sleep 2



.PHONY: build up 
