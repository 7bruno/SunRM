# SunRM

## Base URL

```
Production: https://capstone-q3-sunrn-production.herokuapp.com
Development: https://capstone-q3-sunrn.herokuapp.com

```

# Endpoints

## GET /hsp

get all ufs in the database

### Response Return

```json
{
  "uf": ["LIST OF ALL CITIES IN THE DATABASE"]
}
```

## GET /hsp/<your-ufs-name>

get all ufs in the database

(/hsp/<pernambuco>)

### Response Return

```json
{
  "data": [
    {
      "city": "Petrolina",
      "uf": "PERNAMBUCO",
      "id": 3185
    },
    {
      "city": "Jatobá",
      "uf": "PERNAMBUCO",
      "id": 3186
    }
  ]
}
```

## POST /lead

body to create a simulation of a lead

```json
{
  "name": "USER NAME",
  "email": "USER EMAIL",
  "phone": "USER PHONE",
  "month_energy": 150, // USER ENERGY IN THE MONTH
  "month_value": 120, // USER ENERGY COST IN THE MONTH
  "hsp_id": 1 // UF ID OF USER LOCALIZATION (use route to get the id /hsp/your-city-name)
}
```

### Response Return

```json
{
  "inversor": {
    "brand": "Growatt",
    "model": "Mic1500tl-x",
    "id": 2,
    "price": 2418.56,
    "power": 1500
  },
  "panel": {
    "brand": "Canadian",
    "model": "CS3IU-355P",
    "id": 8,
    "price": 769.0,
    "power": 355,
    "quantity": 4.0
  },
  "energy_cost": 36000,
  "system_cost": 5494.5599999999995,
  "worker_cost": 1098.912,
  "project_cost": 2197.824,
  "eletric_materials_cost": 549.456,
  "maintanance_cost": 686.8199999999999,
  "total_system_cost": 10027.572,
  "roi_years": 6.963591666666667
}
```

## ENDPOINTS TO SELLERS

## GET /register

register a seller

body

```json
{
  "name": "SELLER NAME",
  "email": "SELLER EMAIL",
  "password": "SELLER PASSWORD"
}
```

### Response Return

```json
{
  "auth_token": "SELLER TOKEN",
  "user": {
    "id": 1,
    "name": "SELLER NAME",
    "email": "SELLER EMAIL"
  }
}
```

## GET /login

login seller

body

```json
{
  "email": "SELLER EMAIL",
  "password": "SELLER PASSWORD"
}
```

### Response Return

```json
{
  "refresh_token": "SELLER REFRESH TOKEN",
  "auth_token": "SELLER TOKEN",
  "user": {
    "id": 1,
    "name": "SELLER NAME",
    "email": "SELLER EMAIL"
  }
}
```

## GET /lead

to get all leads and simulations in the system

header

```json
Authorization: 'Bearer ' + <TOKEN>
```

### Response Return

```json
[
  {
    "name": "USER NAME",
    "id": 1,
    "email": "USER EMAIL",
    "energy_id": 1,
    "simulations": [
      {
        "panel_id": 6,
        "worker_cost": 1232.712,
        "total_system_cost": 11248.497,
        "lead_id": 1,
        "project_cost": 2465.424,
        "eletric_materials_cost": 616.356,
        "system_cost": 6163.5599999999995,
        "energy_cost": 36000.0,
        "panel_quantity": 5.0,
        "inversor_id": 2,
        "roi_years": 7.811456249999999,
        "maintanance_cost": 770.4449999999999
      }
    ],
    "phone": "USER PHONE"
  }
]
```

## GET /lead/<lead_id>

header

```json
Authorization: 'Bearer ' + <TOKEN>
```

### Response Return

```json
{
  "lead": {
    "name": "USER NAME",
    "id": 1,
    "email": "USER EMAIL",
    "energy_id": 1,
    "simulations": [
      {
        "panel_id": 6,
        "worker_cost": 1232.712,
        "total_system_cost": 11248.497,
        "lead_id": 1,
        "project_cost": 2465.424,
        "eletric_materials_cost": 616.356,
        "system_cost": 6163.5599999999995,
        "energy_cost": 36000.0,
        "panel_quantity": 5.0,
        "inversor_id": 2,
        "roi_years": 7.811456249999999,
        "maintanance_cost": 770.4449999999999
      }
    ],
    "phone": "USER PHONE"
  },
  "messages": [
    {
      "classification": 5,
      "lead_id": 1,
      "id": 1,
      "message": "THE MESSAGE OF THE CONTACT OF THE LEAD AND THE SELLER",
      "seller_id": 1
    }
  ]
}
```

## POST /message

create a message to a lead, indicate the classification of the simulation 0-5

header

```json
Authorization: 'Bearer ' + <TOKEN>
```

body

```json
{
  "lead_id": 1,
  "seller_id": 1,
  "classification": 5,
  "message": "THE MESSAGE OF THE CONTACT OF THE LEAD AND THE SELLER"
}
```

### Response Return

```json
{
  "id": 1,
  "lead_id": 1,
  "seller_id": 1,
  "classification": 5,
  "message": "THE MESSAGE OF THE CONTACT OF THE LEAD AND THE SELLER"
}
```

## GET /message/<message_id>

get a expecific message

header

```json
Authorization: 'Bearer ' + <TOKEN>
```

### Response Return

```json
{
  "id": 1,
  "lead_id": 1,
  "seller_id": 1,
  "classification": 5,
  "message": "THE MESSAGE OF THE CONTACT OF THE LEAD AND THE SELLER"
}
```

- **Note: this project is create by [Christopher William](https://www.linkedin.com/in/christopher-william-4363321a5/) [Bruno Alexandre Gomes de Souza](https://www.linkedin.com/in/brunoagsouza/), [Cauan França Ramos](https://www.linkedin.com/in/cauan-f-ramos/), [Edson Silva](https://www.linkedin.com/in/edson-silva-fullstack-developer/), [Felipe Matheus Mello de Morais](https://www.linkedin.com/in/felipe-matheus-mello/), see more about!**

## Learn More About [Kenzie Academy](https://kenzie.com.br/)

Somos uma escola norte-americana que veio para o Brasil com o objetivo de ofertar ensino de qualidade para quem deseja trabalhar na área da tecnologia. Temos como foco o aprendizado do aluno, desde o nível técnico de um programador full stack, até soft-skills para entrar no mercado de trabalho.
