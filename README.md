# Amazon category scrapping


## Port

* `9050` SOCKSv5 (without auth)


## Getting started

### Installation

Automated builds of the image are available on [Docker Hub](https://hub.docker.com/r/osminogin/tor-simple/) and is the recommended method of installation.

```bash
docker-compse up --build
```

## Output

#### searchResult.csv

```ini
key,Categories 
Matelas gonflable 2 personnes,"Lits, coussins et accessoires gonflables"
Matelas gonflable 2 personnes,"Lits, coussins et accessoires gonflables|Lits gonflables"
Matelas gonflable 2 personnes,Couchage pour camping et randonnée
Matelas gonflable 2 personnes,Couchage pour camping et randonnée|Matelas gonflables
Matelas gonflable 2 personnes,Meubles de salon
Matelas gonflable 2 personnes,Meubles de salon|Ensembles de meubles de salon
Matelas gonflable 2 personnes,Matelas et sommiers pour adulte
Matelas gonflable 2 personnes,Matelas et sommiers pour adulte|Matelas de lit d'adulte
```
